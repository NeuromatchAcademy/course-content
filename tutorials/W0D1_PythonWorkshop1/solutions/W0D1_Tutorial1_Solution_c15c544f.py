
# Initialize step_end
step_end = 25

with plt.xkcd():
  # Initialize the figure
  plt.figure()
  plt.title('Synaptic Input $I(t)$')
  plt.xlabel('time (s)')
  plt.ylabel('$I$ (A)')

  # Loop for step_end steps
  for step in range(step_end):

    # Compute value of t
    t = step * dt

    # Compute value of i at this time step
    i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))

    # Plot i (use 'ko' to get small black dots (short for color='k' and marker = 'o'))
    plt.plot(t, i, 'ko')

  # Display the plot
  plt.show()