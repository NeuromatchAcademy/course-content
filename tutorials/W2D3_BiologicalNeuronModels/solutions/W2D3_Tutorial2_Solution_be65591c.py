
"""
Discussion:

1. Anything that tries to reduce the mean or variance of the input e.g. mean can
be reduced by inhibition, sigma can be reduced by the membrane time constant.
Obviously, if the two neurons have different parameters that will decorrelate them.
But more importantly, it is the slope of neuron transfer function that will affect the
output correlation.

2. These observations pose an interesting problem at the network level. If the
output correlation are smaller than the input correlation, then the network activity
should eventually converge to zero correlation. But that does not happen. So there
is something missing in this model to understand origin of synchrony in the network.

3. For spike trains, we do not have explicit control over mu and sigma but these
two variables will be tied to the firing rate of the inputs. So the
results will be qualitatively similar. But when we think of multiple spike inputs
two different types of correlations arise (see Bujan et al. 2015 for more info)
""";