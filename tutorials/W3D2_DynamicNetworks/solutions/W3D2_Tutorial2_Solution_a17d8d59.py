pars = default_pars()     # get the default value
x = np.arange(0, 10, .1)  # set the input

print(pars['a_E'], pars['theta_E'])
print(pars['a_I'], pars['theta_I'])

# Compute the F-I of E population
FI_exc = F(x, pars['a_E'], pars['theta_E'])
# Compute the F-I of I population
FI_inh = F(x, pars['a_I'], pars['theta_I'])

# Uncomment when you fill the (...)
with plt.xkcd():
  plot_FI_EI(x, FI_exc, FI_inh)