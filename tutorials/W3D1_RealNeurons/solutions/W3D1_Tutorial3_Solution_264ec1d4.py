
"""
Discussion:

1. We can push the neuron to spike almost like a Poisson neuron. Of course given
that there is a refractoriness it will never spike completely like a Poisson process.
Poisson type spike irregularity will be achieved when mean is small (far from the
spike threshold) and fluctuations are large. This will achieved when excitatory
and inhibitory rates are balanced -- i.e. ratio of exc and inh. spike rate is
constant as you vary the inout rate.

2. Firing rate will increase because fluctuations will increase as we increase
exc. and inh. rates. But if synapses are modelled as conductance as opposed to
currents, fluctuations may start decrease at high input rates because neuron time
constant will drop.

""";