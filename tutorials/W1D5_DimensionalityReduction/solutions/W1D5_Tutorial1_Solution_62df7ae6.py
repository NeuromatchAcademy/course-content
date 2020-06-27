
def calculate_cov_matrix(var_1,var_2,corr_coef):
  """
  Calculates the covariance matrix based on the variances and correlation coefficient.
  
  Args:
    var_1 (scalar):    variance of the first random variable
    var_2 (scalar):    variance of the second random variable
    corr_coef (scalar):      correlation coefficient
  
  Returns: 
    (numpy array of floats) : covariance matrix
  """
  cov = corr_coef * np.sqrt(var_1 * var_2)
  cov_matrix = np.array([[var_1,cov],[cov,var_2]])
  return cov_matrix

cov_matrix = calculate_cov_matrix(variance_1,variance_2,corr_coef)
X = get_data(cov_matrix)

with plt.xkcd():
  plot_data(X)
