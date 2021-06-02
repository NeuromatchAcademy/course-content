dt = 0.5
t_rest = 0

t = np.arange(0, 1000, dt)

tau_m = 10
R_m = 10
V_reset = E_L = -75

I = 10

V = E_L + R_m*I + (V_reset - E_L - R_m*I) * np.exp(-(t)/tau_m)

with plt.xkcd():

  fig = plt.figure(figsize=(6, 4))
  plt.plot(t,V)
  plt.ylabel('V (mV)')
  plt.xlabel('time (ms)')
  plt.show()