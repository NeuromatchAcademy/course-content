

def F(x, a, theta):
  """
  Population activation function.

  Args:
    x     : the population input
    a     : the gain of the function
    theta : the threshold of the function

  Returns:
    the population activation response F(x) for input x
  """

  # add the expression of f = F(x)
  f = (1 + np.exp(-a * (x - theta)))**-1 - (1 + np.exp(a * theta))**-1

  return f


pars = default_pars_single()   # get default parameters
x = np.arange(0, 10, .1)       # set the range of input

# Uncomment below to test your function
f = F(x, pars['a'], pars['theta'])

with plt.xkcd():
  plot_fI(x, f)