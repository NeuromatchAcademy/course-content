
input_matrix = np.zeros_like(posterior_matrix)

for i in np.arange(x.shape[0]):
  input_matrix[:, i] = my_gaussian(hypothetical_stim, -2.5, 1)
  input_matrix[:, i] = input_matrix[:, i] / np.sum(input_matrix[:, i])

with plt.xkcd():
  plot_mymatrix(input_matrix, 'x', 'x_tilde', 'Sample Input Matrix: p(x_tilde | x = -2.5)')