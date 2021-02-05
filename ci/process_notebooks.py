"""Process tutorials for Neuromatch Academy

- Filter input file list for .ipynb files
- Check that the cells have been executed sequentially on a fresh kernel
- Strip trailing whitespace from all code lines
- Execute the notebook and fail if errors are encountered
- Extract solution code and write a .py file with the solution
- Replace solution cells with a "hint" image and a link to the solution code
- Redirect Colab-inserted badges to the master branch
- Set the Colab notebook name field based on file path
- Standardize some Colab settings (always have ToC, always hide form cells)
- Clean the notebooks (remove outputs and noisy metadata)
- Write the executed version of the input notebook to its original path
- Write the post-processed notebook to a student/ subdirectory
- Write solution images to a static/ subdirectory
- Write solution code to a solutions/ subdirectory

"""
import os
import re
import sys
import argparse
import hashlib
import typing as t
from io import BytesIO
from binascii import a2b_base64
from copy import deepcopy
import asyncio

from PIL import Image
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbclient.util import run_sync, ensure_async
from nbclient.exceptions import CellControlSignal, CellExecutionError, DeadKernelError


GITHUB_RAW_URL = (
    "https://raw.githubusercontent.com/NeuromatchAcademy/course-content/master"
)
GITHUB_TREE_URL = (
    "https://github.com/NeuromatchAcademy/course-content/tree/master/"
)


class NMAPreprocessor(ExecutePreprocessor):
    """
    Custom subclass of the ExecutePreprocessor for NMA tutorials.

    This class overwrites the execute_cell method to ignore NotImplementedError
    exceptions, which are raised when incomplete exercise functions are called.
    All other errors will be handled as normal.

    """
    # Note: we have to patch the entire async_execute_cell method because it checks
    # for errors with a private method (_check_raise_for_error). It would be cleaner
    # to customize only the error handling method, but alas, that is not allowed.

    async def async_execute_cell(
            self,
            cell: nbformat.NotebookNode,
            cell_index: int,
            execution_count: t.Optional[int] = None,
            store_history: bool = True) -> nbformat.NotebookNode:
        """
        Executes a single code cell.

        To execute all cells see :meth:`execute`.

        Parameters
        ----------
        cell : nbformat.NotebookNode
            The cell which is currently being processed.
        cell_index : int
            The position of the cell within the notebook object.
        execution_count : int
            The execution count assigned to the cell (default: Use kernel response)
        store_history : bool
            Determines if history should be stored in the kernel (default: False).
            Specific to ipython kernels, which can store command histories.
        Returns
        -------
        output : dict
            The execution output payload (or None for no output).
        Raises
        ------
        CellExecutionError
            If execution failed and should raise an exception, this will be raised
            with defaults about the failure.
        Returns
        -------
        cell : NotebookNode
            The cell which was just processed.

        This method was copied from the nbclient library and modified to specifically
        ignore NotImplementedError exceptions. The original code is under the following
        license:

        This project is licensed under the terms of the Modified BSD License
        (also known as New or Revised or 3-Clause BSD), as follows:

        - Copyright (c) 2020-, Jupyter Development Team

        All rights reserved.

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are met:

        Redistributions of source code must retain the above copyright notice, this
        list of conditions and the following disclaimer.

        Redistributions in binary form must reproduce the above copyright notice, this
        list of conditions and the following disclaimer in the documentation and/or
        other materials provided with the distribution.

        Neither the name of the Jupyter Development Team nor the names of its
        contributors may be used to endorse or promote products derived from this
        software without specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
        ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
        WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
        DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
        FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
        DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
        SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
        CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
        OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
        OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

        """
        assert self.kc is not None
        if cell.cell_type != 'code' or not cell.source.strip():
            self.log.debug("Skipping non-executing cell %s", cell_index)
            return cell

        if self.record_timing and 'execution' not in cell['metadata']:
            cell['metadata']['execution'] = {}

        self.log.debug("Executing cell:\n%s", cell.source)
        parent_msg_id = await ensure_async(
            self.kc.execute(
                cell.source,
                store_history=store_history,
                stop_on_error=not self.allow_errors
            )
        )
        # We launched a code cell to execute
        self.code_cells_executed += 1
        exec_timeout = self._get_timeout(cell)

        cell.outputs = []
        self.clear_before_next_output = False

        task_poll_kernel_alive = asyncio.ensure_future(
            self._async_poll_kernel_alive()
        )
        task_poll_output_msg = asyncio.ensure_future(
            self._async_poll_output_msg(parent_msg_id, cell, cell_index)
        )
        self.task_poll_for_reply = asyncio.ensure_future(
            self._async_poll_for_reply(
                parent_msg_id,
                cell,
                exec_timeout,
                task_poll_output_msg,
                task_poll_kernel_alive,
            )
        )
        try:
            exec_reply = await self.task_poll_for_reply
        except asyncio.CancelledError:
            # can only be cancelled by task_poll_kernel_alive when the kernel is dead
            task_poll_output_msg.cancel()
            raise DeadKernelError("Kernel died")
        except Exception as e:
            # Best effort to cancel request if it hasn't been resolved
            try:
                # Check if the task_poll_output is doing the raising for us
                if not isinstance(e, CellControlSignal):
                    task_poll_output_msg.cancel()
            finally:
                raise

        if execution_count:
            cell['execution_count'] = execution_count
        self._check_raise_for_error_nma(cell, exec_reply)
        self.nb['cells'][cell_index] = cell
        return cell

    def _check_raise_for_error_nma(
            self,
            cell: nbformat.NotebookNode,
            exec_reply: t.Optional[t.Dict]) -> None:

        cell_tags = cell.metadata.get("tags", [])
        cell_allows_errors = self.allow_errors or "raises-exception" in cell_tags

        if self.force_raise_errors or not cell_allows_errors:

            if (exec_reply is not None) and exec_reply['content']['status'] == 'error':

                if exec_reply['content']['ename'] != 'NotImplementedError':
                    raise CellExecutionError.from_cell_and_msg(cell,
                                                               exec_reply['content'])

    execute_cell = run_sync(async_execute_cell)


