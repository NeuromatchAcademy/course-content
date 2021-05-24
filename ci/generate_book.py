import yaml


def main():
    with open('tutorials/materials.yml') as fh:
        materials = yaml.load(fh, Loader=yaml.FullLoader)
    
    toc = [{'file': 'intro.md'},
           {'part': 'Preliminary', 'chapters': []},
           {'part': 'Week 1', 'chapters': []},
           {'part': 'Week 2', 'chapters': []},
           {'part': 'Week 3', 'chapters': []}]
    
    for m in materials:
        directory = f"tutorials/{m['day']}_{''.join(m['name'].split())}"
        chapter = {'file': f"{directory}/README.md", 
                   'title': m['name'],
                   'sections': []}
        part = int(m['day'][1]) + 1
        
        for i in range(m['tutorials']):
            directory = f"tutorials/{m['day']}_{''.join(m['name'].split())}"
            notebook = f"{m['day']}_Tutorial{i+1}.ipynb"
            chapter['sections'].append({'file': f"{directory}/{notebook}"})

        toc[part]['chapters'].append(chapter)
    
    with open('book/_toc.yml', 'w') as fh:
        yaml.dump(toc, fh)


if __name__ == '__main__':
    main()
