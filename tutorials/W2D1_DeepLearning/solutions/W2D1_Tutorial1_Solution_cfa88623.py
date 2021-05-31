
"""
1. It seems like the model did not learn any weights for those hidden units,
perhaps the problem is simple enough that the weights were not needed, or the
random initialization of the W_out weights for those hidden units close to zero
kept them from changing. You could test the second hypothesis by looking at the
weights at initialization
2. Neurons often have tuning preference to two gratings at 180 degrees apart
since these two gratings are the same other than the phase. This is likely why
there are two peaks.
3. One could look at the activity of the hidden units across various stimuli,
making tuning curves for the hidden units.
""";