def main(arglist):
    """Process IPython notebooks from a list of files."""
    args = parse_args(arglist)

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

    nb_paths = [arg for arg in args.files if should_process(arg)]
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

        if not sequentially_executed(nb):
            if args.require_sequntial:
                err = (
                    "Notebook is not sequentially executed on a fresh kernel."
                    "\n"
                    "Please do 'Restart and run all' before pushing to Github."
                )
                errors[nb_path] = err
                continue

        # Clean whitespace from all code cells
        clean_whitespace(nb)

        # Run the notebook from top to bottom, catching errors
        print(f"Executing {nb_path}")
        executor = NMAPreprocessor(**exec_kws)
        try:
            executor.preprocess(nb)
        except Exception as err:
            # Log the error, but then continue
            errors[nb_path] = err
        else:
            notebooks[nb_path] = nb

    if errors or args.check_only:
        exit(errors)

    # Further filter the notebooks to run post-processing only on tutorials
    tutorials = {
        nb_path: nb
        for nb_path, nb in notebooks.items()
        if nb_path.startswith("tutorials")
    }

    # Post-process notebooks to remove solution code and write both versions
    for nb_path, nb in tutorials.items():

        # Extract components of the notebook path
        nb_dir, nb_fname = os.path.split(nb_path)
        nb_name, _ = os.path.splitext(nb_fname)

        # Loop through the cells and fix any Colab badges we encounter
        for cell in nb.get("cells", []):
            if has_colab_badge(cell):
                redirect_colab_badge_to_master_branch(cell)

        # Ensure that Colab metadata dict exists and enforce some settings
        add_colab_metadata(nb, nb_name)

        # Clean the original notebook and save it to disk
        print(f"Writing complete notebook to {nb_path}")
        with open(nb_path, "w") as f:
            nb_clean = clean_notebook(nb)
            nbformat.write(nb_clean, f)

        # Create subdirectories, if they don't exist
        student_dir = make_sub_dir(nb_dir, "student")
        static_dir = make_sub_dir(nb_dir, "static")
        solutions_dir = make_sub_dir(nb_dir, "solutions")

        # Generate the student version and save it to a subdirectory
        print(f"Extracting solutions from {nb_path}")
        processed = extract_solutions(nb, nb_dir, nb_name)
        student_nb, static_images, solution_snippets = processed

        # Loop through cells and point the colab badge at the student version
        for cell in student_nb.get("cells", []):
            if has_colab_badge(cell):
                redirect_colab_badge_to_student_version(cell)

        # Write the student version of the notebook
        student_nb_path = os.path.join(student_dir, nb_fname)
        print(f"Writing student notebook to {student_nb_path}")
        with open(student_nb_path, "w") as f:
            clean_student_nb = clean_notebook(student_nb)
            nbformat.write(clean_student_nb, f)

        # Write the images extracted from the solution cells
        print(f"Writing solution images to {static_dir}")
        for fname, image in static_images.items():
            fname = fname.replace("static", static_dir)
            image.save(fname)

        # Write the solution snippets
        print(f"Writing solution snippets to {solutions_dir}")
        for fname, snippet in solution_snippets.items():
            fname = fname.replace("solutions", solutions_dir)
            with open(fname, "w") as f:
                f.write(snippet)

    exit(errors)


