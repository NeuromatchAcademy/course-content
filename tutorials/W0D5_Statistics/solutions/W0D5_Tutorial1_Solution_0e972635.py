def generate_random_sample(num_points):
  """ Generate a random sample containing a desired number of points (num_points)
  in the range [0, 1] using a random number generator object.

  Args:
    num_points (int): number of points desired in random sample

  Returns:
    dataX, dataY (ndarray, ndarray): arrays of size (num_points,) containing x
    and y coordinates of sampled points

  """

  # Generate desired number of points uniformly between 0 and 1 (using uniform) for
  #     both x and y
  dataX = np.random.uniform(0, 1, size = (num_points,))
  dataY = np.random.uniform(0, 1, size = (num_points,))

  return dataX, dataY

# Set a seed
np.random.seed(0)

# Set number of points to draw
num_points = 10

# Draw random points
dataX, dataY = generate_random_sample(num_points)

# Visualize
with plt.xkcd():
  plot_random_sample(dataX, dataY, "Random sample of 10 points")