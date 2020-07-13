def F_inv(x, a, theta):
  """
  Args:
    x         : the population input
    a         : the gain of the function
    theta     : the threshold of the function

  Returns:
    F_inverse : value of the inverse function
  """

  # Calculate Finverse (ln(x) can be calculated as np.log(x))
  F_inverse = -1/a * np.log((x + (1 + np.exp(a * theta))**-1)**-1 - 1) + theta

  return F_inverse


def get_E_nullcline(pars, rE):
  """
  Solve for rI along the rE from drE/dt = 0.

  Args:
    pars  : Parameter dictionary
    rE    : a single value or an array

  Returns:
    rI    : values of inhibitory population along the nullcline on the rE
  """

  a_E, theta_E = pars['a_E'], pars['theta_E']
  wEE, wEI = pars['wEE'], pars['wEI']
  I_ext_E = pars['I_ext_E']

  # calculate rI for E nullclines on rI
  rI = 1 / wEI * (wEE * rE - F_inv(rE, a_E, theta_E) + I_ext_E)

  return rI


def get_I_nullcline(pars, rI):
  """
  Solve for E along the I_grid from dI/dt = 0.

  Args:
    pars  : Parameter dictionary
    rI    : a single value or an array

  Returns:
    rE    : values of the excitatory population along the nullcline on the rI
  """

  a_I, theta_I = pars['a_I'], pars['theta_I']
  wIE, wII = pars['wIE'], pars['wII']
  I_ext_I = pars['I_ext_I']

  # calculate rE for I nullclines on rI
  rE = 1 / wIE * (wII * rI + F_inv(rI, a_I, theta_I) - I_ext_I)

  return rE


pars = default_pars()  # get parameters

# Uncomment the below lines after completing the functions
Exc_null_rE = np.linspace(-0.01, 0.96, 100)
Exc_null_rI = get_E_nullcline(pars, Exc_null_rE)
Inh_null_rI = np.linspace(-.01, 0.8, 100)
Inh_null_rE = get_I_nullcline(pars, Inh_null_rI)

with plt.xkcd():
  plot_nullclines(Exc_null_rE, Exc_null_rI, Inh_null_rE, Inh_null_rI)