"""Lint tutorial notebooks with pyflakes and pycodestyle (aka flake8).

Running this script on a notebook will print a report of issues flagged by
pyflakes (which checks some aspects of code quality) and pycodestyle (which
checks adherence to the PEP8 stylistic standards).

Note that these checks do not capture all potential issues with a codebase,
and some checks will false-alarm because of deliberate choices we have made
about how to write tutorials. Nevertheless, this can be an easy way to flag
potential issues.

Requires nbformat (part of Jupyter) and flake8.

"""
import os
import io
import re
import sys
import argparse
import tempfile
import subprocess
import collections
import nbformat
from pyflakes.api import check
from pyflakes.reporter import Reporter


def main(arglist):

    args = parse_args(arglist)

    _, fname = os.path.split(args.path)

    script, cell_lines = extract_code(args.path)
    warnings, errors = check_code(script)
    violations = check_style(script)

    if args.brief:
        report_brief(fname, warnings, errors, violations)
    else:
        line_map = remap_line_numbers(cell_lines)
        report_verbose(fname, warnings, errors, violations, line_map)


def parse_args(arglist):

    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("path", help="Path to notebook file")
    parser.add_argument("--brief", action="store_true",
                        help="Print brief report (useful for aggregating)")

    return parser.parse_args(arglist)


def extract_code(nb_fname):
    """Turn code cells from notebook into a script, track cell sizes."""
    with open(nb_fname) as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)

    script_lines = []
    cell_lengths = []
    for cell in nb.get("cells", []):
        if cell["cell_type"] == "code":
            cell_lines = cell.get("source", "").split("\n")
            cell_lengths.append(len(cell_lines))
            for line in cell_lines:
                if line and line[0] in ["!", "%"]:  # IPython syntax
                    line = "# " + line
                script_lines.append(line)

    script = "\n".join(script_lines)

    return script, cell_lengths


def check_code(script):
    """Run pyflakes checks over the script and capture warnings/errors."""
    errors = io.StringIO()
    warnings = io.StringIO()
    reporter = Reporter(warnings, errors)
    check(script, "notebook", reporter)

    warnings.seek(0)
    errors.seek(0)

    return warnings, errors


def check_style(script):
    """Write a temporary script and run pycodestyle (PEP8) on it."""

    with tempfile.NamedTemporaryFile("w", suffix=".py") as f:

        f.write(script)

        cmdline = [
            "pycodestyle",
            "--ignore=E111,E114",
            "--max-line-length=88",
            f.name,
        ]
        res = subprocess.run(cmdline, capture_output=True)

    output = res.stdout.decode().replace(f.name, "f").split("\n")

    if not output:
        return collections.Counter()

    error_classes = []
    pat = re.compile(r"^f:\d+:\d+: (\w\d{3}) (.*)$")
    for line in output:
        m = pat.match(line)
        if m is not None:
            error_classes.append(f"{m.group(1)} ({m.group(2)})")

    return collections.Counter(error_classes)


def remap_line_numbers(cell_lines):
    """Create a mapping from script line number to notebook cell/line."""
    line_map = {}
    cell_start = 0
    for cell, cell_length in enumerate(cell_lines, 1):
        for line in range(1, cell_length + 1):
            line_map[cell_start + line] = cell, line
        cell_start += cell_length
    return line_map


def report_brief(fname, warnings, errors, violations):
    """Print a single-line report, suibtable for aggregation."""
    n_warnings = len(warnings.read().splitlines())
    n_errors = len(errors.read().splitlines())
    n_violations = len(list(violations.elements()))
    print(f"{fname} {n_warnings + n_errors} {n_violations}")


def report_verbose(fname, warnings, errors, violations, line_map):
    """Report every pyflakes problem and more codestyle information."""
    s = f"Code report for {fname}"
    print("", s, "=" * len(s), sep="\n")

    s = "Quality (pyflakes)"
    print("", s, "-" * len(s), "", sep="\n")

    warning_lines = reformat_line_problems(warnings, line_map)
    error_lines = reformat_line_problems(errors, line_map, "ERROR in ")

    issues = warning_lines + error_lines
    print(f"Total code issues: {len(issues)}")
    if issues:
        print()
        print("\n".join(warning_lines + error_lines))

    s = "Style (pycodestyle)"
    print("", s, "-" * len(s), "", sep="\n")

    n = len(list(violations.elements()))
    print(f"Total PEP8 violations: {n}")

    # TODO parametrize n_most_common
    if violations:
        print()
        print("Common problems:")
        for code, count in violations.most_common(10):
            plural = "" if count == 1 else "s"
            print(f"- {count} instance{plural} of {code}")

    print("")


def reformat_line_problems(stream, line_map, prefix=""):
    """Reformat a pyflakes output stream for notebook cells."""
    pat = re.compile(r"^\w*:(\d+):\d+ (.+)$")

    new_lines = []
    orig_lines = stream.read().splitlines()

    for line in orig_lines:
        m = pat.match(line)
        if m:
            cell, line = line_map[int(m.group(1))]
            new_lines.append(
                f"{prefix}Cell {cell}, Line {line}: {m.group(2)}"
            )

    return new_lines


if __name__ == "__main__":

    main(sys.argv[1:])
