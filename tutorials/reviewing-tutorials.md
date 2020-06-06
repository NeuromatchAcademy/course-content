# Reviewing tutorials

Tutorials are Python code. Therefore, they need to follow the conventions of Python:

* Use [PEP8 style](https://www.python.org/dev/peps/pep-0008/)
* Use [Google commenting style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* Use colab spacing standard: 2 spaces

Reviewing colab/jupyter notebook tutorials is also a little different than normal Python code review. Things to watch out for:

* Run the notebook from top to bottom (`Runtime` > `Run all`). Very frequently, notebooks cells have dependencies on later cells - when they are run in order, they fail. Correct these and make sure to Run All after all changes to verify that dependencies run top to bottom.
* When a function needs to be filled in by the student, raise a `NotImplementedError` to indicate to the student they have to implement the function.
* Long notebooks can be hard to read. Using headings (Markdown `#`, `##`, `###`, etc.) can be used to automatically create headings. 
* Heavy notebooks can be slow to load in developing countries. Use developer tools (`Ctrl+Shift+I`) and go to `Network` > `Throttle`, and choose 3G to test things out.

Guidelines for file and folder names:
* Lower case for folder names
* Snake case for markdown and python files
* First letter in caps for ipython notebooks (with spaces in the filename)
