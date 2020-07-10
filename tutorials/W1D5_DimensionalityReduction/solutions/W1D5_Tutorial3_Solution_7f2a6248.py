score, evectors, evals = pca(X)

with plt.xkcd():
  plot_eigenvalues(evals, limit=False)
  plt.xlim([0, 100])
  plt.show()