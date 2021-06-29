
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

  for k in range(n-1):
    dV = (-(V[k] - E_L) + R_m*I[k]) / tau_m
    V[k+1] = V[k] + dt*dV

    # Discontinuity for Spike
    if V[k] > V_th:
      V[k] = 0
      V[k+1] = V_reset
      t_isi = time[k]
      Spike = Spike + 1
      Spike_time = np.append(Spike_time, time[k])

  return Spike, Spike_time, V

# Set up time step and current
dt = 1
t = np.arange(0, 1000, dt)
I = np.sin(4 * 2 * np.pi * t/1000) + 2

# Model integrate and fire neuron
Spike, Spike_time, V = Euler_Integrate_and_Fire(I, t, dt)

# Visualize
with plt.xkcd():
  plot_IF(t, V,I,Spike_time)