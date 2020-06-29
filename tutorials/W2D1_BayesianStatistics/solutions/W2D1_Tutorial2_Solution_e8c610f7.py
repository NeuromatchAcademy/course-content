
binary_decision_matrix = np.zeros_like(posterior_matrix)

for i_posterior in np.arange(posterior_matrix.shape[0]):
    id_max = np.argmax(posterior_matrix[i_posterior,:])
    binary_decision_matrix[i_posterior,id_max] = 1

with plt.xkcd():
    plot_mymatrix(x, binary_decision_matrix, 'Orientation (Degree)', 'Repetitions', 'Binary Decision Matrix')