mse = np.zeros((max_order + 1))
for order in range(0, max_order + 1):
  X_design = make_design_matrix(x, order)
  y_hat = X_design @ theta_hat[order]
  residuals = y - y_hat
  mse[order] = np.mean(residuals ** 2)

with plt.xkcd():
  fig, ax = plt.subplots()

  ax.bar(range(max_order + 1), mse);

  ax.set(title='Comparing Polynomial Fits', xlabel='Polynomial order', ylabel='MSE')