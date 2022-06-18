
# Plot the weights of the first principal component
with plt.xkcd():
  plot_MNIST_weights(evectors[:, 0])