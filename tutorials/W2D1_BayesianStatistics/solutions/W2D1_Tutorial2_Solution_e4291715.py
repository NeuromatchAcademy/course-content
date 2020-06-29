
visual_mean = np.linspace(-8, 8, x.shape[0]-1)
visual_sigma  = 2
likelihood_matrix = np.zeros_like(prior_matrix)

for i_likelihood in np.arange(visual_mean.shape[0]):
    likelihood_matrix[i_likelihood,:] = my_gaussian(x, visual_mean[i_likelihood], visual_sigma)
    likelihood_matrix[i_likelihood,:] = likelihood_matrix[i_likelihood,:]/np.sum(likelihood_matrix[i_likelihood,:])

with plt.xkcd():
    plot_mymatrix(x, likelihood_matrix, 'Orientation (Degree)', 'Repetitions', 'Sample Output')