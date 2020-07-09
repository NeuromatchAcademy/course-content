
# set random number generator
np.random.seed(2020)

# initialize step_end, t_range, n, v_n, syn and nbins
t_range = np.arange(0, t_max, dt)
step_end = len(t_range)
n = 10000
v_n = el * np.ones([n,step_end])
syn = i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * (2 * np.random.random([n, step_end]) - 1))
nbins = 32

# loop for step_end - 1 steps
for step, t in enumerate(t_range):
  if step==0:
    continue

  v_n[:, step] =  v_n[:, step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r*syn[:, step])

with plt.xkcd():

  # initialize the figure
  plt.figure()
  plt.ylabel('Frequency')
  plt.xlabel('$V_m$ (V)')

  plt.hist(v_n[:,int(step_end / 10)], nbins,
           histtype='stepfilled', linewidth=0,
           label = 't='+ str(t_max / 10) + 's')

  plt.hist(v_n[:, -1], nbins,
           histtype='stepfilled', linewidth=0,
           label = 't='+ str(t_max) + 's')
  
  plt.legend()
  plt.show()