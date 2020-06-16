# Python standards for Neuromatch Academy (NMA)

Tutorials are Python code. Therefore, they need to follow the conventions of Python:

* Use [PEP8 style](https://www.python.org/dev/peps/pep-0008/)
* Use [Google commenting style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* Use colab spacing standard: 2 spaces

Notebook tutorials are a little different from normal Python code. Things to watch out for when writing and reviewing them:

* Run the notebook from top to bottom (`Runtime` > `Run all`). Notebooks cells often have dependencies on later cells - when they are run in order, they fail. Correct these, restart the kernel (`Runtime` > `Restart runtime`) and make sure to Run All after all changes to verify that dependencies run top to bottom.
* When a function needs to be filled in by the student, have it raise a `NotImplementedError` to indicate that it is part of an exercise. Add a message to the error so that this is explicit. Otherwise students may get confused about why the code won't run.
* Excercises should be accompanied by a solution cell (a completed version of the exercise) that the TAs will have access to. Solution cells should start with a comment that begins with `#@title Solution`. This is also the syntax for making a cell hide-able in Colab. This comment will signal that the cell should be removed from the student version of the tutorial.
* The notebook must still be able to execute from top-to-bottom with the incomplete stub functions (including after solutions are removed), so later cells should not be written in a way that depends on them being implemented. Where necessary, this can be accomplished by "commenting-out" calls to the function, but it is better to write self-contained exercises.
* Long notebooks can be hard to read. Using headings (Markdown `#`, `##`, `###`, etc.) can be used to create headings automatically. 
* Heavy notebooks can be slow to load in developing countries. Use developer tools (`Ctrl+Shift+I`) and go to `Network` > `Throttle`, and choose 3G to test things out.

Guidelines for file and folder names:
* Lower case for folder names
* Snake case for markdown and python files
* First letter in caps for jupyter notebooks (with spaces in the filename)

How to provide feedback:
* During the initial stage, we will use comments on colab notebooks, including code edits. Check to make sure your comments are saved by reloading the notebook.
* Once the colabs are posted on github, we'll use a different mechanism.
