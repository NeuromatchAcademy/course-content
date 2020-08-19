# Neuromatch Academy Content Pipeline

This document summarizes the pipeline from content creation to publishing, focusing on practical details relating to the Tutorials.


## Content Creation


## Content Review

After Tutorials have been created, they are evaluated by several Reviewers. The review process focuses on the accuracy and pedagogical effectiveness of the content, including videos, prose, math, and code. Ideally, Reviewers will have domain-specific expertise relating to the days that they volunteer to review, although non-experts can provide helpful feedback about clarity and organization. Reviewing and Editing are partially overlapping, but Reviewers should focus on content, not style.

Content Review is organized externally to the GitHub repository using a Google Sheet that tracks the URLs for the latest version of each notebook, the associated Tutorial videos, and the identities of the various parties involved. There is also a slack channel (`#content-reviews`) where review assignments are coordinated.

Google Colab's commenting feature is the primary medium for the review. Notebooks should be shared with commenting enabled, but do *not* enable third-party editing, as this can lead to loss of work. Be aware that comments apply on a cell-wise basis; to comment about specific lines of code, enable line numbering (`Ctrl-M Ctrl-L`) and reference the number in the comment. There will also be a dedicated Slack channel (e.g. `#w1d3-modelfitting-review`) for each day that serves as a forum for discussions between Content Creators and Reviewers.

The Reviewers should have access to the one-page document outlining the learning objectives for the day, and they should provide feedback on how effectively the content satisfies those objectives. They should also consider whether the material in the tutorials requires background knowledge beyond the stated prerequisites for the course and the content on previous days. And they should evaluate the length and complexity of the tutorials, making suggestions where material can be cut or marked as "Bonus" when appropriate.

After the Reviewers have completed their work, the Content Creators should revise the notebooks to incorporate the feedback. But it is important to note that the review process is not adversarial — rather, the goal is to make the best possible content for the students.

## Content Editing

Content Editing begins once Content Creators have incorporated the review feedback and completed their work on the notebooks. Unlike Reviewers, Editors make direct changes to the notebooks, so they should create a copy of the Content Creator's final version (tracking ownership on the same Google Sheet) and work on that.

The overall objective of Content Editing is to ensure that the tutorials are standardized, clear, and accurate.

Standardization is important because it reduces the cognitive load that students would incur if each tutorial had a different structure, nomenclature, or style. Editors have several tools at their disposal to help enforce standardization. The first is the [Style Guide](./Neuromatch_Tutorial_Format.ipynb), an example notebook that defines the overall document structure and formatting requirements for individual components such as Videos, Exercises, and Interactive Demos. The second is a [finalization checklist](https://docs.google.com/forms/d/e/1FAIpQLSccR3zlUp9SoOwDoUU9lSIAZxvqTMk-smXjIX0RJjUq-oYcdQ/viewform) that enumerates specific guidelines, and the third is the [`lint_tutorials.py`](../ci/lint_tutorials.py) script, which runs as part of the Content Publishing workflow and provides feedback about code quality and style.

Editors should also evaluate and improve the clarity of the prose and code, aiming to reduce the chance of student confusion. This can include changes such as modifying exercise structure, moving boilerplate code into a hidden function, or cutting complicated digressions that do not contribute to the main learning objectives. When making substantive modifications, Editors should keep the original Content Creators in the loop, but Editors have final say over the changes.

Finally, Editors are responsible for ensuring that the notebooks will run correctly. This is partially enforced by the CI workflow that is discussed in the Content Publishing section, which will check that notebooks can run from top-to-bottom without encountering an error and that the given exercise code matches what is in the solutions. But Editors should also pay attention to pitfalls that are difficult to catch through automated analysis. For example, if the given code expects students to define `numpy` arrays, will it fail in a confusing way if students solve the exercise using Python lists? Are functions defined in the notebook using global variables when they should be using their local arguments? Do the Interactive Demos crash when the sliders are moved to extreme values?

## Content Publishing

Notebooks are published when they are merged into the `master` branch in the [`NeuromatchAcademy/course-content`](https://github.com/NeuromatchAcademy/course-content/) repository.