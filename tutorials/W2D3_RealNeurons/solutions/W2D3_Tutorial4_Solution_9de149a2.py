def generate_P(pars, pre_spike_train_ex):
  """
  track of pre-synaptic spikes

  Args:
    pars               : parameter dictionary
    pre_spike_train_ex : binary spike train input from
                         presynaptic excitatory neuron

  Returns:
    P                  : LTP ratio
  """

  # Get parameters
  A_plus, tau_stdp = pars['A_plus'], pars['tau_stdp']
  dt, range_t = pars['dt'], pars['range_t']
  Lt = range_t.size

  # Initialize
  P = np.zeros(pre_spike_train_ex.shape)
  for it in range(Lt - 1):
    # Calculate the delta increment dP
    dP = -(dt / tau_stdp) * P[:, it] + A_plus * pre_spike_train_ex[:, it + 1]
    # Update P
    P[:, it + 1] = P[:, it] + dP

  return P


pars = default_pars_STDP(T=200., dt=1.)
pre_spike_train_ex = Poisson_generator(pars, rate=10, n=5, myseed=2020)
P = generate_P(pars, pre_spike_train_ex)
with plt.xkcd():
  my_example_P()