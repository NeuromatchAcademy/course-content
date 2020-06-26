
def reconstruct_data(score,evectors,X_mean,K):
  """
  Reconstruct the data based on the top K components.
  
  Args:
     score (numpy array of floats) : Score matrix
     evectors (numpy array of floats) : Matrix of eigenvectors
     X_mean (numpy array of floats) : Vector corresponding to data mean
     K (scalar) : Number of components to include
     
  Returns: 
     (numpy array of floats) : Matrix of reconstructed data 
    
  """
  X_reconstructed = np.matmul(score[:,:K],evectors[:,:K].T) + X_mean
  return X_reconstructed

K = 784

with plt.xkcd():
  X_mean = np.mean(X,0) 
  X_reconstructed = reconstruct_data(score,evectors,X_mean,K)
  plot_MNIST_reconstruction(X ,X_reconstructed)
