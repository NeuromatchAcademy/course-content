class LDS:
  """
    T: Length of timeline (global, fixed variable)
    standard_normal_noise: Global noise of length T drawn from N(0, 1)
    noise: Gaussian noise N(mean, var) = mean + sqrt(var) * standard_normal_noise
    ...
  """
  def __init__(self, ini_state: float, noise_var: float, static_noise=False):
    self.ini_state = ini_state
    self.noise_var = noise_var
    self.T = T
    self.static_noise = static_noise

  def dynamics(self, D: float):
    s = np.zeros(T)  # states initialization
    s[0] = self.ini_state
    if self.static_noise:
      noise = np.sqrt(self.noise_var) * standard_normal_noise
    else:
      noise = np.sqrt(self.noise_var) * np.random.randn(T)

    for t in range(T - 1):
      # calculate the state of t+1
      s[t + 1] = D * s[t] + noise[t]

    return s

  def dynamics_openloop(self, D: float, B: float, a: np.ndarray):

    s = np.zeros(T)  # states initialization
    s[0] = self.ini_state
    if self.static_noise:
      noise = np.sqrt(self.noise_var) * standard_normal_noise
    else:
      noise = np.sqrt(self.noise_var) * np.random.randn(T)

    for t in range(T - 1):
      # calculate the state of t+1
      s[t + 1] = D * s[t] + B * a[t] + noise[t]

    return s

  def dynamics_closedloop(self, D: float, B: float, L: np.ndarray):

    s = np.zeros(T)  # states initialization
    a = np.zeros(T - 1)
    s[0] = self.ini_state

    if self.static_noise:
      noise = np.sqrt(self.noise_var) * standard_normal_noise
    else:
      noise = np.sqrt(self.noise_var) * np.random.randn(T)

    for t in range(T - 1):
      # calculate the current action
      a[t] = L[t] * s[t]
      # calculate the next state
      s[t + 1] = D * s[t] + B * a[t] + noise[t]

    return s, a


# Test your function
test_lds_class(LDS)