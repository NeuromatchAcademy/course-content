
# sweep through values for lambda
lambdas = np.arange(0.05, 0.95, 0.01)
empirical_variances = np.zeros_like(lambdas)
analytical_variances = np.zeros_like(lambdas)

sig = 0.87

# compute empirical equilibrium variance
for i, lam in enumerate(lambdas):
    empirical_variances[i] = ddm_eq_var(5000, x0, xinfty, lambdas[i], sig)

analytical_variances = sig**2 / 2 / (1 - lambdas)

with plt.xkcd():
  var_comparison_plot(empirical_variances, analytical_variances)
