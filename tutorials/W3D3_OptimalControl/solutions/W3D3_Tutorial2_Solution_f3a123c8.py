class LQR(LDS):
  def __init__(self, T, ini_state, noise_var):
    super().__init__(T, ini_state, noise_var)
    self.goal = np.zeros(T)  # The class LQR only supports g=0

  def control_gain_LQR(self, D, B, rho):
    P = np.zeros(self.T)  # Dynamic programming variable
    L = np.zeros(self.T - 1)  # control gain
    P[-1] = 1

    for t in range(self.T - 1):
        P_t_1 = P[self.T - t - 1]
        P[self.T - t-2] = (1 + P_t_1 * D**2 - D * P_t_1 * B / (
                rho + P_t_1 * B) * B**2 * P_t_1 * D)

        L[self.T - t-2] = - (1 / (rho + P_t_1 * B**2) * B * P_t_1 * D)
    return L

  def calculate_J_state(self, s:np.ndarray):
    # calculate the state
    J_state = np.sum((s - self.goal)**2)

    return J_state

  def calculate_J_control(self, a:np.ndarray):
    # calculate the control
    J_control = np.sum(a**2)

    return J_control


test_lqr_class(LQR)