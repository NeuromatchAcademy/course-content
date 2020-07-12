
evals, evectors = np.linalg.eigh(cov_matrix)
evals, evectors = sort_evals_descending(evals, evectors)

with plt.xkcd():
  plot_basis_vectors(X, evectors)