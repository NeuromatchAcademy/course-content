
#. 1) Information is ~ 1/variance, so the new information you have is roughly 1/(0.5^2 + 0.5^2)
#.    (compared to 1/0.5^2) for each original measurement.

#. 2) The estimate will be almost entirely dependent on the mu_{1}! There is almost no
#.    information from mu_{2}.

#. 3) Because the variances are the same, the amount of information you have about the center
#.    is lower (very low in fact), but the mean doesn't change!

#. 4) There are an infinite number of variances that will produce the same (relative) weighting.
#.    The only thing that matters is the relative means and relative variances!

#. 5) This is the same intuition, it's the relative weightings that matter, so you can only
#.    think about the result (in this case the variance of the second Gaussian) relative to
#.    the first.

#. 6) As the variances -> zero, the amount of information goes to infinity!