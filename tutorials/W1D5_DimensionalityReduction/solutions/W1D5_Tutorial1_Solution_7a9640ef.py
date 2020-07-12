def define_orthonormal_basis(u):
  """
  Calculates an orthonormal basis given an arbitrary vector u.

  Args:
    u (numpy array of floats) : arbitrary 2-dimensional vector used for new
                                basis

  Returns:
    (numpy array of floats)   : new orthonormal basis
                                columns correspond to basis vectors
  """

  # normalize vector u
  u = u / np.sqrt(u[0] ** 2 + u[1] ** 2)
  # calculate vector w that is orthogonal to w
  w = np.array([-u[1], u[0]])

  W = np.column_stack((u, w))

  return W


np.random.seed(2020)  # set random seed
variance_1 = 1
variance_2 = 1
corr_coef = 0.8

cov_matrix = calculate_cov_matrix(variance_1, variance_2, corr_coef)
X = get_data(cov_matrix)
u = np.array([3, 1])

# Uncomment and run below to plot the basis vectors
W = define_orthonormal_basis(u)
with plt.xkcd():
  plot_basis_vectors(X, W)