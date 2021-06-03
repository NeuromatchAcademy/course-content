def markov_forward(p0, A):
  """Calculate the forward predictive distribution in a discrete Markov chain

  Args:
    p0 (numpy vector): a discrete probability vector
    A (numpy matrix): the transition matrix, A[i,j] means the prob. to
    switch FROM i TO j

  Returns:
    p1 (numpy vector): the predictive probabilities in next time step
  """

  p1 = A.T @ p0
  return p1


# Set random seed
np.random.seed(101)

# Set parameters of HMM
T = 100
switch_prob = 0.1
noise_level = 2.0

# Create HMM
model = create_HMM(switch_prob=switch_prob, noise_level=noise_level)

# Get predictive probabilities
predictive_probs = simulate_prediction_only(model, T)

# Visualize
with plt.xkcd():
  plot_marginal_seq(predictive_probs, switch_prob)