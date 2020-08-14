# set random number generator
np.random.seed(2020)

# initialize step_end, n, t_range, v and syn
step_end = int(t_max / dt)
n = 50
t_range = np.linspace(0, t_max, num=step_end)
v_n = el * np.ones([n, step_end])
syn = i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * (2 * np.random.random([n, step_end]) - 1))

# loop for step_end - 1 steps
for step in range(1, step_end):
  v_n[:,step] = v_n[:,step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r * syn[:, step])

v_mean = np.mean(v_n, axis=0)
v_std = np.std(v_n, axis=0)

with plt.xkcd():
  # initialize the figure
  plt.figure()
  plt.title('Multiple realizations of $V_m$')
  plt.xlabel('time (s)')
  plt.ylabel('$V_m$ (V)')

  plt.plot(t_range, v_n[:-1].T, 'k', alpha=0.3)

  plt.plot(t_range, v_n[-1], 'k', alpha=0.3, label='V(t)')
  plt.plot(t_range, v_mean, 'C0', alpha=0.8, label='mean')
  plt.plot(t_range, v_mean+v_std, 'C7', alpha=0.8)
  plt.plot(t_range, v_mean-v_std, 'C7', alpha=0.8, label='mean $\pm$ std')

  plt.legend()
  plt.show()