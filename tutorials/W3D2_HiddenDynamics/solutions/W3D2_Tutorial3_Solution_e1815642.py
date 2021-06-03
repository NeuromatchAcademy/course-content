def simulate_trajectory(D, s0, sigma_eta, T):
  """ Compute the response of the linear dynamical system.

  Args:
    D (scalar): dynamics multiplier
    s0 (scalar): initial postion
    sigma_eta (scalar): amount of noise in the system
    T (scalar): total duration of the simulation

  Returns:
    ndarray: `s`: astrocat's trajectory up to time T
  """

  # Initialize variables
  s = np.zeros(T + 1)
  s[0] = s0

  # Compute the position at time t given the position at time t-1 for all t
  # Consider that np.random.normal(mu, sigma) generates a random sample from
  # a gaussian with mean = mu and standard deviation = sigma

  for t in range(1, len(s)):

    s[t] = D*s[t-1] + np.random.normal(0, sigma_eta)

  return s

# Set random seed
np.random.seed(0)

# Choose parameters
D = -0.5    # parameter in f(x)
T = 10      # total Time duration
s0 = 5.     # initial condition of x at time 0
sigma_eta = 2 # amount of noise in the actuators of astrocat's propulsion unit

# Simulate trajectory
s = simulate_trajectory(D, s0, sigma_eta, T)

# Visualize
with plt.xkcd():
  plot_trajectory(s, T)