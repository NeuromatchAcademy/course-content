
AIC = np.zeros((max_order+1))
for order in range(0, max_order+1):

  # Compute predictions for this model 
  X_design = make_design_matrix(x_train, order)
  y_hat = np.dot(X_design, theta_hat[order])

  # Compute SSE
  residuals = y_train - y_hat
  sse = np.sum(residuals ** 2)

  # Get K
  K = len(theta_hat[order])

  # Compute AIC
  AIC[order] = 2*K + n_samples * np.log(sse/n_samples)

with plt.xkcd():
  plt.bar(range(max_order+1), AIC);
  plt.ylabel('AIC')
  plt.xlabel('polynomial order')
  plt.title('comparing polynomial fits')
  plt.show()