def simulate_wc(pars):
  """
  Simulate the Wilson-Cowan equations

  Args:
    pars : Parameter dictionary

  Returns:
    rE   : Activity of excitatory population (array)
    rI   : Activity of inhibitory population (array)
  """

  # Set parameters
  tau_E, a_E, theta_E = pars['tau_E'], pars['a_E'], pars['theta_E']
  tau_I, a_I, theta_I = pars['tau_I'], pars['a_I'], pars['theta_I']
  wEE, wEI = pars['wEE'], pars['wEI']
  wIE, wII = pars['wIE'], pars['wII']
  I_ext_E, I_ext_I = pars['I_ext_E'], pars['I_ext_I']
  rE_init, rI_init = pars['rE_init'], pars['rI_init']
  dt, range_t = pars['dt'], pars['range_t']
  Lt = range_t.size

  # Initialize activity
  rE = np.zeros(Lt)
  rI = np.zeros(Lt)
  rE[0] = rE_init
  rI[0] = rI_init
  I_ext_E = I_ext_E * np.ones(Lt)
  I_ext_I = I_ext_I * np.ones(Lt)  # ensure the external input an array

  # simulate the Wilson-Cowan equations
  for k in range(Lt-1):

    # Calculate the derivative of E population
    drE = dt/tau_E * (-rE[k] + F(wEE * rE[k] - wEI * rI[k] + I_ext_E[k],
                                 a_E, theta_E))

    # calculate the derivative of I population
    drI = dt/tau_I * (-rI[k] + F(wIE * rE[k] - wII * rI[k] + I_ext_I[k],
                                 a_I, theta_I))

    # Update using Euler's method
    rE[k+1] = rE[k] + drE
    rI[k+1] = rI[k] + drI

  return rE, rI


pars = default_pars()
# Uncomment the below lines after completing the simulate_wc function
# Here are tow trjectories with close intial values
pars['rE_init'], pars['rI_init'] = 0.32, 0.15
rE1, rI1 = simulate_wc(pars)
pars['rE_init'], pars['rI_init'] = 0.33, 0.15
rE2, rI2 = simulate_wc(pars)

with plt.xkcd():
  my_test_plot(pars['range_t'], rE1, rI1, rE2, rI2)