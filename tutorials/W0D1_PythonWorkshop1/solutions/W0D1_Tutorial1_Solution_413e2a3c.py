
# Set random number generator
np.random.seed(2020)

# Initialize step_end and v
step_end = int(t_max / dt)
v = el

with plt.xkcd():
  # Initialize the figure
  plt.figure()
  plt.title('$V_m$ with random I(t)')
  plt.xlabel('time (s)')
  plt.ylabel('$V_m$ (V)')

  # loop for step_end steps
  for step in range(step_end):

    # Compute value of t
    t = step * dt

    # Get random number in correct range of -1 to 1 (will need to adjust output of np.random.random)
    random_num = 2 * np.random.random() - 1

    # Compute value of i at this time step
    i =  i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * random_num)

    # Compute v
    v = v + dt/tau * (el - v + r*i)

    # Plot v (using 'k.' to get even smaller markers)
    plt.plot(t, v, 'k.')


  # Display plot
  plt.show()