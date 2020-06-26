
def define_orthonormal_basis(u):
  """
  Calculates an orthonormal basis given an arbitrary vector u.
  
  Args:
    u (numpy array of floats):    arbitrary 2-dimensional vector used for new basis
  
  Returns: 
    (numpy array of floats) : new orthonormal basis
                                columns correspond to basis vectors
  """
  u = u / np.sqrt(u[0]**2 + u[1]**2)
  w = np.array([-u[1],u[0]])
  W = np.column_stack((u,w))
  return W


W = define_orthonormal_basis(u)

with plt.xkcd():
  plot_basis_vectors(X,W)