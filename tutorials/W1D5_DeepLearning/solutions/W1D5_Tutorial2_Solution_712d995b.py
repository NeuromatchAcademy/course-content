
# Stimulus parameters
in_channels = 1 # how many input channels in our images
h = 48 # height of images
w = 64 # width of images

# Convolution layer parameters
K = 7 # filter size
out_channels = 6 # how many convolutional channels to have in our layer
example_filters = filters(out_channels, K) # create filters to use

convout = np.zeros(0) # assign convolutional activations to convout

# Initialize conv layer and add weights from function filters
# you need to specify :
# * the number of input channels c_in
# * the number of output channels c_out
# * the filter size K
convLayer = ConvolutionalLayer(c_in=in_channels, c_out=out_channels, K=K, filters=example_filters)

# Create stimuli (H_in, W_in)
orientations = [-90, -45, 0, 45, 90]
stimuli = torch.zeros((len(orientations), in_channels, h, w), dtype=torch.float32)
for i,ori in enumerate(orientations):
  stimuli[i,0] = grating(ori)

convout = convLayer(stimuli)
convout = convout.detach() # detach gradients

with plt.xkcd():
  plot_example_activations(stimuli, convout, channels=np.arange(0, out_channels))