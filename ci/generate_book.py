import os

import yaml
from jinja2 import Template


def main():
    with open('materials.yml') as fh:
        materials = yaml.load(fh, Loader=yaml.FullLoader)

    toc = {'Pre-reqs Refresher': {'part': 'Pre-reqs Refresher', 'chapters': []},
           'Intro to Modeling': {'part': 'Intro to Modeling', 'chapters': []},
           'Machine Learning': {'part': 'Machine Learning', 'chapters': []},
           'Dynamical Systems': {'part': 'Dynamical Systems', 'chapters': []},
           'Stochastic Processes': {'part': 'Stochastic Processes', 'chapters': []}}

    for m in materials:
        directory = f"{m['day']}_{''.join(m['name'].split())}"
        chapter = {'file': f"tutorials/{directory}/intro_text.md",
                   'title': f"{m['name']} ({m['day']})",
                   'sections': []}
        print(m['day'])
        part = m['category']

        # Generate intro video page
        chapter = generate_page(m, directory, chapter, "Intro")

        # Add tutorials
        for i in range(m['tutorials']):
            directory = f"tutorials/{m['day']}_{''.join(m['name'].split())}"
            notebook = f"{m['day']}_Tutorial{i + 1}.ipynb"
            chapter['sections'].append({'file': f"{directory}/student/{notebook}"})

        # Generate outro video page
        chapter = generate_page(m, f"{m['day']}_{''.join(m['name'].split())}", chapter, "Outro")

        toc[part]['chapters'].append(chapter)

    # Turn toc into list
    toc_list = [{'file': 'intro.md'}]
    for key in toc.keys():
        toc_list.append(toc[key])

    with open('_toc.yml', 'w') as fh:
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


if __name__ == '__main__':
    main()
