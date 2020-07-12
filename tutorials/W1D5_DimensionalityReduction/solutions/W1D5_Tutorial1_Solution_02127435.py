

def change_of_basis(X, W):
  """
  Projects data onto new basis W.

  Args:
    X (numpy array of floats) : Data matrix each column corresponding to a
                                different random variable
    W (numpy array of floats) : new orthonormal basis columns correspond to
                                basis vectors

  Returns:
    (numpy array of floats)    : Data matrix expressed in new basis
  """

  ###################################################################
  # Insert your code here to:
  ###################################################################
  # project data onto new basis described by W
  Y = np.matmul(X, W)

  # comment this once you've filled the function
  # raise NotImplementedError("Student excercise: implement change of basis")

  return Y


# Unomment below to transform the data by projecting it into the new basis
Y = change_of_basis(X, W)
# Plot the projected data
with plt.xkcd():
  plot_data_new_basis(Y)