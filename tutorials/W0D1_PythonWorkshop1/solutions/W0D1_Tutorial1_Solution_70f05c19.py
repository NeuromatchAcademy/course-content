
# Initialize step_end
step_end = int(t_max / dt)

# Initialize v0
v = el

with plt.xkcd():
  # Initialize the figure
  plt.figure()
  plt.title('$V_m$ with sinusoidal I(t)')
  plt.xlabel('time (s)')
  plt.ylabel('$V_m$ (V)');

  # Loop for step_end steps
  for step in range(step_end):

    # Compute value of t
    t = step * dt

    # Compute value of i at this time step
    i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))

    # Compute v
    v = v + dt/tau * (el - v + r*i)

    # Plot v (using 'k.' to get even smaller markers)
    plt.plot(t, v, 'k.')

  # Display plot
  plt.show()