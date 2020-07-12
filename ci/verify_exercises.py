#! /usr/bin/env python
import re
import sys
from textwrap import dedent
from fuzzywuzzy import fuzz
import nbformat


def main(nb_fpath):

    with open(nb_fpath) as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)

    exercise = 0
    for i, cell in enumerate(nb.get("cells", [])):

        if has_solution(cell):

            exercise += 1

            j = 1
            while (i - j):
                stub_cell = nb["cells"][i - j]
                if stub_cell["cell_type"] == "code":
                    break
                j += 1

            stub_code, stub_comments = logical_lines(stub_cell["source"])
            solu_code, solu_comments = logical_lines(cell["source"])

            unmatched_code = unmatched_lines(stub_code, solu_code)
            unmatched_comments = unmatched_lines(
                stub_comments, solu_code + solu_comments
            )

            print("-" * 88)
            print(f"Exercise {exercise}")
            report("Code", unmatched_code)
            report("Comment", unmatched_comments)


def report(kind, unmatched, thresh=50):

    if not unmatched:
        print(f"{kind}: All perfect")
    for (score, stub, solu) in unmatched:
        if score < thresh:
            print(f"{kind} without close match:")
            print(f"* {stub}")
        else:
            print(f"{kind} with close mismatch ({score}%)")
            print(f"+ {stub}")
            print(f"- {solu}")


def logical_lines(func_str):

    # Standardize docstring string format
    func_str = func_str.replace("'''", '"""')

    # Define a regular expression to remove comments
    pattern = re.compile(r"^([^#]*)\s*#*\s*(.*?)\s*$")

    code_lines = []
    comment_lines = []

    making_xkcd_plot = False
    reading_block_comment = False

    for line in func_str.split("\n"):

        # Detect and ignore non-assigned block strings:
        # - triple quotes (docstrings)
        # - comment hashmark fences
        comment_block_fence = dedent(line).startswith('"""') or "#####" in line
        if reading_block_comment:
            if comment_block_fence:
                reading_block_comment = False
            continue
        else:
            if comment_block_fence:
                reading_block_comment = True
                continue

        match = pattern.match(line)
        if match:

            # Use nonn-commented component of the line
            code_line = match.group(1)
            comment_line = match.group(2)

            # Handle xkcd context, which is always last thing in solution cell
            if "with plt.xkcd()" in code_line:
                making_xkcd_plot = True
                continue
            if making_xkcd_plot:
                code_line = dedent(code_line)

            # Check for reasons to ignore the line, otherwise keep it

            if not skip_code(code_line):
                code_lines.append(code_line)

            if not dedent(code_line) and not skip_comment(comment_line):
                comment_lines.append(comment_line)

    return code_lines, comment_lines


def unmatched_lines(stub_lines, solu_lines):

    unmatched = []

    for stub_line in stub_lines:

        best_score = 0
        best_line = ""

        for line in solu_lines:

            if "..." in stub_line:
                part_scores = []
                for part in stub_line.split("..."):
                    part_scores.append(fuzz.partial_ratio(part, line))
                score = max(part_scores)
            else:
                score = fuzz.ratio(stub_line, line)

            if score > best_score:
                best_score = score
                best_line = line

        if best_score < 100:
            unmatched.append((best_score, stub_line, best_line))

    return unmatched


def skip_code(line):

    line = dedent(line)
    return not line or "NotImplementedError" in line


def skip_comment(line):

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


if __name__ == "__main__":

    try:
        _, nb_fpath = sys.argv
    except Exception:
        sys.exit("USAGE: python verify_exercies.py <nb_fpath>")

    main(nb_fpath)
