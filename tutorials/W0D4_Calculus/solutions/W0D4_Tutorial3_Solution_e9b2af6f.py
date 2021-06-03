
def Euler_Linear_System_Matrix(t, dt, w_EE=1):
  """
  Args:
    time: time
    dt: time-step
    w_EE: Excitation to excitation weight
  Returns:
    r_E: Excitation Firing Rate
    r_I: Inhibition Firing Rate
    N_Er: Nullclines for drE/dt=0
    N_Ir: Nullclines for drI/dt=0
  """

  tau_E = 100
  tau_I = 120
  n = len(t)
  r_I = 20*np.ones(n)
  r_E = 30*np.ones(n)
  w_EI = -5
  w_IE = 0.6
  w_II = -1

  for i in range(n-1):

    # Calculate the derivatives of the E and I populations
    drE = (w_EI*r_I[i] + w_EE*r_E[i]) / tau_E
    r_E[i+1] = r_E[i] + dt*drE

    drI = (w_II*r_I[i] + w_IE*r_E[i]) / tau_I
    r_I[i+1] = r_I[i] + dt*drI


  N_Er = -w_EE / w_EI*r_E
  N_Ir = -w_IE / w_II*r_E

  return r_E, r_I, N_Er, N_Ir


dt = 0.1 # time-step
t = np.arange(0, 1000, dt)
r_E, r_I, _, _ = Euler_Linear_System_Matrix(t, dt)
plot_rErI(t, r_E, r_I)