"""Process tutorials for Neuromatch Academy

- Excute .ipynb files and report any errors encountered
- Copy the original notebook to a "solutions" folder for TAs
- Remove inputs (but not outputs) from solution cells in original notebook

"""
import os
import sys
import argparse
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def main(arglist):
    """Process IPython notebooks from a list of files."""
    args = parse_args(arglist)

    # Filter to only ipython notebook fikes
    nb_paths = [arg for arg in args.files if arg.endswith(".ipynb")]
    if not nb_paths:
        print("No notebook files found")
        sys.exit(0)

    # Allow environment to override stored kernel name
    exec_kws = {"timeout": 600}
    if "NB_KERNEL" in os.environ:
        exec_kws["kernel_name"] = os.environ["NB_KERNEL"]

    # Defer failures until after processing all notebooks
    errors = {}
    notebooks = {}

    for nb_path in nb_paths:

        # Load the notebook structure
        with open(nb_path) as f:
            nb = nbformat.read(f, nbformat.NO_CONVERT)

        # Run the notebook from top to bottom, catching errors
        print(f"Executing {nb_path}")
        executor = ExecutePreprocessor(**exec_kws)
        try:
            executor.preprocess(nb)
        except Exception as err:
            errors[nb_path] = err
        else:
            notebooks[nb_path] = nb

    if args.checkonly:
        exit(errors)

    # Check compliancy with PEP8, generate a report, but don't fail on issues

    # TODO Check notebook name format?

    # Save the full version of the notebook, which contains solutions
    for nb_path, nb in notebooks.items():

        nb_dir, nb_fname = os.path.split(nb_path)

        # TODO only save out a solutions notebook if some solutions exist?

        # Create a directory for the solutions, if it doesn't exist
        solutions_dir = os.path.join(nb_dir, "solutions")
        if not os.path.exists(solutions_dir):
            os.mkdir(solutions_dir)

        # Write the full notebook (TA verison) to the solutions directory
        solutions_path = os.path.join(solutions_dir, nb_fname)
        print(f"Writing TA notebook to {solutions_path}")
        with open(solutions_path, "w") as f:
            nbformat.write(nb, f)

        # Remove solutions and write the student version of the notebook
        remove_solutions(nb_path, nb)

    exit(errors)


def remove_solutions(nb_path, nb):
    """Remove input source from solution cells with output, or remove cell."""
    print(f"Removing solutions from {nb_path}")

    # Remove the solutions, but keep images they generate
    removed_message = "# Solution removed, here is the example output:"
    nb_cells = nb.get("cells", [])
    for cell in nb_cells:
        cell_text = cell["source"].replace(" ", "").lower()
        if cell_text.startswith("#@titlesolution"):
            if cell["outputs"]:
                cell["source"] = removed_message
            else:
                nb_cells.remove(cell)

    # Write the processed notebook back out to the original path
    with open(nb_path, "w") as f:
        nbformat.write(nb, f)


def exit(errors):
    """Exit with message and status dependent on contents of erros dictionary."""
    for failed_file, error in errors.items():
        print(f"{failed_file} did not execute cleanly.")
        print("Error message:", end="\n")
        print(error)

    status = bool(errors)
    if status:
        print("========== Failure ==========")
    else:
        print("========== Success ==========")
    sys.exit(status)


def parse_args(arglist):
    """Handle the command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Process neuromatch tutorial notebooks",
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="File name(s) to process. Will filter for .ipynb extension."
    )
    parser.add_argument(
        "--checkonly",
        action="store_true",
        help="Only check that the notebook can execute"
    )
    return parser.parse_args(arglist)


if __name__ == "__main__":

    main(sys.argv[1:])
