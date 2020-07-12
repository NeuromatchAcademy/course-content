

def get_variance_explained(evals):
  """
  Plots eigenvalues.

  Args:
    (numpy array of floats) : Vector of eigenvalues

  Returns:
    Nothing.

  """

  ###################################################################
  # Insert your code here to:
  ###################################################################

  # cumulatively sum the eigenvalues
  csum = np.cumsum(evals)
  # normalize by the sum of eigenvalues
  variance_explained = csum / np.sum(evals)
   
  # Comment once you've filled in the function
  # raise NotImplementedError("Student excercise: calculate explaine variance!")

  return variance_explained


###################################################################
# Insert your code here to:
###################################################################

# calculate the variance explained
variance_explained = get_variance_explained(evals)

# Uncomment to plot the variance explained
with plt.xkcd():
  plot_variance_explained(variance_explained)