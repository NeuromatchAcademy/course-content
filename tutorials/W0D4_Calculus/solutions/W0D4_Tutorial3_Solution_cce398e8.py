
def Euler_Simple_Linear_System(t, dt):
  """
  Args:
    time: time
    dt: time-step
  Returns:
    r_E: Excitation Firing Rate
    r_I: Inhibition Firing Rate
  """

  tau_E = 100
  tau_I = 120
  n = len(t)
  r_I = 20*np.ones(n)
  r_E = 30*np.ones(n)

  for i in range(n-1):
    dr_E = -r_I[i]/tau_E
    r_E[i+1] = r_E[i] + dt*dr_E

    dr_I = r_E[i]/tau_I
    r_I[i+1] = r_I[i] + dt*dr_I

  return r_E, r_I


dt = 0.1 # time-step
t = np.arange(0, 1000, dt)
r_E, r_I = Euler_Simple_Linear_System(t, dt)
plot_rErI(t, r_E, r_I)