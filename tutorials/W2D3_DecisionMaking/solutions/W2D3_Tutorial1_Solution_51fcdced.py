def simulate_SPRT_fixedtime(sigma, stop_time, true_dist=1):
  """Simulate a Sequential Probability Ratio Test with fixed time stopping
  rule. Two observation models are 1D Gaussian distributions N(1,sigma^2) and
  N(-1,sigma^2).

  Args:
    sigma (float): Standard deviation
    stop_time (int): Number of samples to take before stopping
    true_dist (0 or 1): Which state is the true state.

  Returns:
    evidence_history (numpy vector): the history of cumulated evidence given
                                      generated data
    decision (int): 1 for pR, 0 for pL
    data (numpy vector): the generated sequences of data in this trial
  """
  muL = -1.0
  muR = 1.0

  pL = stats.norm(loc=-1, scale=sigma)
  pR = stats.norm(loc=1, scale=sigma)

  # Generate a random sequence of data
  if true_dist == 1:
    data = pR.rvs(size=stop_time)
  else:
    data = pL.rvs(size=stop_time)

  # Calculate cumulated evidence
  ll_ratio_vec = log_likelihood_ratio(data, pL, pR)

  evidence_history = np.cumsum(ll_ratio_vec)

  # Make decision
  if evidence_history[-1] > 0:
    decision = 1
  elif evidence_history[-1] < 0:
    decision = 0
  else:
    decision = np.random.randint(2)

  return evidence_history, decision, data


np.random.seed(100)
sigma = 3.5  # standard deviation for pL and pR
num_sample = 10  # number of simulations to run for each stopping time
stop_time = 150 # stopping time

with plt.xkcd():
  simulate_and_plot_SPRT_fixedtime(sigma, stop_time, num_sample)