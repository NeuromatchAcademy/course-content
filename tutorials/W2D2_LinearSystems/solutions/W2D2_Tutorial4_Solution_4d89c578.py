
# compute the predicted values using the autoregressive model (lam_hat), and
# the residual is the difference between x2 and the prediction
res = x2 - (lam_hat * x[0:-2])

# Visualize
with plt.xkcd():
  plot_residual_histogram(res)