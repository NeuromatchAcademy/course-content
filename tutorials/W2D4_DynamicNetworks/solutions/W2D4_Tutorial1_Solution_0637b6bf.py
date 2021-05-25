r = np.linspace(0, 1, 1000)
pars = default_pars_single(I_ext=0.5, w=5)
drdt = compute_drdt(r, **pars)

r_guess_vector = [0, .4, .9]

x_fps = my_fp_finder(pars, r_guess_vector)
with plt.xkcd():
  plot_dr_r(r, drdt, x_fps)