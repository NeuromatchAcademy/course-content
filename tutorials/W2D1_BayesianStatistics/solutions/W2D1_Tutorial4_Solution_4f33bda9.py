
hypothetical_stim = np.linspace(-8, 8, 1000)
x = np.arange(-10, 10, 0.1)

alpha = 0.05
prior_mean = 0
prior_sigma1 = 0.5
prior_sigma2 = 10
prior1 = my_gaussian(x, prior_mean, prior_sigma1)
prior2 = my_gaussian(x, prior_mean, prior_sigma2)

prior_combined = (1-alpha) * prior1 + (alpha * prior2) 
prior_combined = prior_combined / np.sum(prior_combined)

prior_matrix = np.tile(prior_combined, hypothetical_stim.shape[0]).reshape((hypothetical_stim.shape[0], -1))

with plt.xkcd():
  plot_mymatrix(prior_matrix, 'x', 'Repetitions', 'Sample Prior Matrix: p(x)')