
"""
We see many sharp peaks in the training set, but these peaks are not always present
in the test set, suggesting that they are due to noise. Therefore, ignoring this
noise, we might have expected the neural responses to be a sum of only a few
different filters and only at a few different positions. This would mean that we
would expect the `out_layer` weight matrix to be sparse, not dense like the one
shown here.
""";