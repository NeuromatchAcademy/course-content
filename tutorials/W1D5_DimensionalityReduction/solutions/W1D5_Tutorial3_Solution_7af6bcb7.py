
def get_variance_explained(evals):
  """
  Plots eigenvalues.
  
  Args:
     (numpy array of floats) : Vector of eigenvalues
     
  Returns: 
    Nothing.
    
  """
  return np.cumsum(evals)/np.sum(evals)
  
variance_explained = get_variance_explained(evals)

with plt.xkcd():
  plot_variance_explained(variance_explained)