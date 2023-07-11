# Perform PCA
score, evectors, evals = pca(X)

# Plot the eigenvalues
with plt.xkcd():
  plot_eigenvalues(evals, xlimit=True)  # limit x-axis up to 100 for zooming