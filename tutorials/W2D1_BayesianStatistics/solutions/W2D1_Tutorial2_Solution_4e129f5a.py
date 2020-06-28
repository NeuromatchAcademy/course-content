
posterior_matrix = np.zeros_like(likelihood_matrix)

for i_posterior in np.arange(posterior_matrix.shape[0]):
    posterior_matrix[i_posterior,:] = prior_matrix[i_posterior,:] * likelihood_matrix[i_posterior,:]
    posterior_matrix[i_posterior,:] = posterior_matrix[i_posterior,:] / np.sum(posterior_matrix[i_posterior,:])
    
with plt.xkcd():
    plot_mymatrix(x, posterior_matrix, 'Orientation (Degree)', 'Repetitions', 'Sample Output')