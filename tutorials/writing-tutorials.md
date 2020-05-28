# Writing tutorials for Neurmatch Academy (NMA)

**Abreviations:**
    * CC: Content Creators
    * TL: Teaching Lecturer
    * TA: Teaching Assistants

**Requirements**
Tutorials need to be writen in python using jupyter notebooks, so that they can then be easily integrated into Google Colab.
Students will use Google Colab to run the tutorials (unless Colab is unavailable in their country) to reduce setup req./library dependencies issues and provide enough compute power for resource intensive tutorials (e.g. DL tutorials).

**Description**
There will be 4 tutorials per day. Each tutorial aims to be short and concise (15-20 minutes max.), it is therefore essential to limit the amount of text and code present on-screen to the bare minimum required for understanding. We want students to focus on understanding the core concepts of the course, rather than focusing on data manipulation, plotting, etc. 

**Important**
The role of the CC is to create the python tutorials with guidance from the TL (see shared google drive: NMA > curriculum & content > Content creator role.doc) (https://docs.google.com/document/d/1EqDdBy3KPnK0B9ronMhPwa_WnJDjnKIK_fPs9jrDiUY)

Tutorials can take anywhere between 1-2 weeks to prepare, so start as early as possible! Here is how to proceed:

1 - CC checks 1-pagers for the tutorials they are in charge of: (shared google drive: NMA > curriculum & content > One-pare Topic/ Lecture summaries/)
2 - CC meet with TL to discuss the tutorial lecture content and what students will be asked to do in tutorials. At this stage it would be essential to finalise exactly with the TL what you want each exercise of each tutorial to do.
3 - CC familiarizes themselves with existing tutorial templates to understand the format of [NMA tutorials](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials)
4 - Start with the coding of the tutorials (Only when you have finalised step 2 ! This is essential)
        - This is important to minimise the amount of adjustment and doing/redoing required at a later stage. Iterating over step 2 in much detail is much more efficient than: creating code, then deleting whole exercises/tutorials and recoding new ones from scratch) if there is a mismatch.
5 - Reiterate and refine 4 for small adjustments.

### Structure of tutorials

Using markdown headings (#, ##, ###, etc.) can be used to automatically create headings for tutorials, objectives, and exercises, respectively. Use `---` markdown to separate different exercises/sections.

Example tutorials are available at [NMA github course-content/tutorials](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials).

For each tutorial:
0 - Import all necessary libraries, plotting settings and plotting functions in the top code cell of the tutorial
        - include `# @title` at the top of the cell, and click `...`>`Form`>`Hide code` to hide the code cell
1 - Describe the tutorial objectives using 2-3 sentences + bullet points
2 - Split the tutorial into 2-4 exercises:
    Each exercise should have:
        - A short description of what we want the student to do in this exercise
        - All equations necessary to implement the computation req. in the exercise (incl. links to external papers/websites for further reading)
        - A detailed itemized list called `Suggestions` (bullet point list) of the itemized actions we want the students to perform to complete the exercise
        - Code skeleton including all the plotting function req. for completing the exercise (incl. complete [PEP8 compliant](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) docstrings)
        - (optional) Include hints in the code skeletton to highlight where the students should complete the code and what python functions they could use to complete it (e.g.: '#Hint: use the function `np.exp()` to exponentiate' )
        - (optional) A sample output of what the correct output of the exercise should look like. In order to prevent students from focussing on reproducing exactly the plots/expected-outputs rather than understanding the core concepts, we provide them with the plotting functions, and use XKCD style for the expected sample outputs.
3 - Create sample answers for each tutorial, and so that the technical team can check the tutorials, and to facillitate training for the TAs prior to the summer school.

* Tutorials need to be approved by the TL before submitting them to the [NMA github tutorials](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials)
* Once approved by the TL, submit all tutorials to [NMA github tutorials](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials) by June XXth so that the technical team can test the tutorials and check for standardization across all NMA tutorials.