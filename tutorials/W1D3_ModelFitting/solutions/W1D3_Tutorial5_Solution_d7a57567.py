
def compute_mse(x_train,x_test,y_train,y_test,theta_hats,max_order):
  """Compute MSE on training data and test data.
    
  Args:
    x_train(ndarray): training data input vector of shape (n_samples) 
    x_test(ndarray): test vector of shape (n_samples) 
    y_train(ndarray): training vector of measurements of shape (n_samples)
    y_test(ndarray): test vector of measurements of shape (n_samples)
    theta_hats(dict): fitted weights for each polynomial model (dict key is order)
    max_order (scalar): max order of polynomial fit

  Returns:
    ndarray, ndarray: MSE error on training data and test data for each order
  """

  mse_train = evaluate_poly_reg(x_train, y_train, theta_hats, max_order)
  mse_test = evaluate_poly_reg(x_test, y_test, theta_hats, max_order)

  return mse_train, mse_test


mse_train, mse_test = compute_mse(x_train, x_test, y_train, y_test, theta_hats, max_order)

with plt.xkcd():
  fig, ax = plt.subplots()
  ax.bar(np.arange(max_order + 1) - width/2, mse_train, width, label="train MSE")
  ax.bar(np.arange(max_order + 1) + width/2, mse_test , width, label="test MSE")
  ax.legend()
  ax.set(xlabel='Polynomial order', ylabel='MSE', title ='Comparing polynomial fits');
