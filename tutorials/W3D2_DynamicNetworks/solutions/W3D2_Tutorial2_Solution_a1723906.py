
# Define the inverse of F
def F_inv(x,a,theta): 
  """
  Args:
    x         : the population input
    a         : the gain of the function
    theta     : the threshold of the function
  
  Returns:
    F_inverse : value of the inverse function
  """
    
  F_inverse = -1/a * np.log((x+(1+np.exp(a*theta))**-1)**-1 -1) + theta

  return F_inverse


# get the nullcline for E, solve Equation. (4) along the E-grid
def get_E_nullcline(pars, E_grid):
  """
  Solve for I along the E_grid from dE/dt = 0.
  
  Args:
    pars   : Parameter dictionary
    E_grid : a single value or an array
  
  Returns:
    I      : values of inhibitory population along the nullcline on the E-grid
  """
    
  a_E, theta_E = pars['a_E'], pars['theta_E']
  wEE, wEI = pars['wEE'], pars['wEI'] 
  I_ext_E = pars['I_ext_E']
  
  I = 1./wEI * (wEE*E_grid - F_inv(E_grid, a_E, theta_E) + I_ext_E)

  return I

# get the nullcline for I, solve Equation. (5) along the I-grid
def get_I_nullcline(pars, I_grid):
  """
  Solve for E along the I_grid from dI/dt = 0.
  
  Args:
    pars   : Parameter dictionary
    I_grid : a single value or an array
  
  Returns:
    E      : values of the excitatory population along the nullcline on the I-grid
  """
    
  a_I, theta_I = pars['a_I'], pars['theta_I']
  wIE, wII = pars['wIE'], pars['wII']
  I_ext_I =  pars['I_ext_I']

  E = 1./wIE * (wII*I_grid + F_inv(I_grid, a_I, theta_I) - I_ext_I)
  
  return E

pars = default_pars() # get parameters
with plt.xkcd():
    fig3 = plt.figure(figsize=(8, 5.5))
    my_plot_nullcline(pars)