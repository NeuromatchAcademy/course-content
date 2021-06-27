
# Set random number generator
np.random.seed(2020)

# Initialize t_range, step_end, n, v_n, i and nbins
t_range = np.arange(0, t_max, dt)
step_end = len(t_range)
n = 10000
v_n = el * np.ones([n, step_end])
i = i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * (2 * np.random.random([n, step_end]) - 1))
nbins = 32

# Loop over time steps
for step, t in enumerate(t_range):

  # Skip first iteration
  if step==0:
    continue

  # Compute v_n
  v_n[:, step] =  v_n[:, step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r * i[:, step])

# Initialize the figure
with plt.xkcd():
  plt.figure()
  plt.ylabel('Frequency')
  plt.xlabel('$V_m$ (V)')

  # Plot a histogram at t_max/10 (add labels and parameters histtype='stepfilled' and linewidth=0)
  plt.hist(v_n[:,int(step_end / 10)], nbins,
            histtype='stepfilled', linewidth=0,
            label = 't='+ str(t_max / 10) + 's')

  # Plot a histogram at t_max (add labels and parameters histtype='stepfilled' and linewidth=0)
  plt.hist(v_n[:, -1], nbins,
            histtype='stepfilled', linewidth=0,
            label = 't='+ str(t_max) + 's')
  # Add legend
  plt.legend()
  plt.show()