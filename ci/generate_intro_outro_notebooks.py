import os

import yaml
from jinja2 import Template
from process_notebooks import add_colab_metadata, clean_notebook, redirect_colab_badge_to_master_branch, has_colab_badge
import nbformat

def main():

    with open('tutorials/materials.yml') as fh:
        materials = yaml.load(fh, Loader=yaml.FullLoader)

    for m in materials:
        print(m['day'])
        directory = f"{m['day']}_{''.join(m['name'].split())}"

        # Generate intro video page
        generate_page(m, directory, "Intro")

        # Add colab metadata/link/hidden cells
        format_to_colab(m, directory, "Intro")


def convert_video_url_to_id(url):
    if 'youtube' in url:
        url_key = url.split("=")[1]
    elif 'bilibili' in url:
        url_key = url.split('video/')[-1]
        if url_key[-1] == '/':
            url_key = url_key[:-1]
    else:
        url_key = ''
    return url_key


def generate_page(info, directory, file_type):
    if file_type.lower() in info:
        with open(os.path.join("ci", "resources", f"{file_type.lower()}_template.ipynb"), encoding="utf-8") as f:
            template_string = f.read()
            template = Template(template_string)
            for slides in info['slides']:
                if slides['title'] == file_type:
                    prepared_template_string = template.render(playlist = info['playlist'],
                                                               youtube_id=convert_video_url_to_id(
                                                                   info[file_type.lower()]),
                                                               bilibili_id=convert_video_url_to_id(
                                                                   info[f"{file_type.lower()}_bilibili"]),
                                                               slides_link=slides['link'],
                                                               directory_path=f"tutorials/{directory}",
                                                               day = info['day'],
                                                               day_name = directory)
                    with open(f"tutorials/{directory}/{info['day']}_{file_type}.ipynb",
                              "w+") as intro_vid_file:
                        intro_vid_file.write(prepared_template_string)

def format_to_colab(info, directory, file_type):

    # Load the notebook structure
    nb_path = f"tutorials/{directory}/{info['day']}_{file_type}.ipynb"

    if os.path.isfile(nb_path):
        with open(nb_path) as f:
            nb = nbformat.read(f, nbformat.NO_CONVERT)

        # Extract components of the notebook path
        nb_dir, nb_fname = os.path.split(nb_path)
        nb_name, _ = os.path.splitext(nb_fname)

        # Loop through the cells and fix any Colab badges we encounter
        for cell in nb.get("cells", []):
            if has_colab_badge(cell):
                redirect_colab_badge_to_master_branch(cell)

        # Ensure that Colab metadata dict exists and enforce some settings
        add_colab_metadata(nb, nb_name)

        # Clean the original notebook and save it to disk
        print(f"Writing complete notebook to {nb_path}")
        with open(nb_path, "w") as f:
            nb_clean = clean_notebook(nb)
            nbformat.write(nb_clean, f)

if __name__ == '__main__':
    main()