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

Most of the notebook preparation is coordinated on Google Drive by making copies and sharing/tracking links. But after review and waxing, notebooks should be incorporated into the [NMA Github Repository](https://github.com/NeuromatchAcademy/course-content). Github is the canonical source for the version of the tutorials that students will actually see, so it is important to get this process right.

The process involves both automated and manual quality control. Here is a guide to the basic steps you should follow. If you are new to the process, it is best to communicate on Slack about what you are doing (`@Michael Waskom` is the best reference).

While it's helpful to have multiple people handle the work of merging the tutorials, if you're not familiar/confident with Github, feel free to hand the job off (just coordinate on Slack).

1. Create a new feature branch off of master in the `NeuromatchAcademy/course-content` repository.
  - In the github UI, this can be accomplished from the `Branch` dropdown menu.
  - Include `WxDy` in the name. (Replace `x` and `y` to match your day code).
  - It is best to branch off master at the time you're ready to push your tutorials, so that the CI will run the latest version of the notebook processing workflow.
  - For the CI workflow to run properly, the PR must be made from a feature branch on the main repository, not a fork.
2. Notebooks are required to have a sequential execution history on a fresh kernel. This will be automatically checked as part of CI. Before you push, execute the entire notebook (`Runtime -> Restart and run all` in the Colab menu) and make sure it completes without any errors. Then save the notebook.
3. Push the notebook from Colab to Github:
  - `File -> Save a copy in Github` in the Colab menu
  - Select the course repository: (`NeuromatchAcademy/course-content`)
  - Select your feature branch: (e.g. `WxDy`)
  - Write out the complete file path, using the standardized template:
    - `tutorials/W{x}D{y}_{Topic}/WxDy_Tutorial{i}.ipynb`
    - Replace `{x}`, `{y}`, `{Topic}` and `{i}`
    - See the [tutorials directory](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials) for a list of names to use for `{Topic}`
    - An example filename will look like this: `tutorials/W1D5_DimensionalityReduction/W1D5_Tutorial3.ipynb`
    - Don't copy the filename from a rich text display (e.g. the Github UI), because mixing unicode and ASCII can produce duplicate files. Copying the path from the URL bar works.
  - Make sure that "Include a link to Colaboratory" remains checked.
  - **Important**: Double-check that the file path is correct before pushing. Fixing incorrect names is a substantial pain, because multiple derivative files will be created using the name you push.
4. Repeat Step 3 with the other tutorials for that day.
5. On Github, open a Pull Request from your feature branch onto `master`.
6. Opening the PR will trigger the notebook CI workflow. This will (1) run QC checks on the notebooks and (2) create student versions and derivative static files (solution images and scripts).
  - If the checks fail, click through to the Github Action log and try to figure out what's wrong (or ask for help on Slack).
  - Fix the problem on Colab, then repeat step 3 for that notebook. This will trigger a re-run of the CI workflow.
7. All PRs must be approved by someone else with commit rights to the repository before they can be merged. You can select reviewers in the upper-right-hand corner of the Pull Request UI. `@mwaskom`, `@patrickmineault`, or your week chief are good reviewers.
8. Do visual checks of the processed and derivative files to make sure the student versions look correct.
  - The embedded "Open in Colab badge" is modified as part of the CI workflow to point towards the master branch, so you will need to manually change the URL to point towards the feature branch if you want to open on Colab.
  - The links to the solution images and scripts will also reference `master` so those won't be populated yet.
9. If everything looks good, the reviewer should approve the PR and then do a squash-merge onto master.
10. Delete the feature branch after the merge is complete.