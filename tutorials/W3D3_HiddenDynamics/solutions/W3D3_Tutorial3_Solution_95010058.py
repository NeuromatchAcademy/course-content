def read_collar(s, sigma_measurements):
  """ Compute the measurements of the noisy sensor attached to astrocat's collar

  Args:
    s (ndarray): astrocat's true position over time
    sigma_measurements (scalar): amount of noise in the sensor (standard deviation)

  Returns:
    ndarray: `m`: astrocat's position over time according to the sensor
  """

  # Initialize variables
  m = np.zeros(len(s))

  # For all time t, add white Gaussian noise with magnitude sigma_measurements
  # Consider that np.random.normal(mu, sigma) generates a random sample from
  # a gaussian with mean = mu and standard deviation = sigma

  for t in range(len(s)):

    # Read measurement
    m[t] = s[t] + np.random.normal(0, sigma_measurements)

  return m


# Set parameters
np.random.seed(0)
D = 0.9    # parameter in s(t)
T = 50      # total time duration
s0 = 5.     # initial condition of s at time 0
sigma_p = 2 # amount of noise in the actuators of astrocat's propulsion unit
sigma_measurements = 4 # amount of noise in astrocat's collar

# Simulate Astrocat
s = simulate(D, s0, sigma_p, T)

# Take measurement from collar
m = read_collar(s, sigma_measurements)

# Visualize
with plt.xkcd():
  plot_measurement(s, m, T)