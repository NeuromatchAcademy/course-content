
def F(x, a, theta):
  """
  Population activation function.

  Args:
    x (float): the population input
    a (float): the gain of the function
    theta (float): the threshold of the function

  Returns:
    float: the population activation response F(x) for input x
  """

  # Define the sigmoidal transfer function f = F(x)
  f = (1 + np.exp(-a * (x - theta)))**-1 - (1 + np.exp(a * theta))**-1

  return f


# Set parameters
pars = default_pars_single()  # get default parameters
x = np.arange(0, 10, .1)      # set the range of input

# Compute transfer function
f = F(x, pars['a'], pars['theta'])

# Visualize
with plt.xkcd():
  plot_fI(x, f)