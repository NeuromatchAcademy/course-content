
# Solution
res = x2 - (lam_hat * x[0:-2]) # remove later

with plt.xkcd():
  plot_residual_histogram(res)