def sigmoid(z):
  """Return the logistic transform of z."""

  sigmoid = 1 / (1 + np.exp(-z))

  return sigmoid


# Visualize
with plt.xkcd():
  plot_function(sigmoid, "\sigma", "z", (-10, 10))