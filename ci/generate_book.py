import os

import yaml
from jinja2 import Template
import traceback
import json
from bs4 import BeautifulSoup


def main():
    with open('tutorials/materials.yml') as fh:
        materials = yaml.load(fh, Loader=yaml.FullLoader)

    toc = {'Pre-reqs Refresher': {'part': 'Pre-reqs Refresher', 'chapters': []},
           'Intro to Modeling': {'part': 'Intro to Modeling', 'chapters': []},
           'Machine Learning': {'part': 'Machine Learning', 'chapters': []},
           'Dynamical Systems': {'part': 'Dynamical Systems', 'chapters': []},
           'Stochastic Processes': {'part': 'Stochastic Processes', 'chapters': []}}

    for m in materials:
        directory = f"{m['day']}_{''.join(m['name'].split())}"

        # Make temporary chapter title file
        with open(f"tutorials/{directory}/chapter_title.md",
                  "w+") as title_file:
            title_file.write(f"# {m['name']}")

        chapter = {'file': f"tutorials/{directory}/chapter_title.md",
                   'title': f"{m['name']} ({m['day']})",
                   'sections': []}
        print(m['day'])
        part = m['category']
        directory = f"tutorials/{m['day']}_{''.join(m['name'].split())}"

        # Generate intro video page
        if os.path.exists(f"{directory}/{m['day']}_Intro.ipynb"):
            chapter['sections'].append({'file': f"{directory}/{m['day']}_Intro.ipynb"})

        # Add tutorials
        for i in range(m['tutorials']):
            notebook = f"{m['day']}_Tutorial{i + 1}.ipynb"
            chapter['sections'].append({'file': f"{directory}/student/{notebook}"})
            # Pre process notebooks
            notebook_file_path = f"{directory}/student/{notebook}"
            pre_process_notebook(notebook_file_path)

        # Generate outro video page
        if os.path.exists(f"{directory}/{m['day']}_Outro.ipynb"):
            chapter['sections'].append({'file': f"{directory}/{m['day']}_Outro.ipynb"})

        # Add further reading page
        chapter['sections'].append({'file': f"{directory}/further_reading.md"})

        # Add chapter
        toc[part]['chapters'].append(chapter)

    # Turn toc into list
    toc_list = [{'file': 'intro.md'}]
    for key in toc.keys():
        toc_list.append(toc[key])

    with open('book/_toc.yml', 'w') as fh:
        yaml.dump(toc_list, fh)


def convert_youtube_url_to_embed_url(url):
    # TODO: Support Chinese equivalent URLs
    url_key = url.split("=")[1]
    return "https://www.youtube.com/embed/" + url_key


def generate_page(info, directory, chapter, file_type):
    if file_type.lower() in info:
        chapter['sections'].append({'file': f'tutorials/{directory}/{file_type.lower()}_vid.md'})
        with open(os.path.join("ci", "resources", "intro_outro_template.txt"), encoding="utf-8") as f:
            template_string = f.read()
            template = Template(template_string)
            for slides in info['slides']:
                if slides['title'] == file_type:
                    prepared_template_string = template.render(type=file_type,
                                                               video_source_url=convert_youtube_url_to_embed_url(
                                                                   info[file_type.lower()]),
                                                               slide_source_url=slides['link'])
                    with open(os.path.join("tutorials", directory, file_type.lower() + "_vid.md"),
                              "w+") as intro_vid_file:
                        intro_vid_file.write(prepared_template_string)
    return chapter


def pre_process_notebook(file_path):
    try:
        with open(file_path, encoding="utf-8") as read_notebook:
            content = json.load(read_notebook)
        pre_processed_content = open_in_colab_new_tab(content)
        pre_processed_content = link_hidden_cells(pre_processed_content)
        with open(file_path, "w", encoding="utf-8") as write_notebook:
            json.dump(pre_processed_content, write_notebook, indent=1, ensure_ascii=False)
    except Exception:
        print("Exception occurred while trying to pre_process file = {}. Skipping this file.".format(file_path))
        traceback.print_exc()


def open_in_colab_new_tab(content):
    cells = content['cells']
    parsed_html = BeautifulSoup(cells[0]['source'][0], "html.parser")
    for anchor in parsed_html.findAll('a'):
        # Open in new tab
        anchor['target'] = '_blank'
    cells[0]['source'][0] = str(parsed_html)
    return content


def link_hidden_cells(content):
    cells = content['cells']
    for cell in cells:
        if "source" not in cell:
            continue
        source = cell['source'][0]
        if source.startswith("#@title") or source.startswith("# @title"):
            if 'metadata' not in cell:
                cell['metadata'] = {}
            if 'tags' not in cell['metadata']:
                cell['metadata']['tags'] = []
            if "hide-input" not in cell['metadata']['tags']:
                cell['metadata']['tags'].append("hide-input")
    return content


if __name__ == '__main__':
    main()