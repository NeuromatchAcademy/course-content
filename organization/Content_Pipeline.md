# Neuromatch Academy Content Pipeline

This document summarizes the pipeline from content creation to publishing, focusing on practical details relating to the Tutorials.

## Content Creation

The Content Creation team produces Tutorials to accompany their lecture videos. The tutorial notebooks take full advantage of the Jupyter/Colab literate programming environment. They weave together expository prose, math, embedded videos, code, and interactive exercises to make the concepts from the lectures concrete.

The tutorials are made interactive in two ways: exercises and interactive "demos", or "widgets".

Exercises present students with a coding challenge: they must implement some of the ideas in the tutorial. Exercises are meant to encourage deeper engagement with the ideas and conceptual understanding; the actual coding should be straightforward. Each exercise should require not more than a few lines to be written. Exercises are typically structured as a function with clearly defined inputs and outputs and a skeleton describing the operations that must be carried out. Use comments to describe the logic of the function, and provide partial code with `...` indicating where the code needs to be completed.

Exercises cells should include a bit of code the calls the exercise function and produces a visual cue about success or failure -- typically in the form of a plot. An incomplete exercise function should raise a `NotImplementedError` exception with a clear message that the student has a task to complete.

When writing the tutorial notebooks, the exercise cells should be duplicated. One cell should provide the incomplete exercise "stub", and the following cell should provide the exercise solution. The solution should look just like the exercise stub, but the relevant sections should be completed. Solution cells should start with a comment reading `# to_remove solution`; they will be automatically removed during notebook production (see below).

Tutorials should also make use of the [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/) library for interactivity. These "demos" do not require coding, but they build intuition by letting students play with the parameters of a function and see the result through changes in a plot. Interactive demos should pose thought questions to guide the students' interactions and, they can discuss possible answers to those questions in a cell that is structured like an exercise solution but with a `# to_remove explanation` comment in the first line.

Tutorials should be hierarchically organized with meaningful section headers, and they should otherwise use consistent formatting and coding style. The ideal format is described in the [NMA Style Guide](./Neuromatch_Tutorial_Format.ipynb). The Editing process described below will ensure that all notebooks conform to this format, but the process will go more smoothly if it is adopted from the beginning of content creation.

Strive to minimize the amount of unnecessary code that students are exposed to. Colab notebooks will automatically "fold" cells that start with a comment beginning `# @title` or `# @markdown`. Most notebooks have a folded cell near the beginning with utility functions, such as those that download example data or generate plots for the exercises. Some of the tutorials discuss complex algorithms, and these may require larger bodies of code that do not need to be read in detail for conceptual understanding. While this code can also be hidden, it is better to do so in a dedicated cell positioned within the relevant narrative of the notebook so it can be easily accessed by more advanced students.

## Content Review

After Tutorials have been created, they are evaluated by several Reviewers. The review process focuses on the accuracy and pedagogical effectiveness of the content, including videos, prose, math, and code. Ideally, Reviewers will have domain-specific expertise relating to the days that they volunteer to review, although non-experts can provide helpful feedback about clarity and organization. Reviewing and Editing are partially overlapping, but Reviewers should focus on content, not style.

Content Review is organized externally to the GitHub repository using a Google Sheet that tracks the URLs for the latest version of each notebook, the associated Tutorial videos, and the identities of the various parties involved. There is also a slack channel (`#content-reviews`) where review assignments are coordinated.

Google Colab's commenting feature is the primary medium for the review. Notebooks should be shared with commenting enabled, but do *not* enable third-party editing, as this can lead to loss of work. Be aware that comments apply on a cell-wise basis; to comment about specific lines of code, enable line numbering (`Ctrl-M Ctrl-L`) and reference the number in the comment. There will also be a dedicated Slack channel (e.g. `#w1d3-modelfitting-review`) for each day that serves as a forum for discussions between Content Creators and Reviewers.

The Reviewers should have access to the one-page document outlining the learning objectives for the day, and they should provide feedback on how effectively the content satisfies those objectives. They should also consider whether the material in the tutorials requires background knowledge beyond the stated prerequisites for the course and the content on previous days. And they should evaluate the length and complexity of the tutorials, making suggestions where material can be cut or marked as "Bonus" when appropriate.

After the Reviewers have completed their work, the Content Creators should revise the notebooks to incorporate the feedback. But it is important to note that the review process is not adversarial — rather, the goal is to make the best possible content for the students.

## Content Editing

Content Editing begins once Content Creators have incorporated the review feedback and completed their work on the notebooks. Unlike Reviewers, Editors make direct changes to the notebooks, so they should create a copy of the Content Creator's final version (tracking ownership on the same Google Sheet) and work on that.

Ideally, Editors will have a close attention to detail, a deep knowledge of Python, and an intuition for the student mindset.

The overall objective of Content Editing is to ensure that the tutorials are standardized, clear, and accurate.

