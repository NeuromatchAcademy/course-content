def simulate_SPRT_fixedtime(mu, sigma, stop_time, true_dist = 1):
  """Simulate a Sequential Probability Ratio Test with fixed time stopping
  rule. Two observation models are 1D Gaussian distributions N(1,sigma^2) and
  N(-1,sigma^2).

  Args:
    mu (float): absolute mean value of the symmetric observation distributions
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
  assert mu > 0, "Mu should be > 0"
  mu_pos = mu
  mu_neg = -mu

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

  # STEP 1: Calculate accumulated evidence (S) given a time series of evidence (hint: np.cumsum)
  evidence_history = np.cumsum(ll_ratio_vec)

  # STEP 2: Make decision based on the sign of the evidence at the final time.
  decision = np.sign(evidence_history[-1])

  return evidence_history, decision, Mvec


# Set random seed
np.random.seed(100)

# Set model parameters
mu = .2
sigma = 3.5  # standard deviation for p+ and p-
num_sample = 10  # number of simulations to run
stop_time = 150 # number of steps before stopping

# Simulate and visualize
with plt.xkcd():
  simulate_and_plot_SPRT_fixedtime(mu, sigma, stop_time, num_sample)