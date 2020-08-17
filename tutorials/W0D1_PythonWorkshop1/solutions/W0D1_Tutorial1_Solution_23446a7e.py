# initialize step_end
step_end = 25

with plt.xkcd():
  # initialize the figure
  plt.figure()
  plt.title('Synaptic Input $I(t)$')
  plt.xlabel('time (s)')
  plt.ylabel('$I$ (A)')

  # loop for step_end steps
  for step in range(step_end):
    t = step * dt
    i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))
    plt.plot(t, i, 'ko')

  plt.show()