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
