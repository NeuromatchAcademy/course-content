def markov_forward(p0, D):
  """Calculate the forward predictive distribution in a discrete Markov chain

  Args:
    p0 (numpy vector): a discrete probability vector
    D (numpy matrix): the transition matrix, D[i,j] means the prob. to
    switch FROM i TO j

  Returns:
    p1 (numpy vector): the predictive probabilities in next time step
  """

  p1 = D.T @ p0
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