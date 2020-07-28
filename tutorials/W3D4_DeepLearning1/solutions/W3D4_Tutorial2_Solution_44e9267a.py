
# Convolution layer parameters
K = 9 # filter size, now that we've binned let's make this smaller than for the numpy conv
conv_channels = 8 # how many convolutional channels to have in our layer

convout = np.zeros(0) # assign convolutional activations to convout

# Initialize conv layer
convLayer = ConvolutionalLayer(c_in=1, c_out=conv_channels, K=K)

# Call conv layer on stimulus
convout = convLayer(stim_binary)
convout = convout.detach() # detach gradients
print(convout.shape) # can you identify what each of these dimensions are?

# Plot results
with plt.xkcd():
  plot_example_activations(convout)