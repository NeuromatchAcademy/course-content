
"""
1. There are 6 convolutional channels and 12 x 16 positions because the stride
of the convolution is 1. Therefore, there are 6 * 12 * 16 = 1152 units in the
convolutional layer.

2. The fully connected linear layer will have 1152 * n_neurons weights. It will
also have n_neurons additive bias terms.
""";