
# simulation class
class NeuralSimulator:

  def __init__(self, n, t_max=0.15,
               dt=0.001, t_ref_mu = 0.01, t_ref_sigma = 0.002,
               tau=20e-3, el=-60e-3, vr=-70e-3, vth=-50e-3, 
               r=100e6, i_mean=25e-11
               ):
    self.n = n
    self.t_max = t_max
    self.dt = dt
    self.t_ref_mu = t_ref_mu
    self.t_ref_sigma = t_ref_sigma
    self.t_ref = self.t_ref_mu + self.t_ref_sigma*np.random.normal(size=self.n)
    self.t_ref = np.clip(self.t_ref, 0, self.t_ref.max())

    self.tau = tau        # second
    self.el = el          # milivolt
    self.vr = vr          # milivolt
    self.vth = vth        # milivolt
    self.r = r            # ohm
    self.i_mean = i_mean  # ampere

    self.step = 0
    self.step_end = int(t_max/dt)
    self.v_n = el * np.ones([self.n, self.step_end])
    self.syn = i_mean * (1 + 0.1*(self.t_max/self.dt)**(0.5)*(2*np.random.random([self.n,self.step_end])-1))
    self.raster = np.zeros([self.n,self.step_end])
    self.last_spike = -self.t_ref * np.ones([self.n])
    self.t_range = np.linspace(0, self.t_max, num=self.step_end)


  def ode_step(self):

    v = self.v_n[:,self.step-1]
    i = self.syn[:,self.step]
    
    self.v_n[:,self.step] = v + self.dt/self.tau * (self.el - v + self.r*i)


  def spike_clamp(self):

    v = self.v_n[:,self.step]
    t = self.t_range[self.step]

    spiked = (v >= self.vth)
    v[spiked] = self.vr
    self.raster[spiked, self.step] = 1.
    self.last_spike[spiked] = t

    clamped = (self.last_spike + t_ref > t)
    v[clamped] = self.vr

  def run(self):

    # loop for step_end - 1 steps
    for step in range(1, self.step_end):

      self.step = step
      self.ode_step()
      self.spike_clamp()


# initialize class
my_simulator = NeuralSimulator(500)

# simulation run
my_simulator.run()

# plot multiple realizations of Vm, spikes and mean spike rate
plot_all(my_simulator.t_range, my_simulator.v_n, my_simulator.raster)