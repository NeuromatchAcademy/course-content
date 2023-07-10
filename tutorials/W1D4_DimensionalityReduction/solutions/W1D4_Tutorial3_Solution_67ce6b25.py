np.random.seed(2020)  # set random seed

# Add noise to data
X_noisy = add_noise(X, .2)

# Compute mean of noise-corrupted data
X_noisy_mean = np.mean(X_noisy, 0)

# Project onto the original basis vectors
projX_noisy = np.matmul(X_noisy - X_noisy_mean, evectors)

# Reconstruct the data using the top 50 components
X_reconstructed = reconstruct_data(projX_noisy, evectors, X_noisy_mean, 50)

# Visualize
with plt.xkcd():
  plot_MNIST_reconstruction(X_noisy, X_reconstructed)