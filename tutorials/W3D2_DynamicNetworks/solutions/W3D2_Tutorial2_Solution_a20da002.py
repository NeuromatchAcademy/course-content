def EIderivs(E_grid, I_grid, pars):
  """
  Time derivatives for E/I variables (dE/dt, dI/dt).
  """
  
  tau_E, a_E, theta_E = pars['tau_E'], pars['a_E'], pars['theta_E']
  tau_I, a_I, theta_I = pars['tau_I'], pars['a_I'], pars['theta_I']
  wEE, wEI = pars['wEE'], pars['wEI'] 
  wIE, wII = pars['wIE'], pars['wII']
  I_ext_E, I_ext_I = pars['I_ext_E'], pars['I_ext_I'] 
  
  # complete the code according Equations. (4)
  dEdt=(-E_grid + F(wEE*E_grid-wEI*I_grid+I_ext_E,a_E,theta_E))/tau_E
  dIdt=(-I_grid + F(wIE*E_grid-wII*I_grid+I_ext_I,a_I,theta_I))/tau_I
  
  return dEdt, dIdt

pars = default_pars()
with plt.xkcd():
  fig4 = plt.figure(figsize=(8/0.9, 5.5/0.9))
  ax = fig4.add_axes([0.1, 0.1, 0.6, 0.7])
  my_plot_trajectories(pars, 0.2, 6, 'Sample trajectories \nof different initials')
  my_plot_trajectory(pars, 'orange', [0.6, 0.8], 'Sample trajectory to \nlow activity')
  my_plot_trajectory(pars, 'm', [0.6, 0.6], 'Sample trajectory to \nhigh activity')
  my_plot_vector(pars)
  my_plot_nullcline(pars)
  plt.legend(loc=[1.02, 0.6], fontsize=12, handlelength=1)