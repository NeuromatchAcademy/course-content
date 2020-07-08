
# initialize step_end and v
step_end = int(t_max / dt)
v = el

with plt.xkcd():
  # initialize the figure
  plt.figure()
  # loop for step_end steps
  for step in range(step_end):
    t = step * dt
    i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))
    plt.plot(t, v, 'k.')

    v = v + dt/tau * (el - v + r*i)

  t = t + dt
  plt.plot(t, v, 'k.')
  
  plt.title('$V_m$ with sinusoidal I(t)')
  plt.xlabel('time (s)')
  plt.ylabel(r'$V_m$ (V)')
  plt.show()