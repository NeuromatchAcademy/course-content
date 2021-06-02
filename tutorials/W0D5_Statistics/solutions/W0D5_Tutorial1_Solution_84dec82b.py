def generate_random_walk(num_steps, step_size):
  """ Generate the points of a random walk within a 1 X 1 box.

  Args:
    num_steps (int): number of steps in the random walk
    step_size (float): how much each random step size is weighted

  Returns:
    x, y (ndarray, ndarray): the (x, y) locations reached at each time step of the walk

  """
  x = np.zeros(num_steps + 1)
  y = np.zeros(num_steps + 1)

  # Generate the uniformly random x, y steps for the walk
  random_x_steps, random_y_steps = generate_random_sample(num_steps)

  # Take steps according to the randomly sampled steps above
  for step in range(num_steps):

    # take a random step in x and y. We remove 0.5 to make it centered around 0
    x[step + 1] = x[step] + (random_x_steps[step] - 0.5)*step_size
    y[step + 1] = y[step] + (random_y_steps[step] - 0.5)*step_size

    # restrict to be within the 1 x 1 unit box
    x[step + 1]= min(max(x[step + 1], 0), 1)
    y[step + 1]= min(max(y[step + 1], 0), 1)

  return x, y

# Set a random seed
np.random.seed(2)

# Select parameters
num_steps = 100   # number of steps in random walk
step_size = 0.5   # size of each step

# Generate the random walk
x, y = generate_random_walk(num_steps, step_size)

# Visualize
with plt.xkcd():
  plot_random_walk(x, y, "Rat's location throughout random walk")