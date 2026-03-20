def my_CC(i, j):
  """
  Args:
    i, j  : two time series with the same length

  Returns:
    rij   : correlation coefficient
  """

  # Calculate the covariance of i and j
  cov = ((i - i.mean()) * (j - j.mean())).sum()

  # Calculate the variance of i
  var_i = ((i - i.mean()) * (i - i.mean())).sum()

  # Calculate the variance of j
  var_j = ((j - j.mean()) * (j - j.mean())).sum()

  # Calculate the correlation coefficient
  rij = cov / np.sqrt(var_i*var_j)

  return rij


with plt.xkcd():
  example_plot_myCC()