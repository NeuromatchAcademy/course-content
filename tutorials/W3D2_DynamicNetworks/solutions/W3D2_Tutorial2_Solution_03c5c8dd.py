pars = default_pars(T=100.)
pars['wEE'], pars['wEI'] = 6.4, 4.8
pars['wIE'], pars['wII'] = 6.0, 1.2
pars['I_ext_E'] = 0.8

with plt.xkcd():
  plt.figure(figsize=(7, 5.5))
  my_plot_nullcline(pars)

  # Find the correct fixed point
  x_fp_1 = my_fp(pars, 0.8, 0.8)
  if check_fp(pars, x_fp_1):
    plot_fp(x_fp_1, position=(0, 0), rotation=40)

  my_plot_trajectories(pars, 0.2, 3,
                       'Sample trajectories \nwith different initial values')

  my_plot_vector(pars)

  plt.legend(loc=[1.01, 0.7])
  plt.xlim(-0.05, 1.01)
  plt.ylim(-0.05, 0.65)
  plt.show()