
"""
1. As seen above, the stimulus is zero everywhere except for in one bin, and so
the convolutional activations are constant everywhere except for around the stimulus.
The constant offset is from a bias term that each convolutional channel has.
2. The width of non-constant activations is the kernel size K.
3. The convLayer has K*C_out weights.
4. A fully connected layer would have (B^2)*C_out weights.
""";