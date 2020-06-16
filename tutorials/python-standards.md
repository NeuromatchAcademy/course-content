# Python standards for Neuromatch Academy (NMA)

Tutorials are Python code. Therefore, they need to follow the conventions of Python:

* Use [PEP8 style](https://www.python.org/dev/peps/pep-0008/)
* Use [Google commenting style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* Use colab spacing standard: 2 spaces

Notebook tutorials are a little different from normal Python code. Things to watch out for when writing and reviewing them:

* Notebooks that are iteratively developed often end up with code that depends on later cells, meaning that they fail when run in order on a fresh kernel. To check for this issue, periodically restart the kernel and execute the notebook (`Runtime` > `Restart and run all`). Make sure to do this before passing the notebook off for review.
* The notebook must still be able to execute from top-to-bottom with incomplete exercises (including after solutions are removed), so incomplete exercises should not cause errors, and later cells should not depend on their implemention. Where necessary, this can be accomplished by "commenting-out" calls to the function, but it is better to write self-contained exercises.
* Long notebooks can be hard to read. Using headings (Markdown `#`, `##`, `###`, etc.) can be used to create headings automatically. 
* Heavy notebooks can be slow to load in developing countries. Use developer tools (`Ctrl+Shift+I`) and go to `Network` > `Throttle`, and choose 3G to test things out.

Guidelines for file and folder names:
* Lower case for folder names
* Snake case for markdown and python files
* First letter in caps for jupyter notebooks (with spaces in the filename)

How to provide feedback:
* During the initial stage, we will use comments on colab notebooks, including code edits. Check to make sure your comments are saved by reloading the notebook. Note that comments are linked to each cell, not to individual lines. You can enable line numbers and then mention them in your comment to give more specific feedback.
* Once the colabs are posted on github, we'll use a different mechanism.
