import os
import sys
import argparse
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def main(arglist):

    args = parse_args(arglist)

    # Filter to only ipython notebook fikes
    nb_files = [arg for arg in args.files if arg.endswith(".ipynb")]
    if not nb_files:
        print("No notebook files found")
        sys.exit(0)

    # Allow environment to override stored kernel name
    exec_kws = {"timeout": 600}
    if "NB_KERNEL" in os.environ:
        exec_kws["kernel_name"] = os.environ["NB_KERNEL"]

    errors = {}

    for nb_file in nb_files:

        # Load the notebook structure
        with open(nb_file) as f:
            nb = nbformat.read(f, nbformat.NO_CONVERT)

        # Run the notebook from top to bottom
        print(f"Executing {nb_file}")
        executor = ExecutePreprocessor(**exec_kws)
        try:
            executor.preprocess(nb)
        except Exception as err:
            errors[nb_file] = err

    if args.checkonly:
        exit(errors)

    exit(errors)


def exit(errors):

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