
X_noisy_mean = np.mean(X_noisy, 0)
projX_noisy = np.matmul(X_noisy - X_noisy_mean, evectors)
X_reconstructed = reconstruct_data(projX_noisy, evectors, X_noisy_mean, 50)

with plt.xkcd():
  plot_MNIST_reconstruction(X_noisy, X_reconstructed)