
pars = default_pars(T=10000)
my_bin = np.arange(0, pars['T'], 20) # 20 [ms] bin-size

n_trials = 100 # 20 realizations
r12 = np.zeros(n_trials)
for i in range(n_trials):  
  sp1, sp2 = generate_corr_Poisson(pars, 20., 0.2)
  sp1_count, _ = np.histogram(sp1, bins=my_bin)
  sp2_count, _ = np.histogram(sp2, bins=my_bin)

  r12[i] = my_CC(sp1_count, sp2_count)

print('True corr coe = %.3f' % c)
print('Simu corr coe = %.3f' % r12.mean())