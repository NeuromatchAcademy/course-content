pars = default_pars()
x = np.arange(0, 10, .1)

print(pars['a_E'], pars['theta_E'])
print(pars['a_I'], pars['theta_I'])

# Compute the F-I curve of the excitatory population
FI_exc = F(x, pars['a_E'], pars['theta_E'])

# Compute the F-I curve of the inhibitory population
FI_inh = F(x, pars['a_I'], pars['theta_I'])

# Visualize
with plt.xkcd():
  plot_FI_EI(x, FI_exc, FI_inh)