
def Euler_Integrate_and_Fire(I, time, dt):
  """
  Args:
    I: Input
    time: time
    dt: time-step
  Returns:
    Spike: Spike count
    Spike_time: Spike times
    V: membrane potential esitmated by the Euler method
  """

  Spike = 0
  tau_m = 10
  R_m = 10
  t_isi = 0
  V_reset = E_L = -75
  n = len(time)
  V = V_reset * np.ones(n)
  V_th = -50
  Spike_time = []

  for i in range(n-1):
    dV = (-(V[i] - E_L) + R_m*I[i]) / tau_m
    V[i+1] = V[i] + dt*dV

    # Discontinuity for Spike
    if V[i] > V_th:
      V[i] = 0
      V[i+1] = V_reset
      t_isi = time[i]
      Spike = Spike + 1
      Spike_time = np.append(Spike_time, time[i])

  return Spike, Spike_time, V