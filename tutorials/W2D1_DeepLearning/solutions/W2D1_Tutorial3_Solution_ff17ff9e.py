
"""
The single unit activations of the 'pool' layer in the model have peaks at various
orientations, but they appear to have more peaks than the tuning curves from the
original data do. When we look at the population level responses we see that they
are not quite as smooth across orientations in the t-SNE embedding, which is likely
due to the fact that the 'pool' layer activations do not have localized responses
to orientations like the neural data.

The representations in the fully-connected 'fc' layer appear to be much more
clustered than the 'pool' layer. Stimuli which correspond to the same choice are
clustered together. It seems like the 'pool' layer is still working hard to
represent information about the orientation of the stimulus (much like the V1
population), whereas the 'fc' layer only cares about tilt category, representing
all the stimuli with the same category in a similar way regardless of their different
orientations.

From this analysis, it appears that the 'pool' layer is more similar to the neural
data at the population level.

""";