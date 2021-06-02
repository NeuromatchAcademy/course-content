def compute_rate_and_gain(I, a, theta, current_timestep):
  """ Compute rate and gain of neuron based on parameters

  Args:
    I (ndarray): different possible values of the current
    a (scalar): parameter of the transfer function
    theta (scalar): parameter of the transfer function
    current_timestep (scalar): the time we're using to take steps

  Returns:
    (ndarray, ndarray): rate and gain for each possible value of I
  """

  # Compute rate
  rate = (1+np.exp(-a*(I-theta)))**-1 - (1+np.exp(a*theta))**-1

  # Compute gain
  gain = numerical_derivative(rate, current_timestep)

  return rate, gain


current_timestep = 0.1
I = np.arange(0, 8, current_timestep)

# Neuron transfer function
a = 1.2     # You can change this value
theta = 5 # You can change this value

# Compute rate and gain
rate, gain = compute_rate_and_gain(I, a, theta, current_timestep)

# Visualize rate and gain

with plt.xkcd():
  plot_rate_and_gain(I, rate, gain)