def extract_solutions(nb, nb_dir, nb_name):
    """Convert solution cells to markdown; embed images from Python output."""
    nb = deepcopy(nb)
    _, tutorial_dir = os.path.split(nb_dir)

    static_images = {}
    solution_snippets = {}

    nb_cells = nb.get("cells", [])
    for i, cell in enumerate(nb_cells):

        if has_solution(cell):

            # Get the cell source
            cell_source = cell["source"]

            # Hash the source to get a unique identifier
            cell_id = hashlib.sha1(cell_source.encode("utf-8")).hexdigest()[:8]

            # Extract image data from the cell outputs
            cell_images = {}
            for j, output in enumerate(cell.get("outputs", [])):

                fname = f"static/{nb_name}_Solution_{cell_id}_{j}.png"
                try:
                    image_data = a2b_base64(output["data"]["image/png"])
                except KeyError:
                    continue
                cell_images[fname] = Image.open(BytesIO(image_data))
            static_images.update(cell_images)

            # Clean up the cell source and assign a filename
            snippet = "\n".join(cell_source.split("\n")[1:])
            py_fname = f"solutions/{nb_name}_Solution_{cell_id}.py"
            solution_snippets[py_fname] = snippet

            # Convert the solution cell to markdown,
            # Insert a link to the solution snippet script on github,
            # and embed the image as a link to static file (also on github)
            py_url = f"{GITHUB_TREE_URL}/tutorials/{tutorial_dir}/{py_fname}"
            new_source = f"[*Click for solution*]({py_url})\n\n"

            if cell_images:
                new_source += "*Example output:*\n\n"
                for f, img in cell_images.items():

                    url = f"{GITHUB_RAW_URL}/tutorials/{tutorial_dir}/{f}"

                    # Handle matplotlib retina mode
                    dpi_w, dpi_h = img.info["dpi"]
                    w = img.width // (dpi_w // 72)
                    h = img.height // (dpi_h // 72)

                    tag_args = " ".join([
                        "alt='Solution hint'",
                        "align='left'",
                        f"width={w}",
                        f"height={h}",
                        f"src={url}",
                    ])
                    new_source += f"<img {tag_args}>\n\n"

            cell["source"] = new_source
            cell["cell_type"] = "markdown"
            cell["metadata"]["colab_type"] = "text"
            if "outputID" in cell["metadata"]:
                del cell["metadata"]["outputId"]
            if "outputs" in cell:
                del cell["outputs"]
            if "execution_count" in cell:
                del cell["execution_count"]

    return nb, static_images, solution_snippets


