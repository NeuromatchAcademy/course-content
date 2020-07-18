
def mse(x, x_hats):
  """Mean-squared error cost function
    Args:
      x (scalar): One true value of $x$
      x_hats (scalar or ndarray): Estimate of x 
    Returns:
      same shape/type as x_hats): MSE costs associated with 
      predicting x_hats instead of x$
  """

  ##############################################################################
  # Complete the MSE cost function
  #
  ### Comment out the line below to test your function
  #raise NotImplementedError("You need to complete the MSE cost function!")
  ##############################################################################
  
  my_mse = (x - x_hats)**2
  return my_mse


def abs_err(x, x_hats):
  """Absolute error cost function
    Args:
      x (scalar): One true value of $x$
      x_hats (scalar or ndarray): Estimate of x 
    Returns:
      (same shape/type as x_hats): absolute error costs associated with 
      predicting x_hats instead of x$
  """

  ##############################################################################
  # Complete the absolute error cost function
  #
  ### Comment out the line below to test your function
  #raise NotImplementedError("You need to complete the absolute error function!")
  ##############################################################################
  
  my_abs_err = np.abs(x - x_hats)
  return my_abs_err


def zero_one_loss(x, x_hats):
  """Zero-One loss cost function
    Args:
      x (scalar): One true value of $x$
      x_hats (scalar or ndarray): Estimate of x 
    Returns:
      (same shape/type as x_hats) of the 0-1 Loss costs associated with predicting x_hat instead of x
  """

  ##############################################################################
  # Complete the zero-one loss cost function
  #
  ### Comment out the line below to test your function
  #raise NotImplementedError("You need to complete the 0-1 loss cost function!")
  ##############################################################################
      
  my_zero_one_loss = (x != x_hats).astype(np.float)
  return my_zero_one_loss


## When you are done with the functions above, uncomment the line below to 
## visualize them
with plt.xkcd():
  visualize_loss_functions(mse, abs_err, zero_one_loss)
