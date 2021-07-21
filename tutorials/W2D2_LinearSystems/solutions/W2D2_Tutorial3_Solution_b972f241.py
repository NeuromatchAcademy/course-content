def ddm(T, x0, xinfty, lam, sig):
    t = np.arange(0, T, 1.)
    x = np.zeros_like(t)
    x[0] = x0

    for k in range(len(t)-1):
        x[k+1] = xinfty + lam * (x[k] - xinfty) + sig * np.random.standard_normal(size=1)

    return t, x

# computes equilibrium variance of ddm
# returns variance
def ddm_eq_var(T, x0, xinfty, lam, sig):
    t, x = ddm(T, x0, xinfty, lam, sig)

    # returns variance of the second half of the simulation
    # this is a hack: assumes system has settled by second half
    return x[-round(T/2):].var()

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

# Plot the empirical variance vs analytical variance
with plt.xkcd():
  var_comparison_plot(empirical_variances, analytical_variances)