
# Take only the first 2000 samples with the corresponding labels
X, labels = X[:2000, :], labels[:2000]

# Perform PCA
scores = pca_model.transform(X)

# Plot the data and reconstruction
with plt.xkcd():
  visualize_components(scores[:, 0], scores[:, 1], labels)