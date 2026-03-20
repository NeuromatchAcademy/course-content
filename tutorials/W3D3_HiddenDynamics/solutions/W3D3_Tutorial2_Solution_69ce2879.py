
def markov_forward(p0, D):
  """Calculate the forward predictive distribution in a discrete Markov chain

  Args:
    p0 (numpy vector): a discrete probability vector
    D (numpy matrix): the transition matrix, D[i,j] means the prob. to
    switch FROM i TO j

  Returns:
    p1 (numpy vector): the predictive probabilities in next time step
  """

  # Calculate predictive probabilities (prior)
  p1 = p0 @ D

  return p1

def one_step_update(model, posterior_tm1, M_t):
  """Given a HMM model, calculate the one-time-step updates to the posterior.
  Args:
    model (GaussianHMM1D instance): the HMM
    posterior_tm1 (numpy vector): Posterior at `t-1`
    M_t (numpy array): measurements at `t`
    Returns:
    posterior_t (numpy array): Posterior at `t`
  """
  # Calculate predictive probabilities (prior)
  prediction = markov_forward(posterior_tm1, model.transmat)

  # Get the likelihood
  likelihood = compute_likelihood(model, M_t)

  # Calculate posterior
  posterior_t = prediction * likelihood

  # Normalize
  posterior_t /= np.sum(posterior_t)

  return prediction, likelihood, posterior_t


# Set random seed
np.random.seed(12)

# Set parameters
switch_prob = 0.4
noise_level = .4
t = 75

# Create and sample from model
model = create_HMM(switch_prob = switch_prob,
                    noise_level = noise_level,
                    startprob=[0.5, 0.5])

measurements, states = sample(model, nstep)

# Infer state sequence
predictive_probs, likelihoods, posterior_probs = simulate_forward_inference(model, nstep,
                                                            measurements)
states_inferred = np.asarray(posterior_probs[:,0] <= 0.5, dtype=int)

# Visualize
with plt.xkcd():
  plot_forward_inference(
        model, states, measurements, states_inferred,
        predictive_probs, likelihoods, posterior_probs,t=t, flag_m = 0
      )