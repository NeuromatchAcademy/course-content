#! /usr/bin/env python
"""Check that exercise code matches solution code.

Exercises are allowed to deviate from solutions in several ways:

- Exercise code may replace solution code with an ellipsis (...)
- Exercise code may have "commented-out" solution code

Additionally:

- Docstrings are currently ignored
- Blank lines are ignored

This script will report whether exercises and solutions otherwise match.

"""
import os
import re
import sys
import argparse
from textwrap import dedent
from fuzzywuzzy import fuzz
import nbformat


def main(arglist):

    args = parse_args(arglist)

    if "skip verification" in args.commit_message:
        # Putting this logic here as I didn't have time to figure
        # out how to do it in the github actions workflow
        print("Skipping exercise verification")
        sys.exit(0)

    # Track overall status
    failure = False
    unmatched = {}

    for nb_fpath in args.files:

        _, nb_name = os.path.split(nb_fpath)
        unmatched[nb_name] = []

        # Load the notebook file
        with open(nb_fpath) as f:
            nb = nbformat.read(f, nbformat.NO_CONVERT)

        for i, cell in enumerate(nb.get("cells", [])):

            # Detect solution cells based on removal tag
            if has_solution(cell):

                # Find a corresponding exercise cell
                # (Assume it is the previous *code* cell)
                j, stub_cell = 1, None
                while (i - j):
                    stub_cell = nb["cells"][i - j]
                    if stub_cell["cell_type"] == "code":
                        break
                    else:
                        stub_cell = None
                    j += 1
                if stub_cell is None:
                    continue

                # Extract the code and comments from both cells
                stub_code, stub_comments = logical_lines(stub_cell["source"])
                solu_code, solu_comments = logical_lines(cell["source"])

                # Identify violations in the exercise cell
                unmatched_code = unmatched_lines(stub_code, solu_code)
                unmatched_comments = unmatched_lines(
                    stub_comments, solu_code + solu_comments
                )
                unmatched[nb_name].append((unmatched_code, unmatched_comments))
                if unmatched_code or unmatched_comments:
                    failure = True

    # Report the results for this noteobokk
    for nb_name, nb_unmatched in unmatched.items():
        print()
        print("---" + nb_name + "-" * (69 - 5 - len(nb_name)))
        for exercise, (code, comments) in enumerate(nb_unmatched, 1):
            report(exercise, code, comments)

    # Print overall summary and exit with return code
    message = "Failure" if failure else "Success"
    print("\n" + "=" * 30, message, "=" * 30)
    sys.exit(failure)


def report(exercise, code, comment, thresh=50):
    """Print information about unmatched code and comments in an exercise."""
    code_status = "FAIL" if code else "PASS"
    comment_status = "FAIL" if comment else "PASS"
    print(
        f"Exercise {exercise} | Code {code_status} | Comments {comment_status}"
    )

    for kind, unmatched in zip(["Code", "Comment"], [code, comment]):
        for (score, stub, solu) in unmatched:
            if score < thresh:
                print(f"  {kind} without close match:")
                print(f"  * {stub}")
            else:
                print(f"  {kind} with close mismatch ({score}%)")
                print(f"  + {stub}")
                print(f"  - {solu}")


def logical_lines(func_str):
    """Extract code and block comments from cell string."""
    # Standardize docstring string format
    func_str = func_str.replace("'''", '"""')

    # Define a regular expression to remove comments
    pattern = re.compile(r"^([^#]*)\s*#* {0,1}(.*?)\s*$")

    code_lines = []
    comment_lines = []

    making_xkcd_plot = False
    reading_block_comment = False

    for line in func_str.split("\n"):

        # Detect and ignore lines within multi-line comments
        # - triple quotes (docstrings)
        # - comment hashmark fences
        comment_block_fence = dedent(line).startswith('"""') or "###" in line
        if reading_block_comment:
            if comment_block_fence:
                reading_block_comment = False
            continue
        else:

            # Detect and ignore single-line docstrings
            text = line.strip()
            single_line_docstring = (
                text.startswith('"""')
                and text.endswith('"""')
                and len(text) > 3
            )
            if single_line_docstring:
                continue

            # Otherwise, assume we are starting a comment block
            if comment_block_fence:
                reading_block_comment = True
                continue

        match = pattern.match(line)
        if match:

            # Split the line on the first comment hash encountered
            code_line = match.group(1)
            comment_line = match.group(2)

            # If there is code before the comment, assume comment is inline
            # use entire line (allows inline comments in commented-out code)
            if dedent(code_line):
                code_line = match.group(0)

            # Handle xkcd context, which is always last thing in solution cell
            if "plt.xkcd()" in code_line:
                making_xkcd_plot = True
                continue
            if making_xkcd_plot:
                code_line = code_line[2:]

            # Check for reasons to ignore the line, otherwise keep it

            if not skip_code(code_line):
                code_lines.append(code_line)

            if not dedent(code_line) and not skip_comment(comment_line):
                comment_lines.append(comment_line)

    return code_lines, comment_lines


def unmatched_lines(stub_lines, solu_lines):
    """Identify lines in the exercise stub without a match in the solution."""
    unmatched = []

    for stub_line in stub_lines:

        # When we don't match, we want to track lines that are close
        best_score = 0
        best_line = ""

        for line in solu_lines:

            # Match whole lines or parts of lines that need completion
            if "..." in stub_line:
                part_scores = []
                for part in stub_line.split("..."):
                    if not part:
                        continue
                    part_scores.append(fuzz.partial_ratio(part, line))
                score = min(part_scores)
            else:
                score = fuzz.ratio(stub_line, line)

            if score > best_score:
                best_score = score
                best_line = line

        # Track all lines that are not perfect matches
        if best_score < 100:
            unmatched.append((best_score, stub_line, best_line))

    return unmatched


def skip_code(line):
    """Return True if a code line should be skipped based on contents."""
    line = dedent(line)
    return not line or "NotImplementedError" in line


def skip_comment(line):
    """Return True if a comment line should be skipped based on contents."""
    line = dedent(line)
    return not line or "to_remove" in line or "uncomment" in line.lower()


def has_solution(cell):
    """Return True if cell is marked as containing an exercise solution."""
    cell_text = cell["source"].replace(" ", "").lower()
    first_line = cell_text.split("\n")[0]
    return (
        cell_text.startswith("#@titlesolution")
        or "to_remove" in first_line
        and "explanation" not in first_line
    )


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
        "--commit-message",
        default="",
        help="Will exit cleanly if message contains 'skip verify'",
    )
    return parser.parse_args(arglist)


if __name__ == "__main__":

    main(sys.argv[1:])