Standardization is important because it reduces the cognitive load that students would incur if each tutorial had a different structure, nomenclature, or style. Editors have several tools at their disposal to help enforce standardization. The first is the [Style Guide](./Neuromatch_Tutorial_Format.ipynb), an example notebook that defines the overall document structure and formatting requirements for individual components such as Videos, Exercises, and Interactive Demos. The second is a [finalization checklist](https://docs.google.com/forms/d/e/1FAIpQLSccR3zlUp9SoOwDoUU9lSIAZxvqTMk-smXjIX0RJjUq-oYcdQ/viewform) that enumerates specific guidelines, and the third is the [`lint_tutorials.py`](../ci/lint_tutorials.py) script, which runs as part of the Content Publishing workflow and provides feedback about code quality and style.

Editors should also evaluate and improve the clarity of the prose and code, aiming to reduce the chance of student confusion. This can include changes such as modifying exercise structure, moving boilerplate code into a hidden function, or cutting complicated digressions that do not contribute to the main learning objectives. When making substantive modifications, Editors should keep the original Content Creators in the loop, but Editors have final say over the changes.

Finally, Editors are responsible for ensuring that the notebooks will run correctly. This is partially enforced by the CI workflow that is discussed in the Content Publishing section, which will check that notebooks can run from top-to-bottom without encountering an error and that the given exercise code matches what is in the solutions. But Editors should also pay attention to pitfalls that are difficult to catch through automated analysis. For example, if the given code expects students to define `numpy` arrays, will it fail in a confusing way if students solve the exercise using Python lists? Are functions defined in the notebook using global variables when they should be using their local arguments? Do the Interactive Demos crash when the sliders are moved to extreme values?

## Content Publishing

The public-facing course content lives in the [`NeuromatchAcademy/course-content`](https://github.com/NeuromatchAcademy/course-content/) GitHub repository.

Notebooks are published when they are merged into the `master` branch in this repository. As part of the merge process, notebooks are evaluated by an automated continuous integration (CI) pipeline that runs in a [GitHub Action](https://github.com/features/actions). The CI pipeline is triggered automatically when opening or updating a Pull Request (PR) containing `.ipynb` files. Its objective is both to implement a quality control step -- aiding the content editing process -- and to automate the process of generating the version of the tutorials that students use.

The general workflow for initiating this process is to (1) create a staging branch using the GitHub UI (2) push notebooks from Colab to your branch using the "Save a copy in GitHub" feature in Colab, and (3) opening a PR from your staging branch to `master` on GitHub.

The CI checks will either pass or fail. A failure causes the pull request to be blocked. The reason for the failure can be discerned in the Actions log. The following checks are part of the pass/fail decision:

- If the notebook is in an executed state, its prompt numbers must sequentially index from 1 (i.e., you must use the "Restart and run all" in Colab option immediately before submitting the notebook).
- The CI workflow will (re)execute the notebook and fail if any unexpected errors are encountered. The only allowed exception class is `NotImplementedError`, which we use to indicate the presence of an exercise.
- The given code in the exercise cells will be compared to the relevant solution, and the check will fail if they do not match. This check ignores ellipses (`...`, which represent code that needs to be filled in), and code between block comments (matching lines of `#####` marks). It also ignores one level of indentation below a `with plt.xkcd():` line, which should appear in the solution but not in the exercise. Additionally, comments in the exercise body are compared against logical code lines in the solution, allowing code that would cause an error prior to exercise completion to be disabled by "commenting it out". Note that commenting out exercise code is no longer necessary, and it is better to write the exercise such that it raises a `NotImplementedError` before the dependent code is encountered.

The CI workflow will also evaluate the code style (checking conformance to [PEP8](https://www.python.org/dev/peps/pep-0008/) standards) and "lint" it to check for subtle problems that do not directly cause exceptions (such as variables that are defined but not used). These issues will be summarized in a comment on the pull request. PEP8 violations and code lint do not automatically block the PR, but they should be minimized subject to human judgement; this automated report can help aid this process.

If the checks pass, the CI workflow will automatically generate "student" versions of the notebooks. Student notebooks replace the solution cells with (1) a cartoon image of what a correct exercise would produce and (2) a link to the solution script on GitHub. These files are added to the PR manifest.

The workflow will also overwrite the original notebook with a "clean" version, which normalizes whitespace, removes cell outputs, and strips Colab metadata. This reduces noise in the GitHub diffs.

The workflow will also re-generate the [`README`](../tutorials/README.md) file, adding links to the Colab notebooks, YouTube playlists, and slide links. Links to the notebooks are generated automatically; links to videos and slides read from text files in the [`tutorials/`](../tutorials/) directory.

The comment with the code report will also add links to view the staging branch versions of the student and instructor notebooks on Colab; these should be manually checked to ensure that the conversion process worked as expected. Note that the solution links will point at the master branch, so solution images and scripts may not render properly in these previews. (Check them by looking in the PR's "Files changed" tab).

If the checks fail, or if the notebook needs further revisions, edit and then push a new version to the same branch it will restart the process.

Once the tests are passing and the notebooks are in a finalized state, another organizer with commit rights on the GitHub repository can approve the PR and merge. Delete the staging branch after merge to keep things tidy.
