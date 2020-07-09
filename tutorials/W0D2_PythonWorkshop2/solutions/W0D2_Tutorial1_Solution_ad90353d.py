
# set random number generator
np.random.seed(2020)

# initialize step_end, t_range, n, v_n and syn
t_range = np.arange(0, t_max, dt)
step_end = len(t_range)
n = 500
v_n = el * np.ones([n,step_end])
syn = i_mean * (1 + 0.1*(t_max/dt)**(0.5)*(2*np.random.random([n,step_end])-1))

# initialize spikes and spikes_n
spikes = {j: [] for j in range(n)}
spikes_n = np.zeros([step_end])

# loop time steps
for step, t in enumerate(t_range):
  if step==0:
    continue

  v_n[:,step] = v_n[:,step-1] + dt/tau * (el - v_n[:,step-1] + r*syn[:,step])

  # collect neurons that spiked and reset to resting potential
  spiked = (v_n[:,step] >= vth)
  v_n[spiked,step] = vr

  # collect spike times
  for j in np.where(spiked)[0]:
    spikes[j] += [t]
    spikes_n[step] += 1

# collect mean spiking rate
spikes_mean = spikes_n / n

# plot multiple realizations of Vm, spikes and mean spike rate
with plt.xkcd():
  plot_all(t_range, v_n, spikes=spikes, spikes_mean=spikes_mean)