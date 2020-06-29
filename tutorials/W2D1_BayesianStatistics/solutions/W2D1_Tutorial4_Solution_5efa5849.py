
posterior_matrix = np.zeros_like(likelihood_matrix)

# You might be tempted to write a for-loop over rows or individual elements, like this:
#for i_posterior in np.arange(posterior_matrix.shape[0]):
#    posterior_matrix[i_posterior,:] = np.multiply(prior_matrix[i_posterior,:], likelihood_matrix[i_posterior,:])
#    posterior_matrix[i_posterior,:] = posterior_matrix[i_posterior,:] / np.sum(posterior_matrix[i_posterior,:])

# However, the vectorized version is faster and easier to understand.
posterior_matrix = likelihood_matrix * prior_matrix
posterior_matrix/= posterior_matrix.sum(axis=1, keepdims=True)

with plt.xkcd():
  plot_mymatrix(posterior_matrix, 'x', 'x_tilde', 'Sample Posterior Matrix : p(x | x_tilde)')