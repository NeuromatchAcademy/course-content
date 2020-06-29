
marginalization_matrix = np.zeros_like(posterior_matrix)

marginalization_matrix = input_matrix * binary_decision_matrix

marginal = np.sum(marginalization_matrix, axis=0)
marginal = marginal / np.sum(marginal)

with plt.xkcd():
  plot_mymatrix(marginalization_matrix, 'x', 'x_hat', 'Sample Marginalization Matrix')

with plt.xkcd():
  fig = plt.figure(figsize=(fig_w*1.192, fig_h*1.5))
  plt.plot(x, marginal)
  plt.xlabel('x_hat')
  plt.ylabel('probability')
  plt.title('Sample Marginal ')
  plt.show()