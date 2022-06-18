
"""
1. A complex cell combines two rectified Gabor filters of the same orientation but with
different phases. This is something a neural network can reproduce with a
RELU layer and combinations of convolutional channels. Additionally neural networks
employ a strategy called pooling layers, which combine units in a small region and
take the maximum value of their activations as the output. We will see these
layers in the next tutorial, where we will try to decode orientation directly from
images.

2. A cell that responds to multiple orientations would have to be a sum of multiple
convolutional channels. In the next bonus section, we will hook up this convolutional
layer to a fully connected layer.
""";