
#. 1) If we do not use a Gaussian prior, we will not necessarily have a Gaussian
#.    posterior as the type of posterior distribution depends on the types of both the
#.    prior and likelihood distributions.

#. 2) A flat prior means you have no helpful prior information coming in: all options are
#.    equally likely.

#. 3) The Gamma prior has skew, which is the property of not being symmetric, so, like the
#.    mixture of Gaussians, it has different mean, median and mode. But unlike all the other
#.    distributions, the Gamma PDF is positive only for x > 0, so it has a hard truncation,
#.    even when its parameters cause the values just above x = 0 to be large. In fact, the
#.    the Exponential distribution, Erlang distribution, and chi-square distribution are
#.    special cases of the gamma distribution. In our example, you can see that the posterior
#.    also incoreporates the hard truncation.

#. 4) We have only changed the prior, but the prior and the likelihood are just probability
#.    distributions. In principle, they can be any properly defined probability distribution.
#.    An example that may seem bizare is the Driac (delta) function, which is a PDF, that has
#.    all it's probability density in one location, desite being continuous. But in the case
#.    of the brain, it's possible that strange likelihood distributions could be used. However,
#.    for the same reasons we, as scientists, like exponential family distributions, it may be
#.    that evolution selected only ways of representing probability distributions that had useful
#.    properties.