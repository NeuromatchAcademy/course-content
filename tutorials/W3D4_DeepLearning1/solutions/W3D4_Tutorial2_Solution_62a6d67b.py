
K = 9 # now that we've binned let's make this smaller
conv_channels = 8 # how many convolutional channels to have in our layer

convLayer = ConvolutionalLayer(c_in=1, c_out=conv_channels, K=K)
convout = convLayer(stim_binary)
convout = convout.detach() # detach gradients

print(convout.shape) # can you identify what each of these dimensions are?
with plt.xkcd():
  plot_example_activations(convout)