
x = np.arange(-10, 11, 1)

prior_mean = 0.
prior_sigma1  = .5
prior_sigma2  = 3.
prior1 = my_gaussian(x, prior_mean, prior_sigma1)
prior2 = my_gaussian(x, prior_mean, prior_sigma2)

alpha = 0.05
prior_combined = (1-alpha) * prior1 + (alpha * prior2) 
prior_combined = prior_combined / np.sum(prior_combined)

prior_matrix = np.tile(prior_combined, 20).reshape((20,-1))

with plt.xkcd():
    plot_mymatrix(x, prior_matrix, 'Orientation (Degree)', 'Repetitions', 'Sample Output')