# The zen of reviewing tutorials for Neuromatch Academy (NMA)

Thank you for agreeing to review tutorials for NMA!

How can tutorial content reviewers contribute to material authored by domain experts? Reviewers that are domain experts help double-check scientific content. Non-experts contribute to alignment and consistency, which applies to all content in NMA.

## Contribution scope

Content creators design tutorials for a particular day. Reviewers see materials across days and assist in polishing them for publication. Creators and reviewers work together in iterative loops to improve consistency with the other days.

Content reviewers follow 3 to 5 days of tutorials, and at least two reviewers see each tutorial.

## Reference documents

These are the main areas for alignment and consistency: 

* Learning objectives and tutorial content from [One-page Topic/Lecture summaries](https://drive.google.com/drive/folders/1mrXdVGgPqb-NVVLZj3E0FWETp9z-L9I-)
* Guidelines for [Writing tutorials for Neuromatch Academy (NMA)](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/writing-tutorials.md)
* Python guidelines and best practices from [Python-standards](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/python-standards.md)
* Consistent math notation and formatting defined in [Standardized nomenclature, math, fonts](https://docs.google.com/document/d/1Z3Bc0oQA4a-y3xJU2mtIDMAOen1SO8AmUjkc3_xFOPM/edit)
* Self-consistency: Each slide deck and notebook stands on its own, except for dependencies from other days
* The Github repository has several demos of [example tutorial components](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials/demo)

## Content review workflow

1. Content creators post links to new material on Slack channel `#content-reviews` with **comment permissions**.
2. Content review team adds these links to the sheet [Content Review Sign-Up](https://docs.google.com/spreadsheets/d/1LtLEk0H7gkR34kXJVC3hICUsLwfabbSjTPSlterB-xg/edit)
3. Reviewers comment directly on docs or colab notebooks or reply in Slack threads
4. Materials migrate to Github after reaching initial draft status, and reviews continue there

See [Content Review Sign-Up](https://docs.google.com/spreadsheets/d/1LtLEk0H7gkR34kXJVC3hICUsLwfabbSjTPSlterB-xg/edit) for additional instructions

## Workflow for incorporation into the Github repostory

After initial review, notebooks should be incorporated into the [NMA Github Repository](https://github.com/NeuromatchAcademy/course-content). This involves both manual and automated quality control.

1. Once initial review is complete, Content Creators should *hand off* the tutorial to their Review Day Chief. At this time, the tutorial content should be finished, but the notebook may be missing links to the finalized lecture videos. The hand-off is accomplished by having the Review Day Chief make a copy of the tutorial that they now own.
2. The Review Day Chief should run their copy of the notebook from top-to-bottom on a fresh kernel (`Runtime -> Restart and run all`) and check that it runs without error.
3. The Review Day Chief should upload their copy to Github:
  - `File -> Save a copy in Github`
  - Repository: `NeuromatchAcademy/course-content`
  - Branch: `WxDy`
    - Replace `x` and `y` with the appropriate week and day (e.g. `W2D3`)
  - File path: `tutorials/WxDy-$Topic/WxDy-Tutorial$i.ipynb`
    - Replace `x`, `y`, `$Topic` and `$i`
    - See the [tutorials directory](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials) for a list names to use for `$Topic`
    - E.g. `tutorials/W1D5-DimensionalityReduction/W1D5-Tutorial3.ipynb`
    - **Important**: Double-check that the file name is correct; fixing it will be a pain
4. The Review Day Chief should open a Pull Request (PR) from the `WxDy` branch to `master`
  - To create a PR, click on 'course-content' at the top of the page to return to directory, then click on PR symbol.  
  - On the right-hand side, click on the gear next to 'Reviewers' to select Github Reviewers (@mwaskom, @mpbrigham, @patrickmineault) to approve the PR.
  - It is best to do this after all of the notebooks for a given day have been uploaded
  - This will trigger an automated quality control workflow
  - If the QC checks pass, student versions (solutions removed) will be created
5. If the tutorials are missing final pieces (e.g. Youtube links), mark the PR as a "draft"
6. If the QC workflow fails, revise the notebook on Colab then repeat Step 3.
7. Once the final pieces (e.g. video links) are in place, repeat Step 2 and Step 3, then remove the "draft" status from the PR on github and @ the reviewers for the merge.
