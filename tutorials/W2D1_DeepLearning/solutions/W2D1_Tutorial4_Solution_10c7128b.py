
"""
It appears that the errors are larger at 0 and 360 degrees. The errors are biased
in the positive direction at 0 degrees and in the negative direction at 360 degrees.
This is because the 0 degree stimulus and the 360 degree stimulus are in fact the
same because orientation is a circular variable. The network therefore has trouble
determining whether the stimulus is 0 or 360 degrees.

We can modify the deep network to avoid this problem in a few different ways.
One approach would be to predict a sine and a cosine of the angle and then taking
the predicted angle as the angle of the complex number $sin(\theta) + i cos(\theta)$.

An alternative approach is to bin the stimulus responses and predict the bin of the stimulus.
This turns the problem into a classification problem rather than a regression problem,
and in this case you will need to use a new loss function (see below).
""";