"""Print names of derivative files that are no longer used in the notebooks."""
from glob import glob

if __name__ == "__main__":

    day_paths = glob("tutorials/W?D?_*")
    for day_path in sorted(day_paths):

        # Read all of the text for this day's student notebooks into one string
        student_notebooks = glob(f"{day_path}/student/*.ipynb")
        notebook_text = ""
        for nb_path in student_notebooks:
            with open(nb_path) as f:
                notebook_text += f.read()

        # Find solution images and scripts
        solution_pattern = "W?D?_*_Solution*"
        static_paths = glob(f"{day_path}/static/{solution_pattern}")
        script_paths = glob(f"{day_path}/solutions/{solution_pattern}")

        # Print paths that are not referenced in the notebooks
        for path in sorted(static_paths + script_paths):
            if path not in notebook_text:
                print(path)
