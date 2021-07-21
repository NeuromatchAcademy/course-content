def system(t, x, a00, a01, a10, a11):
    '''
    Compute the derivative of the state x at time t for a linear
    differential equation with A matrix [[a00, a01], [a10, a11]].

    Args:
      t (float): time
      x (ndarray): state variable
      a00, a01, a10, a11 (float): parameters of the system

    Returns:
      ndarray: derivative xdot of state variable x at time t
    '''

    # compute x1dot and x2dot
    x1dot = a00 * x[0] + a01 * x[1]
    x2dot = a10 * x[0] + a11 * x[1]

    return np.array([x1dot, x2dot])


# Set parameters
T = 6 # total time duration
dt = 0.1 # timestep of our simulation
A = np.array([[2, -5],
              [1, -2]])
x0 = [-0.1, 0.2]

# Simulate and plot trajectories
with plt.xkcd():
  plot_trajectory(system, [A[0,0],A[0,1],A[1,0],A[1,1]], x0, dt=dt, T=T)