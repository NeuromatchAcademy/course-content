def dF(x,a,theta): 
  """
  Population activation function.

  Args:
    x     : the population input
    a     : the gain of the function
    theta : the threshold of the function
  
  Returns:
    dFdx  : the population activation response F(x) for input x
  """

  dFdx = a*np.exp(-a*(x-theta))*(1+np.exp(-a*(x-theta)))**-2

  return dFdx

# get default parameters
pars = default_parsE()

# set the range of input
x = np.arange(0,10,.1)

# plot figure
with plt.xkcd():
  plot_dFdt(x,dF(x,pars['a_E'],pars['theta_E']))

