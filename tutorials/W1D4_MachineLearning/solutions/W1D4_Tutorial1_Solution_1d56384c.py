def make_design_matrix(stim, d=25):
  """Create time-lag design matrix from stimulus intensity vector.

  Args:
    stim (1D array): Stimulus intensity at each time point.
    d (number): Number of time lags to use.

  Returns
    X (2D array): GLM design matrix with shape T, d

  """
  padded_stim = np.concatenate([np.zeros(d - 1), stim])   
  T = len(stim)
  X = np.zeros((T, d))
  for t in range(T):
      X[t] = padded_stim[t:t + d]

  return X            

#with plt.xkcd(): #not using plt.xkcd() as it changes plot suboptimally
X = make_design_matrix(stim)
plot_glm_matrices(X, spikes, nt=50)
plt.show()