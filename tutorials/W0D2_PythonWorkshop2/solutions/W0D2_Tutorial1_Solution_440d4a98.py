
def ode_step(v, i):

  return v + dt/tau * (el - v + r*i)

def clamp(v, last, t):

  clamped = (last + t_ref > t)
  v[clamped] = vr

  return v

def spike(v, raster, last, t):

  spiked = (v >= vth)
  v[spiked] = vr
  raster[spiked] = 1.
  last[spiked] = t

  return v, raster, last

def run_simulation(syn, t_range, t_ref):

  v_n = el * np.ones([n,step_end])
  raster = np.zeros([n,step_end])
  last_spike = -t_ref * np.ones([n])

  # loop for step_end - 1 steps
  for step in range(1, step_end):
    t = t_range[step]

    v_n[:,step] = ode_step(v_n[:,step-1], syn[:,step])

    v_n[:,step], raster[:,step], last_spike = \
      spike(v_n[:,step], raster[:,step], last_spike, t)

    v_n[:,step] = clamp(v_n[:,step], last_spike, t)

  return v_n, raster

# set random number generator
np.random.seed(2020)

# initialize step_end, n, t_range, and syn
step_end = int(t_max/dt)
n = 500
t_range = np.linspace(0, t_max, num=step_end)
syn = i_mean * (1 + 0.1*(t_max/dt)**(0.5)*(2*np.random.random([n,step_end])-1))

# initialize t_ref and last_spike
mu = 0.01
sigma = 0.007
t_ref = mu + sigma*np.random.normal(size=n)
t_ref = np.clip(t_ref, 0, t_ref.max())

# run simulation
v_n, raster = run_simulation(syn, t_range, t_ref)

# plot multiple realizations of Vm, spikes and mean spike rate
plot_all(t_range, v_n, raster)