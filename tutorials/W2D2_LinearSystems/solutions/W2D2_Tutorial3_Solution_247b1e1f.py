np.random.seed(2020) # set random seed

# sweep through values for lambda
lambdas = np.arange(0.05, 0.95, 0.01)
empirical_variances = np.zeros_like(lambdas)
analytical_variances = np.zeros_like(lambdas)

sig = 0.87

# compute empirical equilibrium variance
for i, lam in enumerate(lambdas):
    empirical_variances[i] = ddm_eq_var(5000, x0, xinfty, lambdas[i], sig)

# Hint: you can also do this in one line outside the loop!
analytical_variances = sig**2 / (1 - lambdas**2)

with plt.xkcd():
  var_comparison_plot(empirical_variances, analytical_variances)
