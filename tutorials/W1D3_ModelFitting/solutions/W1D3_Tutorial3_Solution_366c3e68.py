def bootstrap_estimates(x, y, n=1000):
  """Generate a set of theta_hat estimates using the bootstrap method.
    
  Args:
    x (ndarray): An array of shape (samples,) that contains the input values.
    y (ndarray): An array of shape (samples,) that contains the corresponding
      measurement values to the inputs.
    n (int): The number of estimates to compute

  Returns:
    ndarray: An array of estimated parameters with size (n,)
  """
  theta_hats = np.zeros(n)
  for i in range(n):
    x_, y_ = resample_with_replacement(x, y)
    theta_hats[i] = solve_normal_eqn(x_, y_)
  return theta_hats