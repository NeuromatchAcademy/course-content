# Writing tutorials for Neuromatch Academy (NMA)

Thank you for agreeing to write tutorials for NMA! We're so glad you're here. We try to smooth out writing tutorials so you can concentrate on doing what you do best. 

## Environment

Tutorials are written in Python for the Google Colab environment.
Students will use Google Colab to run the tutorials to reduce setup requirements and provide enough compute power for resource-intensive tutorials (e.g. deep learning tutorials). 

We also have a pre-baked environment in *environment.yml* for students for whom Colab is unavailable in their country; it allows the tutorials to be run locally or via binderhub [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NeuromatchAcademy/course-content/master).

## Tutorial structure

There will be 4 tutorials per day. Each tutorial aims to be short and concise (15-20 minutes max.). We limit the amount of text and code present on-screen to the bare minimum required for understanding. We want students to focus on understanding the core concepts of the course, rather than focusing on data manipulation, plotting, etc. The rule of thumb is that students will need to write *3 lines of code per tutorial*.

## Organization & Communication

As a content creator, you create the python tutorials. You will need to coordinate with the day organizer so the tutorials meet the objectives of the day (see shared google drive: NMA > curriculum & content > [Content creator role.doc](https://docs.google.com/document/d/1EqDdBy3KPnK0B9ronMhPwa_WnJDjnKIK_fPs9jrDiUY))

Tutorials can take anywhere between 1-2 weeks to prepare, so start as early as possible! Here is how to proceed:

1. Read the 1-pagers for the tutorials you are in charge of: (shared google drive: NMA > curriculum & content > [One-pare Topic/ Lecture summaries/](https://drive.google.com/drive/folders/1mrXdVGgPqb-NVVLZj3E0FWETp9z-L9I-))
2. Meet with the day organizer to discuss the tutorial lecture content and what students will be asked to do in tutorials. At this stage, it will be essential to decide what you want each exercise of each tutorial to do.
3. You familiarize yourself with existing tutorial templates to understand the format of [NMA tutorials](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials)
4. Start with the coding of the tutorials (Only when you have finalised step 2! otherwise you'll have to redo a bunch of tutorials!)
   - This is important to minimise the amount of adjustment and doing/redoing required at a later stage. Iterating over step 2 in much detail is much more efficient than: creating code, then deleting whole exercises/tutorials and recoding new ones from scratch) if there is a mismatch.
5. Reiterate and refine step 4 for small adjustments.

## Structure of tutorials

Markdown headings (`#`, `##`, `###`, etc.) can be used to automatically create headings for tutorials, objectives, and exercises, respectively. Use `---` in markdown to separate different exercises/sections.

Example tutorials are available at [NMA github course-content/tutorials](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials).

For each tutorial:
1. Import all necessary libraries, plotting settings and plotting functions in the top code cell of the tutorial
   - write `# @title` at the top of the cell, and click `...`>`Form`>`Hide code` to hide the code cell (special colab trickery)
   - check the notebook [`Installing Python libraries.ipynb`](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/utils/Installing%20Python%20libraries.ipynb) on how to install additional libraries or your custom library
2. Describe the tutorial objectives using 2-3 sentences + bullet points
3. Start with a soft landing exercise to make students feel confident and relaxed.
4. Split core tutorial content into additional 2-4 exercises. Each exercise should have:
   - A short description of what we want the student to do in this exercise
   - All equations necessary to implement the computation req. in the exercise (incl. links to external papers/websites for further reading)
   - A detailed itemized list called `Suggestions` (bullet point list) of the itemized actions we want the students to perform to complete the exercise
   - Code skeleton, including all the plotting function req. for completing the exercise (incl. complete [Google-style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) docstrings)
   - When a function needs to be filled in by the student, have it raise a `NotImplementedError` to indicate that it is part of an exercise. Add a message to the error so that this is explicit. Otherwise students may get confused about why the code won't run.
   - (optional) Include hints in the code skeleton to highlight where the students should complete the code and what Python functions they could use to complete it (e.g.: '#Hint: use the function `np.exp()` to exponentiate' )
   - (optional) A sample output of what the correct output of the exercise should look like. To prevent students from focussing on reproducing exactly the plots/sample outputs rather than understanding the core concepts, we provide them with the plotting functions and use the XKCD style for the expected sample outputs.
5. Create solutions for each excercise in the tutorial. This will allow the technical team to check the tutorials, and it will facilitate training for the TAs before the summer school.
   - See example [here](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/demo/Exercise_With_Solution.ipynb)
   - The sample answers should be written in a separate cell. The first line of the cell should begin with `# @title Solution`. This comment will signal that the cell should be removed from the student version of the tutorial.
    - Make sure that later content doesn't depend on variables defined in these solution cells or on the output of the completed functions. Where necessary, you can "comment-out" such references and make it clear that the student should uncomment them once the exercise is complete. But it is better for the exercises to be self-contained.
6. Tutorial notebooks should be able to execute from top-to-bottom without error, including after the solution cells are removed. This allows us to automatically enforce a minimum standard of correctness.
7. Each tutorial stands on its own. Like a memorable story, set the context in the introduction, take the student forward through the exercises, and anchor learned points in the conclusion section.

Have a look at the reference tutorial to see what a tutorial looks like in the end: [Bayes Day tutorial 1](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/tutorials/Bayes/TA_solutions/BayesDay_Tutorial_1_solutions.ipynb)

There is also a collection of self-contained [Tutorial demos](./demos) illustrating invidual components.

## Reviewing

* Talk to your day organizer before submitting tutorials to the [NMA course-content github repo](https://github.com/NeuromatchAcademy/course-content/)
* Once approved, submit tutorials to [the NMA github](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials) so that the technical team can test the tutorials and check for standardization across all NMA tutorials.
* This is [the guide we use to review tutorials](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/reviewing-tutorials.md). We try to enforce a consistent style across notebooks so it's easy for students to jump in. We try to minimize the burden on the tutorial authors. You're the stars! 
* [We use a branch-pull-request workflow for content](https://guides.github.com/introduction/flow/). You stage everything on your branch - you can mess up this branch as much as you want, it's 100% yours. Then when you're ready, you create a pull request to ask to merge your branch with the master branch (the stuff everybody sees). Add Marco and Patrick as reviewers. They'll review your notebooks, make comments, and after a couple of iterations, they will merge onto master.

## Colab & Github workflow
When you have final version of Colab, we'll pull into Github following this [workflow](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/reviewing-tutorials.md#workflow-for-incorporation-into-the-github-repostory)

