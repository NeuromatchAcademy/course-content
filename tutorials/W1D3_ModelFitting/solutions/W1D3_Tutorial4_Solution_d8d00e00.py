mse = np.zeros((max_order + 1))
for order in range(0, max_order + 1):

  X_design = make_design_matrix(x, order)

  # Get prediction for the polynomial regression model of this order
  y_hat = X_design @ theta_hats[order]

  # Compute the residuals
  residuals = y - y_hat

  # Compute the MSE
  mse[order] = np.mean(residuals ** 2)

with plt.xkcd():
  fig, ax = plt.subplots()

  ax.bar(range(max_order + 1), mse);

  ax.set(title='Comparing Polynomial Fits', xlabel='Polynomial order', ylabel='MSE')