mse = np.zeros((max_order+1))
for order in range(0, max_order+1):
  X_design = make_design_matrix(x, order)
  y_hat = np.dot(X_design, theta_hat[order])
  residuals = y - y_hat
  mse[order] = np.mean(residuals ** 2)

with plt.xkcd():
  plt.bar(range(max_order+1), mse);
  plt.ylabel('MSE')
  plt.xlabel('polynomial order')
  plt.title('comparing polynomial fits');
