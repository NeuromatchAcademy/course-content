
# set random number generator
np.random.seed(2020)

# initialize step_end, t_range, v and syn
step_end = int(t_max / dt)
t_range = np.linspace(0, t_max, num=step_end)
v = el * np.ones(step_end + 1)
syn = i_mean * (1 + 0.1 * (t_max/dt) ** (0.5) * (2 * np.random.random(step_end) - 1))

# loop for step_end - 1 steps
for step in range(step_end):

  v[step + 1] = v[step] + (dt / tau) * (el - v[step] + r * syn[step])

with plt.xkcd():
  # initialize the figure
  plt.figure()
  plt.title('$V_m$ with random I(t)')
  plt.xlabel('time (s)')
  plt.ylabel(r'$V_m$ (V)')

  plt.plot(t_range, v[:-1], 'k.')
  plt.show()
