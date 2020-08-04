def instrument_strength_effect(etas, n_neurons, timesteps, n_trials):
  """ Compute IV estimation performance for different instrument strengths

  Args:
    etas (list): different instrument strengths to compare
    n_neurons (int): number of neurons in simulation
    timesteps (int): number of timesteps in simulation
    n_trials (int): number of trials to compute

  Returns:
    ndarray: n_trials x len(etas) array where each element is the correlation
        between true and estimated connectivity matries for that trial and
        instrument strength
  """

  # Initialize corr array
  corr_data = np.zeros((n_trials, len(etas)))

  # Loop over trials
  for trial in range(n_trials):
      print("Trial {} of {}".format(trial + 1, n_trials))

      # Loop over instrument strenghs
      for j, eta in enumerate(etas):

          # Simulate system
          A, X, Z = simulate_neurons_iv(n_neurons, timesteps, eta, trial)

          # Compute IV estimate
          iv_V = get_iv_estimate_network(X, Z)

          # Compute correlation
          corr_data[trial, j] =  np.corrcoef(A.flatten(), iv_V.flatten())[1, 0]

  return corr_data

# Parameters of system
n_neurons = 20
timesteps = 10000
n_trials = 3
etas = [2, 1, 0.5, 0.25, 0.12]  # instrument strengths to search over

# Uncomment below to test your function
corr_data = instrument_strength_effect(etas, n_neurons, timesteps, n_trials)
with plt.xkcd():
  plot_performance_vs_eta(etas, corr_data)