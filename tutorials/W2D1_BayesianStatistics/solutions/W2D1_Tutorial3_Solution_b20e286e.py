def mse(x, x_hats):
    """Mean squared error (MSE) cost function
    Args:
      x: One true value of $x$
      x_hat: Estimate of $x$
    Returns:
      ndarray of the MSE costs associated with predicting x_hat instead of x$
    """
    return (x - x_hats)**2

def abs_err(x, x_hats):
    """Absolute error  cost function
    Args:
      x (scalar): One true value of $x$
      x_hat (scalar or ndarray): Estimate of $x$ 
    Returns:
      ndarray of the absolute error costs associated with predicting x_hat instead of x$
    """
    return np.abs(x - x_hats)

def zero_one_loss(x, x_hats):
  """Zero-One Loss cost function
    Args:
      x (scalar): One true value of $x$
      x_hat (scalar or ndarray): Estimate of $x$ 
    Returns:
      ndarray of the 0-1 Loss costs associated with predicting x_hat instead of x$
    """
  return (x != x_hats).astype(np.float)

with plt.xkcd():
  visualize_loss_functions(mse, abs_err, zero_one_loss)
