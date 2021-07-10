
np.random.seed(2020)  # set random seed

# Add noise to data
X_noisy = add_noise(X, .2)

# Perform PCA on noisy data
score_noisy, evectors_noisy, evals_noisy = pca(X_noisy)

# Compute variance explained
variance_explained_noisy = get_variance_explained(evals_noisy)

# Visualize
with plt.xkcd():
  plot_MNIST_sample(X_noisy)
  plot_variance_explained(variance_explained_noisy)