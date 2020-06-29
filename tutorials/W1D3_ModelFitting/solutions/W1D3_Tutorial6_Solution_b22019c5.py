
def compute_mse(x_train,x_test,y_train,y_test,theta_hat,max_order):

  """Compute MSE on training data and test data.
    
  Args:
    x_train(ndarray):An array of shape (samples, ) that contains the training set input values.
    x_test(ndarray): An array of shape (samples,) that contains the test set values.
    y_train(ndarray): An array of shape (samples, ) that contains the output values.
    y_test(ndarray): An array of shape (samples, ) that contains the output testing set.
    theta_hat(numpy array): (input_features, max_order+1) Each column contains the fitted 
    weights for that order of polynomial regression
    max_order (scalar): The order of the polynomial we want to fit

  Returns:
    mse_train: MSE error on training data for each order
    mse_test: MSE error on test data for each order
  """

  mse_train = np.zeros((max_order+1))
  for order in range(0, max_order+1):
    X_design_train = make_design_matrix(x_train, order)
    y_hat = np.dot(X_design_train, theta_hat[order])
    residuals = y_train - y_hat
    mse_train[order] = np.mean(residuals ** 2)

  mse_test = np.zeros((max_order+1))
  for order in range(0, max_order+1):
    X_design_test = make_design_matrix(x_test, order)
    y_hat = np.dot(X_design_test, theta_hat[order])
    residuals = y_test - y_hat
    mse_test[order] = np.mean(residuals ** 2)

  return mse_train, mse_test

mse_train, mse_test = compute_mse(x_train,x_test,y_train,y_test,theta_hat,max_order)

with plt.xkcd():
  width = .35
  plt.figure()
  plt.bar(np.arange(max_order+1) - width/2, mse_train, width, label="train MSE")
  plt.bar(np.arange(max_order+1) + width/2, mse_test , width, label="test MSE")
  plt.legend()
  plt.xlabel('polynomial order')
  plt.ylabel('MSE')
  plt.title('comparing polynomial fits');
