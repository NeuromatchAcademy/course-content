def resample_with_replacement(x, y):
  """Resample data points with replacement from the dataset of `x` inputs and
  `y` measurements.

  Args:
    x (ndarray): An array of shape (samples,) that contains the input values.
    y (ndarray): An array of shape (samples,) that contains the corresponding
      measurement values to the inputs.

  Returns:
    ndarray, ndarray: The newly resampled `x` and `y` data points.
  """

  # Get array of indices for resampled points
  sample_idx = np.random.choice(len(x), size=len(x), replace=True)

  # Sample from x and y according to sample_idx
  x_ = x[sample_idx]
  y_ = y[sample_idx]

  return x_, y_


with plt.xkcd():
  fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))  
  ax1.scatter(x, y)
  ax1.set(title='Original', xlabel='x', ylabel='y')

  x_, y_ = resample_with_replacement(x, y)
  ax2.scatter(x_, y_, color='c')

  ax2.set(title='Resampled', xlabel='x', ylabel='y', 
          xlim=ax1.get_xlim(), ylim=ax1.get_ylim());
