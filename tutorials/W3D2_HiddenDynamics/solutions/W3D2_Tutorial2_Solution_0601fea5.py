
def one_step_update(model, posterior_tm1, Y_t):
  """Given a HMM model, calculate the one-time-step updates to the posterior.
  Args:
    model (GaussianHMM instance): the HMM
    posterior_tm1 (numpy array): Posterior at `t-1`
    Y_t (numpy array): Observation at `t`
    Returns:
    posterior_t (numpy array): Posterior at `t`
  """
  prediction = model.transmat_ @ posterior_tm1
  likelihood = np.exp(model._compute_log_likelihood(Y_t))
  posterior_t = prediction * likelihood
  return posterior_t


np.random.seed(101)
switch_prob = 0.1
noise_level = 0.5
nsample = 50
T = 160
model = create_HMM(switch_prob, noise_level)

posterior_list = []
for i in range(nsample):
  predictive_probs, posterior_probs = simulate_forward_inference(model, T)
  posterior_list.append(posterior_probs)
posterior_matrix = np.asarray(posterior_list)

with plt.xkcd():
  plot_evidence_vs_noevidence(posterior_matrix, predictive_probs)