def compare(s, m):
  """ Compute a scatter plot

  Args:
    s (ndarray): astrocat's true position over time
    m (ndarray): astrocat's measured position over time according to the sensor

  """

  fig = plt.figure()
  ax = fig.add_subplot(111)
  sbounds = 1.1*max(max(np.abs(s)), max(np.abs(m)))
  ax.plot([-sbounds, sbounds], [-sbounds, sbounds], 'k')    # plot line of equality
  ax.set_xlabel('state')
  ax.set_ylabel('measurement')
  ax.set_aspect('equal')

  # Complete a scatter plot: true state versus measurements
  plt.scatter(s, m, marker='.', color='red', s=100)

with plt.xkcd():
  compare(s,m)