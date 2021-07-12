
# get weights of conv layer in convLayer
weights = convLayer.conv.weight.detach()
print(weights.shape) # can you identify what each of the dimensions are?

with plt.xkcd():
  plot_weights(weights, channels=np.arange(0, out_channels))