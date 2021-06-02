
#. 1)  We see that the posterior is a weighted average of the prior and likelihood,
#.     where the weights correspond to the information in each (or inverse variance).
#.     That is, if the prior has lower variance, the mean of the posterior is pulled
#.     towards it. If the likelihood has lower variance, the mean of the posterior is
#.     pulled towards it

#. 2)  When we simply multiplied the Gaussians, we end up with an a true Probability
#.     Density Function (PDF)--that is, the integral under the curve is one. However,
#.     when we calculate the likelihood * prior, it will look like a Gaussian, but it
#.     must be normalized by the marginal likelihood so that the posterior is a true
#.     PDF.

#. 3) The prior and posterior can both be thought of as having information, as we
#.    described earlier. So this means you can think of the weighting applied to each
#.    as proportional to the amount of information each contain. For Gaussians, you
#.    know how to calculate this directly.