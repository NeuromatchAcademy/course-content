def my_CC(x, y):
  """
  Args:
    x, y  : two time serieses with same length

  Returns:
    rxy   : correlation coefficient
  """
  xy = ((x-x.mean())*(y-y.mean())).sum()
  xx = ((x-x.mean())*(x-x.mean())).sum()
  yy = ((y-y.mean())*(y-y.mean())).sum()

  rxy = xy/np.sqrt(xx*yy)

  return rxy


example_plot_myCC()