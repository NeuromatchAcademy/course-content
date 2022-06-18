
"""
1. There are H * W activations in each channel because the stride in the
convolutional layer is set to 1, and the padding is set to K//2.

2. The convLayer has K * K * C_out weights and C_out bias terms.

3. A fully connected layer would have (H * W) * C_out weights and C_out bias terms.

4. A center-surround filter will respond to a change in luminance (black-to-white
or white-to-black) regardless of orientation.

5. A gabor filter of different orientations will respond this way. See the
exercise below for more explanation.
""";