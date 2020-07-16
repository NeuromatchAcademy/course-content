"""From a list of files, select process-able notebooks and print."""
import os
import sys

if __name__ == "__main__":

    _, *files = sys.argv

    # Filter paths from the git manifest
    # - Only process .ipynb
    # - Don't process student notebooks
    # - Don't process deleted notebooks
    def should_process(path):
        return all([
            path.endswith(".ipynb"),
            "student/" not in path,
            os.path.isfile(path),
        ])

    nb_paths = [f for f in files if should_process(f)]
    print(" ".join(nb_paths))
