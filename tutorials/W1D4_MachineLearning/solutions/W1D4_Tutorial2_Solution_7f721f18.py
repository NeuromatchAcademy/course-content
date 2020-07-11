def get_n_zero_coefs(X, y, C_values):
  """Fits a logistic regression model with L1 regularization and returns
  the number of nonzero coefficients as well as the magnitude of the 
  parameters vector.

  Args:
    X (2D array): Data matrix
    y (1D array): Label vector
    C_values (list): List of inverse strengths of regularization

  Returns:
    n_zero_coefs: (int) number of coefficients in the fit model that are zero

  """
  n_zero_coefs = []
  for C in C_values:

    # Initialize and fit the model
    # (Hint, you may need to set max_iter)
    model = LogisticRegression(penalty="l1", C=C, solver="saga", max_iter=5000)

    model.fit(X,y)

    # get the coefs of the fit model
    coefs = model.coef_

    # get the number of nonzero elements in coefs
    n_zero = np.sum(coefs == 0)

    # append to list
    n_zero_coefs.append(n_zero)

  return n_zero_coefs

# Use log-spaced values for C
C_values = np.logspace(-4, 4, 5)

n_zeros_l1 = get_n_zero_coefs(X,y, C_values,)

with plt.xkcd():
  plot_zero_coefs(C_values, n_zeros_l1)