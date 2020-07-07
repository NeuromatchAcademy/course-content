
# set random number generator
np.random.seed(2020)

# initialize step_end and v
step_end = int(t_max/dt)
v = el
t = 0

with plt.xkcd():
  # initialize the figure
  plt.figure()
  plt.title('$V_m$ with random I(t)')
  plt.xlabel('time (s)')
  plt.ylabel(r'$V_m$ (V)')

  # loop for step_end steps
  for step in range(step_end):
    t = step * dt
    plt.plot(t, v, 'k.')

    i = i_mean * (1 + 0.1*(t_max/dt)**(0.5)*(2*np.random.random()-1))
    v = v + dt/tau * (el - v + r*i)

  plt.show()