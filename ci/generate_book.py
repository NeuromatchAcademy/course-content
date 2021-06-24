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
        notebook_file_path = f"{directory}/{m['day']}_Intro.ipynb"
        if os.path.exists(notebook_file_path):
            chapter['sections'].append({'file': notebook_file_path})
            pre_process_notebook(notebook_file_path)

        # Add tutorials
        for i in range(m['tutorials']):
            notebook_file_path = f"{directory}/student/{m['day']}_Tutorial{i + 1}.ipynb"
            chapter['sections'].append({'file': notebook_file_path})
            pre_process_notebook(notebook_file_path)

        # Generate outro video page
        notebook_file_path = f"{directory}/{m['day']}_Outro.ipynb"
        if os.path.exists(notebook_file_path):
            chapter['sections'].append({'file': notebook_file_path})
            pre_process_notebook(notebook_file_path)

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


def pre_process_notebook(file_path):
    #try:
    with open(file_path, encoding="utf-8") as read_notebook:
        content = json.load(read_notebook)
    pre_processed_content = open_in_colab_new_tab(content)
    pre_processed_content = link_hidden_cells(pre_processed_content)
    with open(file_path, "w", encoding="utf-8") as write_notebook:
        json.dump(pre_processed_content, write_notebook, indent=1, ensure_ascii=False)
    # except Exception:
    #     print("Exception occurred while trying to pre_process file = {}. Skipping this file.".format(file_path))
    #     traceback.print_exc()


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
    updated_cells = cells.copy()

    i_updated_cell = 0
    for i_cell, cell in enumerate(cells):
        updated_cell = updated_cells[i_updated_cell]
        if "source" not in cell:
            continue
        source = cell['source'][0]

        if source.startswith("#") and '@title' not in source:
            header_level = source.count('#')

        if '#@title' in source or '#@markdown' in source:
            if 'metadata' not in cell:
                updated_cell['metadata'] = {}
            if 'tags' not in cell['metadata']:
                updated_cell['metadata']['tags'] = []

            # Check if cell is video one
            if 'YouTubeVideo' in ''.join(cell['source']) or 'IFrame' in ''.join(cell['source']):
                if "remove-input" not in cell['metadata']['tags']:
                    updated_cell['metadata']['tags'].append("remove-input")
            else:
                if "hide-input" not in cell['metadata']['tags']:
                    updated_cell['metadata']['tags'].append("hide-input")

            # If header is lost, create one in markdown
            if '@title' in source:
                if source.split('@title')[1] != '':
                    header_cell = {
                        'cell_type': 'markdown',
                        'metadata': {},
                        'source': ['#'*(header_level + 1) + ' ' + source.split('@title')[1]]}
                    updated_cells.insert(i_updated_cell, header_cell)
                    i_updated_cell += 1
        i_updated_cell += 1

    content['cells'] = updated_cells
    return content


if __name__ == '__main__':
    main()