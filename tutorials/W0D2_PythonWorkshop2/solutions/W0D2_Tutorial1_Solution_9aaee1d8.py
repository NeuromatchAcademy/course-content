
# Set random number generator
np.random.seed(2020)

# Initialize step_end, t_range, n, v_n and i
t_range = np.arange(0, t_max, dt)
step_end = len(t_range)
n = 500
v_n = el * np.ones([n, step_end])
i = i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * (2 * np.random.random([n, step_end]) - 1))

# Initialize spikes and spikes_n
spikes = {j: [] for j in range(n)}
spikes_n = np.zeros([step_end])

# Loop over time steps
for step, t in enumerate(t_range):

  # Skip first iteration
  if step==0:
    continue

  # Compute v_n
  v_n[:, step] = v_n[:, step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r*i[:, step])

  # Loop over simulations
  for j in range(n):

    # Check if voltage above threshold
    if v_n[j, step] >= vth:

      # Reset to reset voltage
      v_n[j, step] = vr

      # Add this spike time
      spikes[j] += [t]

      # Add spike count to this step
      spikes_n[step] += 1

# Collect mean Vm and mean spiking rate
v_mean = np.mean(v_n, axis=0)
spikes_mean =  spikes_n / n

with plt.xkcd():
  # Initialize the figure
  plt.figure()

  # Plot simulations and sample mean
  ax1 = plt.subplot(3, 1, 1)
  for j in range(n):
    plt.scatter(t_range, v_n[j], color="k", marker=".", alpha=0.01)
  plt.plot(t_range, v_mean, 'C1', alpha=0.8, linewidth=3)
  plt.ylabel('$V_m$ (V)')

  # Plot spikes
  plt.subplot(3, 1, 2, sharex=ax1)
  # for each neuron j: collect spike times and plot them at height j
  for j in range(n):
    times = np.array(spikes[j])
    plt.scatter(times, j * np.ones_like(times), color="C0", marker=".", alpha=0.2)

  plt.ylabel('neuron')

  # Plot firing rate
  plt.subplot(3, 1, 3, sharex=ax1)
  plt.plot(t_range, spikes_mean)
  plt.xlabel('time (s)')
  plt.ylabel('rate (Hz)')

  plt.tight_layout()