def clean_notebook(nb):
    """Remove cell outputs and most unimportant metadata."""
    # Always operate on a copy of the input notebook
    nb = deepcopy(nb)

    # Remove some noisy metadata
    nb.metadata.pop("widgets", None)

    # Set kernel to default Python3
    nb.metadata["kernel"] = {
        "display_name": "Python 3", "language": "python", "name": "python3"
    }

    # Iterate through the cells and clean up each one
    for cell in nb.get("cells", []):

        # Remove blank cells
        if not cell["source"]:
            nb.cells.remove(cell)
            continue

        # Reset cell-level Jupyter metadata
        for key in ["prompt_number", "execution_count"]:
            if key in cell:
                cell[key] = None

        if "metadata" in cell:
            for field in ["collapsed", "scrolled", "ExecuteTime"]:
                cell.metadata.pop(field, None)

        # Reset cell-level Colab metadata
        if "id" in cell["metadata"]:
            if not cell["metadata"]["id"].startswith("view-in"):
                cell["metadata"].pop("id")

        # Remove code cell outputs
        if cell["cell_type"] == "code":
            cell["outputs"] = []

        # Ensure that form cells are hidden by default
        if cell["cell_type"] == "code":
            first_line, *_ = cell["source"].splitlines()
            if "@title" in first_line or "@markdown" in first_line:
                cell["metadata"]["cellView"] = "form"

    return nb


def add_colab_metadata(nb, nb_name):
    """Ensure that notebook has Colab metadata and enforce some settings."""
    if "colab" not in nb["metadata"]:
        nb["metadata"]["colab"] = {}

    # Always overwrite the name and show the ToC/Colab button
    nb["metadata"]["colab"].update({
        "name": nb_name,
        "toc_visible": True,
        "include_colab_link": True,
    })

    # Allow collapsed sections, but default to not having any
    nb["metadata"]["colab"].setdefault("collapsed_sections", [])


def clean_whitespace(nb):
    """Remove trailing whitespace from all code cell lines."""
    for cell in nb.get("cells", []):
        if cell.get("cell_type", "") == "code":
            source_lines = cell["source"].splitlines()
            clean_lines = [line.rstrip() for line in source_lines]
            cell["source"] = "\n".join(clean_lines)


def has_solution(cell):
    """Return True if cell is marked as containing an exercise solution."""
    cell_text = cell["source"].replace(" ", "").lower()
    first_line = cell_text.split("\n")[0]
    return (
        cell_text.startswith("#@titlesolution")
        or "to_remove" in first_line
    )


def has_colab_badge(cell):
    """Return True if cell has a Colab badge as an HTML element."""
    return "colab-badge.svg" in cell["source"]


def redirect_colab_badge_to_master_branch(cell):
    """Modify the Colab badge to point at the master branch on Github."""
    cell_text = cell["source"]
    p = re.compile(r"^(.+/NeuromatchAcademy/course-content/blob/)\w+(/.+$)")
    cell["source"] = p.sub(r"\1master\2", cell_text)


def redirect_colab_badge_to_student_version(cell):
    """Modify the Colab badge to point at student version of the notebook."""
    cell_text = cell["source"]
    p = re.compile(r"(^.+/tutorials/W\dD\d\w+)/(\w+\.ipynb.+)")
    cell["source"] = p.sub(r"\1/student/\2", cell_text)


def sequentially_executed(nb):
    """Return True if notebook appears freshly executed from top-to-bottom."""
    exec_counts = [
        cell["execution_count"]
        for cell in nb.get("cells", [])
        if (
            cell["source"]
            and cell.get("execution_count", None) is not None
        )
    ]
    sequential_counts = list(range(1, 1 + len(exec_counts)))
    # Returns True if there are no executed code cells, which is fine?
    return exec_counts == sequential_counts


def make_sub_dir(nb_dir, name):
    """Create nb_dir/name if it does not exist."""
    sub_dir = os.path.join(nb_dir, name)
    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)
    return sub_dir


def exit(errors):
    """Exit with message and status dependent on contents of errors dict."""
    for failed_file, error in errors.items():
        print(f"{failed_file} failed quality control.")
        print(error)

    status = bool(errors)
    report = "Failure" if status else "Success"
    print("=" * 30, report, "=" * 30)
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
        "--check-only",
        action="store_true",
        dest="check_only",
        help="Only run QC checks; don't do post-processing"
    )
    parser.add_argument(
        "--allow-non-sequential",
        action="store_false",
        dest="require_sequntial",
        help="Don't fail if the notebook is not sequentially executed"
    )
    return parser.parse_args(arglist)


if __name__ == "__main__":

    main(sys.argv[1:])
