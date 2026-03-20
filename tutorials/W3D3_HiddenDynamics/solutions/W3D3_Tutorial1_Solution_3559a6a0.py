def simulate_SPRT_threshold(mu, sigma, threshold , true_dist=1):
  """Simulate a Sequential Probability Ratio Test with thresholding stopping
  rule. Two observation models are 1D Gaussian distributions N(1,sigma^2) and
  N(-1,sigma^2).

  Args:
    mu (float): absolute mean value of the symmetric observation distributions
    sigma (float): Standard deviation
    threshold (float): Desired log likelihood ratio threshold to achieve
                        before making decision

  Returns:
    evidence_history (numpy vector): the history of cumulated evidence given
                                      generated data
    decision (int): 1 for pR, 0 for pL
    data (numpy vector): the generated sequences of data in this trial
  """
  assert mu > 0, "Mu should be > 0"
  muL = -mu
  muR = mu

  pL = stats.norm(muL, sigma)
  pR = stats.norm(muR, sigma)

  has_enough_data = False

  data_history = []
  evidence_history = []
  current_evidence = 0.0

  # Keep sampling data until threshold is crossed
  while not has_enough_data:
    if true_dist == 1:
      Mvec = pR.rvs()
    else:
      Mvec = pL.rvs()

    # STEP 1: individual log likelihood ratios
    ll_ratio = log_likelihood_ratio(Mvec, pL, pR)

    # STEP 2: accumulated evidence for this chunk
    evidence_history.append(ll_ratio + current_evidence)

    # update the collection of all data
    data_history.append(Mvec)
    current_evidence = evidence_history[-1]

    # check if we've got enough data
    if abs(current_evidence) > threshold:
      has_enough_data = True

  data_history = np.array(data_history)
  evidence_history = np.array(evidence_history)

  # Make decision
  if evidence_history[-1] >= 0:
    decision = 1
  elif evidence_history[-1] < 0:
    decision = 0

  return evidence_history, decision, data_history


# Set parameters
np.random.seed(100)
mu = 1.0
sigma = 2.8
num_sample = 10
log10_alpha = -3 # log10(alpha)
alpha = np.power(10.0, log10_alpha)

# Simulate and visualize
with plt.xkcd():
  simulate_and_plot_SPRT_fixedthreshold(mu, sigma, num_sample, alpha)