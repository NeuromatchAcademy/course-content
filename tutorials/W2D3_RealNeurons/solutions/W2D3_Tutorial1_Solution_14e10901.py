pars = default_pars(T=100.)
sig_gwn = 5.
mu_gwn = 250.

# Calculate the GWN current
I_GWN = my_GWN(pars, mu=mu_gwn, sig=sig_gwn, myseed=2020)

# Run the model and calculate the v and the sp
v, sp = run_LIF(pars, Iinj=I_GWN)

with plt.xkcd():
  plot_GWN(pars, I_GWN)
  plt.show()