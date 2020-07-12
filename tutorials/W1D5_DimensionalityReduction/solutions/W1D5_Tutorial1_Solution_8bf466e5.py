

def calculate_cov_matrix(var_1, var_2, corr_coef):
  """
  Calculates the covariance matrix based on the variances and correlation
  coefficient.

  Args:
    var_1 (scalar)          : variance of the first random variable
    var_2 (scalar)          : variance of the second random variable
    corr_coef (scalar)      : correlation coefficient

  Returns:
    (numpy array of floats) : covariance matrix
  """

  ##################################################################
  # Insert your code here to:
  ##################################################################

  # calculate the covariance from the variances and correlation
  cov = corr_coef * np.sqrt(var_1 * var_2)

  cov_matrix = np.array([[var_1, cov], [cov, var_2]])

  # Comment once you've filled in the function
  # raise NotImplementedError("Student excercise: calculate the covariance matrix!")
  
  return cov_matrix


###################################################################
# generate and plot bivariate Gaussian data with variances of 1
# and a correlation coefficients of: 0.8
# repeat while varying the correlation coefficient from -1 to 1
###################################################################
np.random.seed(2020)  # set random seed
variance_1 = 1
variance_2 = 1
corr_coef = 0.8

# Uncomment to test your code and plot
cov_matrix = calculate_cov_matrix(variance_1, variance_2, corr_coef)
X = get_data(cov_matrix)

with plt.xkcd():
  plot_data(X)