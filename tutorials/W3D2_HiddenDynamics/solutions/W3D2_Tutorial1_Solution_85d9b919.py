def simulate_SPRT_fixedtime(sigma, stop_time, true_dist = 1):
  """Simulate a Sequential Probability Ratio Test with fixed time stopping
  rule. Two observation models are 1D Gaussian distributions N(1,sigma^2) and
  N(-1,sigma^2).

  Args:
    sigma (float): Standard deviation of observation models
    stop_time (int): Number of samples to take before stopping
    true_dist (1 or -1): Which state is the true state.

  Returns:
    evidence_history (numpy vector): the history of cumulated evidence given
                                      generated data
    decision (int): 1 for s = 1, -1 for s = -1
    Mvec (numpy vector): the generated sequences of measurement data in this trial
  """

  # Set means of observation distributions
  mu_pos = 1.0
  mu_neg = -1.0

  # Make observation distributions
  p_pos = stats.norm(loc = mu_pos, scale = sigma)
  p_neg = stats.norm(loc = mu_neg, scale = sigma)

  # Generate a random sequence of measurements
  if true_dist == 1:
    Mvec = p_pos.rvs(size = stop_time)
  else:
    Mvec = p_neg.rvs(size = stop_time)

  # Calculate log likelihood ratio for each measurement (delta_t)
  ll_ratio_vec = log_likelihood_ratio(Mvec, p_neg, p_pos)

  # Calculate cumulated evidence (S) given a vector of individual evidences (hint: np.cumsum)
  evidence_history = np.cumsum(ll_ratio_vec)

  # Make decision
  if evidence_history[-1] > 0:
    # Decision given positive S_t (last value of evidence history)
    decision = 1
  elif evidence_history[-1] < 0:
    # Decision given negative S_t (last value of evidence history)
    decision = -1
  else:
    # Random decision if S_t is 0
    decision = np.random.randint(2)

  return evidence_history, decision, Mvec


# Set random seed
np.random.seed(100)

# Set model parameters
sigma = 3.5  # standard deviation for p+ and p-
num_sample = 10  # number of simulations to run
stop_time = 150 # number of steps before stopping

with plt.xkcd():
  simulate_and_plot_SPRT_fixedtime(sigma, stop_time, num_sample)