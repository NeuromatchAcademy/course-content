

def get_sample_cov_matrix(X):
  """
  Returns the sample covariance matrix of data X

  Args:
    X (numpy array of floats) : Data matrix each column corresponds to a
                                different random variable

  Returns:
    (numpy array of floats)   : Covariance matrix
  """

  ###################################################################
  # Insert your code here to ...
  ###################################################################

  # Subtract the mean of X
  X = X - np.mean(X, 0)
  # Calculate the covariance matrix (hint: use np.matmul)
  cov_matrix = cov_matrix = 1 / X.shape[0] * np.matmul(X.T, X)

  # Comment once you've filled in the function
  # raise NotImplementedError("Student excercise: calculate the cov matrix!")

  return cov_matrix


###################################################################
# Uncomment below code to:
# generate bivariate Gaussian data with variances of 1
# and a correlation coefficient of 0.8
# compare the true and sample covariance matrices
###################################################################
variance_1 = 1
variance_2 = 1
corr_coef = 0.8

np.random.seed(2020)  # set random seed
cov_matrix = calculate_cov_matrix(variance_1, variance_2, corr_coef)
print(cov_matrix)

X = get_data(cov_matrix)
sample_cov_matrix = get_sample_cov_matrix(X)
print(sample_cov_matrix)