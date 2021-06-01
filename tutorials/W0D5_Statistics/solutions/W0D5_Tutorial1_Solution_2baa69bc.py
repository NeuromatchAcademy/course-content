def generate_random_sample(num_points):
  """ Generate a random sample containing a desired number of points (num_points)
  in the range [0, 1] using a random number generator object.

  Args:
    num_points (int): number of points desired in random sample

  Returns:
    dataX, dataY (ndarray, ndarray): arrays of shape (num_points,) containing x
    and y coordinates of sampled points

  """
  random_num_generator = default_rng(0) # initialize a random number generator
  # Use random method to generate desired number of values/points between 0 and 1
  dataX = random_num_generator.random(num_points)
  dataY = random_num_generator.random(num_points)

  return dataX, dataY

# Set the num_points parameter equal to the desired number of points
num_points = 10

# Uncomment once you've filled in code above to plot the x and y coordinates as points
dataX, dataY = generate_random_sample(num_points)
with plt.xkcd():
  plot_random_sample(dataX, dataY, "Random sample of 10 points")