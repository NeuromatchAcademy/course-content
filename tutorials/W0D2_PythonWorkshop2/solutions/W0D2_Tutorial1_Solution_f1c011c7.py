
def ode_step(v, i, dt):
  """
  Evolves membrane potential by one step of discrete time integration
  
  Args:
    v (numpy array of floats)
      membrane potential at previous time step of shape (neurons)

    v (numpy array of floats)
      synaptic input at current time step of shape (neurons)

    dt (float)
      time step increment
            
  Returns:
    v (numpy array of floats)
      membrane potential at current time step of shape (neurons)
  """
  v = v + dt/tau * (el - v + r*i)

  return v

def spike_clamp(v, delta_spike):
  """
  Resets membrane potential of neurons if v>= vth 
  and clamps to vr if interval of time since last spike < t_ref
  
  Args:
    v (numpy array of floats)
      membrane potential of shape (neurons)

    delta_spike (numpy array of floats)
      interval of time since last spike of shape (neurons)
            
  Returns:
    v (numpy array of floats)
      membrane potential of shape (neurons)
    spiked (numpy array of floats)
      boolean array of neurons that spiked  of shape (neurons)      
  """ 
  # bolean array spiked indexes neurons with v>=vth
  spiked = (v >= vth)
  v[spiked] = vr

  # bolean array clamped indexes refractory neurons  
  clamped = (t_ref > delta_spike)
  v[clamped] = vr

  return v, spiked

# set random number generator
np.random.seed(2020)

# initialize step_end, t_range, n, v_n, syn and raster
t_range = np.arange(0, t_max, dt)
step_end = len(t_range)
n = 500
v_n = el * np.ones([n,step_end])
syn = i_mean * (1 + 0.1*(t_max/dt)**(0.5)*(2*np.random.random([n,step_end])-1))
raster = np.zeros([n,step_end])

# initialize t_ref and last_spike
mu = 0.01
sigma = 0.007
t_ref = mu + sigma*np.random.normal(size=n)
t_ref[t_ref<0] = 0

# initialize t_ref and last_spike
last_spike = -t_ref * np.ones([n])

# loop time steps
for step, t in enumerate(t_range):
  if step==0:
    continue

  v_n[:,step] = ode_step(v_n[:,step-1], syn[:,step], dt)

  v_n[:,step], spiked = spike_clamp(v_n[:,step], t - last_spike)

  # update raster and last_spike
  raster[spiked,step] = 1.
  last_spike[spiked] = t

# plot multiple realizations of Vm, spikes and mean spike rate
with plt.xkcd():
  plot_all(t_range, v_n, raster)