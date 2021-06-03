import yaml


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
        chapter = {'file': f"{directory}/intro_text.md",
                   'title': f"{m['name']} ({m['day']})",
                   'sections': []}
        print(m['day'])
        part = m['category']

        # Make intro video page

        # Add tutorials
        for i in range(m['tutorials']):
            directory = f"{m['day']}_{''.join(m['name'].split())}"
            notebook = f"{m['day']}_Tutorial{i+1}.ipynb"
            chapter['sections'].append({'file': f"{directory}/student/{notebook}"})

        # Make outro video page

        toc[part]['chapters'].append(chapter)


    # Turn toc into list
    toc_list = [{'file': 'intro.md'}]
    for key in toc.keys():
        toc_list.append(toc[key])

    with open('tutorials/_toc.yml', 'w') as fh:
        yaml.dump(toc_list, fh)


if __name__ == '__main__':
    main()
