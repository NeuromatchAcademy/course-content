n_neurons = 40 # the size of the system
timesteps = 20000
random_state = 42
eta = 2 # the strength of our instrument

A, X, Z = simulate_neurons_iv(n_neurons, timesteps, eta, random_state)

# solution
observed_ratio = [1, 0.8, 0.6, 0.4, 0.2]

with plt.xkcd():
  compare_iv_estimate_to_regression(observed_ratio)