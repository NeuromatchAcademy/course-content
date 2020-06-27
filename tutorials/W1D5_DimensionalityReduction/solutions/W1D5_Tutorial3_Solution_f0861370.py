score, evectors, evals = pca(X)

with plt.xkcd():
  plot_eigenvalues(evals)
  plt.xlim([0,100])