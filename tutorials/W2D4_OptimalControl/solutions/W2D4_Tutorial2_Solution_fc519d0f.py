class LDS:
  def __init__(self, T: int, ini_state: float, noise_var: float):
    self.T = T  # time horizon
    self.ini_state = ini_state
    self.noise_var = noise_var

  def dynamics(self, D: float):
    s = np.zeros(self.T)  # states initialization
    s[0] = self.ini_state
    noise = np.random.normal(0, self.noise_var, self.T)

    for t in range(self.T - 1):
      # calculate the state of t+1
      s[t + 1] = D * s[t] + noise[t]

    return s

  def dynamics_openloop(self, D: float, B: float, a: np.ndarray):

    s = np.zeros(self.T)  # states initialization
    s[0] = self.ini_state
    noise = np.random.normal(0, self.noise_var, self.T)

    for t in range(self.T - 1):
      # calculate the state of t+1
      s[t + 1] = D * s[t] + B * a[t] + noise[t]

    return s

  def dynamics_closedloop(self, D: float, B: float, L: np.ndarray):

    s = np.zeros(self.T)  # states initialization
    s[0] = self.ini_state
    noise = np.random.normal(0, self.noise_var, self.T)
    a = np.zeros(self.T - 1)

    for t in range(self.T - 1):
      # calculate the current action
      a[t] = L[t] * s[t]
      # calculate the next state
      s[t + 1] = D * s[t] + B * a[t] + noise[t]

    return s, a


test_lds_class(LDS)