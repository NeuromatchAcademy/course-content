
# set random number generator
np.random.seed(2020)

# initialize step_end, t_range, n, v_n and syn
t_range = np.arange(0, t_max, dt)
step_end = len(t_range)
n = 500
v_n = el * np.ones([n, step_end])
syn = i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * (2 * np.random.random([n, step_end]) - 1))

# initialize spikes and spikes_n
spikes = {j: [] for j in range(n)}
spikes_n = np.zeros([step_end])

# loop time steps
for step, t in enumerate(t_range):
  if step==0:
    continue

  v_n[:, step] = v_n[:, step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r*syn[:, step])

  # collect spike times and reset to resting potential
  for j in range(0, n):
    if v_n[j, step] >= vth:
      v_n[j, step] = vr
      spikes[j] += [t]
      spikes_n[step] += 1

# collect mean Vm and mean spiking rate
v_mean = np.mean(v_n, axis=0)
spikes_mean =  spikes_n / n

# initialize the figure
with plt.xkcd():
  plt.figure()

  # collect axis of 1st figure in ax1
  ax1 = plt.subplot(3, 1, 1)
  for j in range(n):
    plt.scatter(t_range, v_n[j], color="k", marker=".", alpha=0.01)
  plt.plot(t_range, v_mean, 'C1', alpha=0.8, linewidth=3)
  plt.ylabel('$V_m$ (V)')

  # share xaxis with 1st figure
  plt.subplot(3, 1, 2, sharex=ax1)
  # for each neuron j: collect spike times and plot them at height j
  for j in range(n):
    times = np.array(spikes[j])
    plt.scatter(times, j * np.ones_like(times), color="C0", marker=".", alpha=0.2)
  plt.ylabel('neuron')

  # share xaxis with 1st figure
  plt.subplot(3, 1, 3, sharex=ax1)
  plt.plot(t_range, spikes_mean)
  plt.xlabel('time (s)')
  plt.ylabel('rate (Hz)')

  plt.tight_layout()
  plt.show()