
evals, evectors = np.linalg.eig(cov_matrix)
evals, evectors = sort_evals_descending(evals,evectors)

with plt.xkcd():
  plot_basis_vectors(X,evectors)
