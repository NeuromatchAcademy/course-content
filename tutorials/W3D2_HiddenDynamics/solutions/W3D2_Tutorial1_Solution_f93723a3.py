def simulate_SPRT_threshold(sigma, threshold , true_dist=1):
  """Simulate a Sequential Probability Ratio Test with thresholding stopping
  rule. Two observation models are 1D Gaussian distributions N(1,sigma^2) and
  N(-1,sigma^2).

  Args:
    sigma (float): Standard deviation
    threshold (float): Desired log likelihood ratio threshold to achieve
                        before making decision

  Returns:
    evidence_history (numpy vector): the history of cumulated evidence given
                                      generated data
    decision (int): 1 for pR, 0 for pL
    data (numpy vector): the generated sequences of data in this trial
  """
  muL = -1.0
  muR = 1.0

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

    # individual log likelihood ratios
    ll_ratio = log_likelihood_ratio(Mvec, pL, pR)
    # cumulated evidence for this chunk
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
  if evidence_history[-1] > 0:
    decision = 1
  elif evidence_history[-1] < 0:
    decision = 0
  else:
    decision = np.random.randint(2)

  return evidence_history, decision, data_history


np.random.seed(100)
sigma = 2.8
num_sample = 10
log10_alpha = -6.5 # log10(alpha)
alpha = np.power(10.0, log10_alpha)

with plt.xkcd():
  simulate_and_plot_SPRT_fixedthreshold(sigma, num_sample, alpha)