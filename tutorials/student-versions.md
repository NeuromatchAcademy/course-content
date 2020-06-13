# Student versions

Sample answers and other auxiliary cells are excluded automatically in the student versions of notebooks. For this to work, they are first identified with the tag `to_remove` in jupyter notebook (not colab!).

## Initial setup
First, activate viewing of cell tags by clicking `View`>`Cell Toolbar`>`Tags` from the notebook menu:

![View tags](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/static/view-tags.png)

Add a tag `to_remove` to each cell to be excluded in student versions:

![Adding tags](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/static/add-tag.png)

![Tag added](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/static/tag-added.png)

## Check student version
Open the notebook [`Generate student versions.ipynb`](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/utils/Generate%20student%20versions.ipynb), adjust the path variables `path_source` and `path_student` as needed, and execute the notebook.

## Code stubbing
In addition to the to_remove tag, student versions of code blocks should include code-stubbing where possible. Code-stubbing includes including the main structure of the desired code, such as variable names or plotting routines, and letting the students fill-in the meat of the line. For examples, see: https://colab.research.google.com/drive/1VqH6iQ42p2M9VNh1Eo5mJ6OoeuYOpGWE?usp=sharing