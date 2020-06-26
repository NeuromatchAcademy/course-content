def mse(x, y, theta_hat):
  """Compute the mean squared error
  
  Args:
    x (ndarray): An array of shape (samples,) that contains the input values.
    y (ndarray): An array of shape (samples,) that contains the corresponding
      measurement values to the inputs.
    theta_hat (float): An estimate of the slope parameter. 

  Returns:
    float: The mean squared error of the data with the estimated parameter.
  """
  y_hat = theta_hat * x
  mse = np.mean((y - y_hat)**2)
  return mse