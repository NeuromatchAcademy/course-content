pars = default_pars(T=100.)
pars['wEE'], pars['wEI'] = 6.4, 4.8
pars['wIE'], pars['wII'] = 6.0, 1.2
pars['I_ext_E'] = 0.8


with plt.xkcd():
  fig6 = plt.figure(figsize=(8, 5.5))
  my_plot_trajectories(pars, 0.2, 3, 'Sample trajectories \nwith different initial values')
  my_plot_vector(pars)
  my_plot_nullcline(pars)

  x_fp_1 = my_fp(pars, 0.8, 0.8)
  if check_fp(x_fp_1):
    plt.plot(x_fp_1[0], x_fp_1[1], 'ko')
    plt.text(x_fp_1[0]-0.02, x_fp_1[1]+0.05, 'Fixed Point1=\n(%.3f, %.3f)' \
            %(x_fp_1[0], x_fp_1[1]), horizontalalignment='center', \
            verticalalignment='center', rotation=40)
  
  plt.legend(loc='best', fontsize=10)

  plt.xlim(-0.1, 1.1)
  plt.ylim(-0.05, 0.65)
  plt.show()