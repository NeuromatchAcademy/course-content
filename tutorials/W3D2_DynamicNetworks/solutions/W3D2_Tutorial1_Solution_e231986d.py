pars = default_parsE() # get default parameters

#set your external input and wEE
pars['I_ext_E'] = 0.5
pars['wEE'] = 5.0
 
# give E_grid
E_grid = np.linspace(0, 1., 1000)

# Calculate dEdt
dEdt = -E_grid + F(pars['wEE']*E_grid+pars['I_ext_E'], pars['a_E'],  pars['theta_E'])


with plt.xkcd():
  plot_dE_E(E_grid, dEdt)
  #Calculate the fixed point with your initial value
  
  x_fp_1 = my_fpE(pars, 0.)
  if check_fpE(pars, x_fp_1):
    plt.plot(x_fp_1, 0, 'bo', ms=8)

  x_fp_2 = my_fpE(pars, 0.4)
  if check_fpE(pars, x_fp_2):
    plt.plot(x_fp_2, 0, 'ro', ms=8)

  x_fp_3 = my_fpE(pars, 0.9)
  if check_fpE(pars, x_fp_3):
    plt.plot(x_fp_3, 0, 'yo', ms=8)

  plt.show()