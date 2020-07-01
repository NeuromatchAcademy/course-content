
def simulate_wc(pars):
    
  """
  Simulate the Wilson-Cowan equations 
  
  Args:
    pars : Parameter dictionary
  
  Returns:
    E    : Activity of excitatory population (array)
    I    : Activity of inhibitory population (array)
  """
  
  # Set parameters
  tau_E, a_E, theta_E = pars['tau_E'], pars['a_E'], pars['theta_E']
  tau_I, a_I, theta_I = pars['tau_I'], pars['a_I'], pars['theta_I']
  wEE, wEI = pars['wEE'], pars['wEI'] 
  wIE, wII = pars['wIE'], pars['wII']
  I_ext_E, I_ext_I = pars['I_ext_E'], pars['I_ext_I'] 
  E_init, I_init = pars['E_init'], pars['I_init']       
  dt, range_t = pars['dt'], pars['range_t'] 
  Lt = range_t.size 
      
  # Initialize activity
  E = np.zeros(Lt)
  I = np.zeros(Lt)
  E[0] = E_init
  I[0] = I_init
  I_ext_E = I_ext_E * np.ones(Lt)
  I_ext_I = I_ext_I * np.ones(Lt)

  # simulate the Wilson-Cowan equations 
  for k in range(Lt-1):
    dE = dt/tau_E * (-E[k] + F(wEE*E[k]-wEI*I[k]+I_ext_E[k],a_E,theta_E))
    dI = dt/tau_I * (-I[k] + F(wIE*E[k]-wII*I[k]+I_ext_I[k],a_I,theta_I))
    E[k+1] = E[k] + dE
    I[k+1] = I[k] + dI
  
  return E,I

pars = default_pars()
pars['E_init'], pars['I_init'] = 0.32, 0.15
E1,I1 = simulate_wc(pars)
pars['E_init'], pars['I_init'] = 0.33, 0.15
E2,I2 = simulate_wc(pars)

with plt.xkcd():
  fig2 = plt.figure(figsize=(8, 5.5))
  my_test_plot(pars['range_t'], E1, I1, E2, I2)
  plt.show()