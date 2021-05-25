def dF(x, a, theta):
  """
  Population activation function.

  Args:
    x     : the population input
    a     : the gain of the function
    theta : the threshold of the function

  Returns:
    dFdx  : the population activation response F(x) for input x
  """

  # Calculate the population activation
  dFdx = a * np.exp(-a * (x - theta)) * (1 + np.exp(-a * (x - theta)))**-2

  return dFdx


pars = default_pars_single()  # get default parameters
x = np.arange(0, 10, .1)      # set the range of input

df = dF(x, pars['a'], pars['theta'])

with plt.xkcd():
  plot_dFdt(x, df)