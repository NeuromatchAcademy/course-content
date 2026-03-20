pars = default_pars()

with plt.xkcd():
  my_plot_nullcline(pars)

  # Find the first fixed point
  x_fp_1 = my_fp(pars, 0.1, 0.1)
  if check_fp(pars, x_fp_1):
    plot_fp(x_fp_1)

  # Find the second fixed point
  x_fp_2 = my_fp(pars, 0.3, 0.3)
  if check_fp(pars, x_fp_2):
    plot_fp(x_fp_2)

  # Find the third fixed point
  x_fp_3 = my_fp(pars, 0.8, 0.6)
  if check_fp(pars, x_fp_3):
    plot_fp(x_fp_3)