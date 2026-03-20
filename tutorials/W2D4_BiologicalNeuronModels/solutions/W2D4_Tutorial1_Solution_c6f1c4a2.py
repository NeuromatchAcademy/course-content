
"""
1. Yes, it does. With DC input the F-I curve has a strong non-linearity but when
a neuron is driven with GWN, as we increase the $\sigma$ the non-linearity is
smoothened out. Essentially, in this case noise is acting to suppress the
non-linearities and render a neuron as a linear system.

2. (here is a short answer) When we increase the mean of the GWN, at some point
effective input mean is above the spike threshold and then the neuron operates
in the so called mean-driven regime -- as the input is so high all the neuron
is does is charge up to the spike threshold and reset. This essentially gives
almost regular spiking.

3. In an LIF, high firing rates are achieved for high GWN mean. Higher the mean,
higher the firing rate and lower the CV_ISI. So you will expect that as firing rate
increases, spike irregularity decreases. This is because of the spike threshold.
FOr a Poisson process there is no relationship between spike rate and spike
irregularity.
""";