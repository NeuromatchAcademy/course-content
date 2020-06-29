
binary_decision_matrix = np.zeros_like(posterior_matrix)

for i_posterior in np.arange(posterior_matrix.shape[0]):
    mean, _, _ = moments_myfunc(x, posterior_matrix[i_posterior,:])
    idx = np.argmin(np.abs(x - mean))
    binary_decision_matrix[i_posterior,idx] = 1 

with plt.xkcd():
  plot_mymatrix(binary_decision_matrix, 'x_tilde', 'x_hat', 'Sample Binary Decision Matrix\nx_hat = mean(x_tilde)')