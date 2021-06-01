def circuit_implementation(W, u0, T):
  """ Simulate the responses of N neurons over time given their connections

  Args:
    W (ndarray): weight matrix of synaptic connections, should be N x N
    u0 (ndarray): initial condition or input vector, should be N,
    T (scalar): number of time steps to run simulation for

  Returns:
    u (ndarray): the neural responses over time, should be N x T

  """

  # Compute the number of neurons
  N = W.shape[0]

  # Initialize empty response array and initial condition
  u = np.zeros((N, T))
  u[:, 0]  = u0

  # Loop over time steps and compute u(t+1)
  for i_t in range(1, T):
      u[:, i_t] = W @ u[:, i_t-1]

  return u


# Define W, u0, T
W = np.array([[1, .2], [.1, 1]])
u0 = np.array([1, 1])
T = 30

# Get neural activities
u = circuit_implementation(W, u0, T)

# Visualize neural activities
with plt.xkcd():
  plot_circuit_responses(u, W)