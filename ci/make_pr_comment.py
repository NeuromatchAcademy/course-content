"""Write a comment to be added to a pull request on github:

- Add Colab badges for the branch version of the notebooks
- Run the code linter over the notebooks and include the report

"""
import os
import sys
import argparse
import subprocess


def main(arglist):

    args = parse_args(arglist)

    # Start with a table of badges for the branch versions of the notebooks
    comment_lines = [
        make_colab_badge_table(args.branch, args.notebooks),
    ]

    # Add a code report (under a details tag) for each notebook
    for nb_fpath in args.notebooks:
        _, nb_fname = os.path.split(nb_fpath)
        nb_name, _ = os.path.splitext(nb_fname)
        comment_lines.extend([
            "\n"
            "<details>",
            f"<summary><i>{nb_name} code report</i></summary>",
            make_lint_report(nb_fpath),
            "---",
            "",
            "</details>",
        ])

    # Dump to stdout or a file
    comment = "\n".join(comment_lines)
    if args.output is None:
        print(comment, flush=True)
    else:
        with open(args.output, "w") as fid:
            fid.write(comment)


def make_lint_report(nb_fpath):
    """Run the tutorial linter on a notebook and capture the output."""
    cmdline = ["python", "ci/lint_tutorial.py", nb_fpath]
    res = subprocess.run(cmdline, capture_output=True)
    return res.stdout.decode()


def make_colab_badge_table(branch, notebooks):
    """Add Colab badges for the branch version of each notebook."""
    header = []
    divider = []
    badges = []
    for nb_fpath in notebooks:
        _, nb_fname = os.path.split(nb_fpath)
        nb_name, _ = os.path.splitext(nb_fname)
        header.append(nb_name)
        badges.append(make_colab_badge(branch, nb_fpath))
        divider.append("-")

    rows = header, divider, badges
    table = "\n".join(
       ["|" + "|".join(row) + "|" for row in rows]
    )
    return table


def make_colab_badge(branch, local_path):
    """Generate a Google Colaboratory badge for a notebook on github."""
    alt_text = "Open In Colab"
    badge_svg = "https://colab.research.google.com/assets/colab-badge.svg"
    url = (
        "https://colab.research.google.com/"
        "github/NeuromatchAcademy/course-content/blob/"
        f"{branch}/{local_path}"
    )
    return f"[![{alt_text}]({badge_svg})]({url})"


def parse_args(arglist):

    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", default="master")
    parser.add_argument("--output")
    parser.add_argument("notebooks", nargs="*")
    return parser.parse_args(arglist)


if __name__ == "__main__":

    main(sys.argv[1:])
