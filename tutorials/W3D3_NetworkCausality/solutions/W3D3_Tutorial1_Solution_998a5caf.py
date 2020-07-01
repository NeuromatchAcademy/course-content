def neuron_B(activity_of_A):
  """Model activity of neuron B as neuron A activity + noise

  Args:
    activity_of_A (ndarray): An array of shape (T,) containing the neural activity of neuron A

  Returns:
    ndarray: activity of neuron B
  """
  noise = np.random.randn(*activity_of_A.shape)
  return activity_of_A + noise

A_0 = np.zeros(5000)
A_1 = np.ones(5000)

diff_in_means = neuron_B(A_1).mean() - neuron_B(A_0).mean()
print(diff_in_means) 