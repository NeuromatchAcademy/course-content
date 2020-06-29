
likelihood_matrix = np.zeros_like(prior_matrix)

for i_likelihood in np.arange(hypothetical_stim.shape[0]):
    likelihood_matrix[i_likelihood,:] = my_gaussian(x, hypothetical_stim[i_likelihood], 1)
    likelihood_matrix[i_likelihood,:] = likelihood_matrix[i_likelihood,:] / np.sum(likelihood_matrix[i_likelihood,:])

with plt.xkcd():
  plot_mymatrix(likelihood_matrix, 'x', 'x_tilde : Brain representation of x', 'Sample Likelihood Matrix : p(x_tilde | x)')