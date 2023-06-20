
"""
1. It seems like the model did not learn any weights for those hidden units.
Perhaps the random initialization of the W_out weights for those hidden units
was close to zero and that meant the gradients were small and they remained
unchanged during training. You could test this hypothesis by trying a
different random seed when initializing the network.

2. Neurons often have tuning preference to two gratings at 180 degrees apart
since these two gratings are the same other than the phase. This is likely why
there are two peaks.

3. Any stimulus orientations that don't activate any hidden units would create
an output vector of zero, and therefore those orientations would not be
distinguishable from each other.
""";