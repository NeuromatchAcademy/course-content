
np.random.seed(2020)  # set random seed
X_noisy = add_noise(X, .2)
score_noisy, evectors_noisy, evals_noisy = pca(X_noisy)
variance_explained_noisy = get_variance_explained(evals_noisy)

with plt.xkcd():
  plot_MNIST_sample(X_noisy)
  plot_variance_explained(variance_explained_noisy)