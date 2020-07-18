def my_CC(x, y):
  """
  Args:
    x, y  : two time series with the same length

  Returns:
    rxy   : correlation coefficient
  """
  # Calculate the covariance of x and y
  xy = ((x - x.mean()) * (y - y.mean())).sum()
  # Calculate the covariance of x
  xx = ((x - x.mean()) * (x - x.mean())).sum()
  # Calculate the covariance of y
  yy = ((y - y.mean())*(y - y.mean())).sum()
  # Calculate the correlation coefficient
  rxy = xy / np.sqrt(xx * yy)

  return rxy


with plt.xkcd():
  example_plot_myCC()