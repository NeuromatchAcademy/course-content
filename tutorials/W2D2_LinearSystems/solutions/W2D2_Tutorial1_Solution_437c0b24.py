def integrate_exponential(a, x0, dt, T):
  """Compute solution of the differential equation xdot=a*x with 
  initial condition x0 for a duration T. Use time step dt for numerical
  solution.
  
  Args:
    a (scalar): parameter of xdot (xdot=a*x)
    x0 (scalar): initial condition (x at time 0)
    dt (scalar): timestep of the simulation
    T (scalar): total duration of the simulation

  Returns:
    ndarray, ndarray: `x` for all simulation steps and the time `t` at each step
  """

  # Initialize variables
  t = np.arange(0, T, dt)
  x = np.zeros_like(t, dtype=complex)
  x[0] = x0

  # Step through system and integrate in time
  for k in range(1, len(t)):
    # for each point in time, compute xdot = a*x
    xdot = (a*x[k-1])

    # update x by adding xdot scaled by dt
    x[k] = x[k-1] +  xdot * dt

  return x, t

# choose parameters
a = -0.5    # parameter in f(x)
T = 10      # total Time duration
dt = 0.001  # timestep of our simulation
x0 = 1.     # initial condition of x at time 0

x, t = integrate_exponential(a, x0, dt, T)
with plt.xkcd():
  fig = plt.figure(figsize=(8, 6))
  plt.plot(t, x.real)  
  plt.xlabel('Time (s)')
  plt.ylabel('x')