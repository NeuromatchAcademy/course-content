
# Convolution layer parameters
K = 7 # filter size
conv_channels = 6 # how many convolutional channels to have in our layer

convout = np.zeros(0) # assign convolutional activations to convout

### Initialize conv layer with weights from function filters
# you need to specify :
# * the number of input channels c_in
# * the number of output channels c_out
# * the filter size K
convLayer = ConvolutionalLayer(c_in=1, c_out=conv_channels, K=K,
                               filters=filters(K))

### Create stimuli (H_in, W_in)
stimuli = torch.zeros((len(orientations), 48, 64), dtype=torch.float32)
orientations = [-90, -45, 0, 45, 90]
for i,ori in enumerate(orientations):
  stimuli[i] = grating(ori)

convout = convLayer(stimuli)
convout = convout.detach() # detach gradients

with plt.xkcd():
  plot_example_activations(stimuli, convout, channels=np.arange(0, conv_channels))