# set random number generator
np.random.seed(2020)

# initialize step_end, t_range, v and syn
step_end = int(t_max / dt)
t_range = np.linspace(0, t_max, num=step_end)
v = el * np.ones(step_end)
syn = i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * (2 * np.random.random(step_end) - 1))

# loop for step_end values of syn
for step, i in enumerate(syn):
  # skip first iteration
  if step==0:
    continue
  v[step] = v[step - 1] + (dt / tau) * (el - v[step - 1] + r*i)

with plt.xkcd():
  # initialize the figure
  plt.figure()
  plt.title('$V_m$ with random I(t)')
  plt.xlabel('time (s)')
  plt.ylabel('$V_m$ (V)')

  plt.plot(t_range, v, 'k')
  plt.show()