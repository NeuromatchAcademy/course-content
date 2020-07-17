pars = default_pars_single()  # get default parameters

# set your external input and wEE
pars['I_ext'] = 0.5
pars['w'] = 5.0

r = np.linspace(0, 1, 1000)  # give the values of r

# Calculate drEdt
drdt = (-r + F(pars['w'] * r + pars['I_ext'],
               pars['a'], pars['theta'])) / pars['tau']

with plt.xkcd():
  plot_dr_r(r, drdt)

  # Calculate the first fixed point with your initial value
  x_fp_1 = my_fp_single(pars, 0.)
  if check_fp_single(pars, x_fp_1):
    plt.plot(x_fp_1, 0, 'bo', ms=8)

  # Calculate the second fixed point with your initial value
  x_fp_2 = my_fp_single(pars, 0.4)
  if check_fp_single(pars, x_fp_2):
    plt.plot(x_fp_2, 0, 'ro', ms=8)

  # Calculate the third fixed point with your initial value
  x_fp_3 = my_fp_single(pars, 0.9)
  if check_fp_single(pars, x_fp_3):
    plt.plot(x_fp_3, 0, 'yo', ms=8)

  plt.show()