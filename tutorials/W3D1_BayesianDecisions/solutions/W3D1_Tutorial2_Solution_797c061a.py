
# 1. The minimium of the different loss functions correspond to the mean, median,
#.   and mode of the posterior (just as in Interactive Demo 3). If we have a bi-modal
#.   prior, those properties of the posterior can be distinct.

#. 2. The posterior is just another probability distribution, so all the properies we
#.    saw in Interactive Demo 3, are true of the posterior two—-even though in this case,
#.    the posterior inherited the non-symetric properties from the prior. So, in this
#.    example, any prior that itself has a different mean, median and mode with also
#.    produce differents across their equivilant Loss functions.

#. 3. As long as the posterior probability densities are symetric around the true mean
#.    (hidden state), the MSE and ABS loss functions will look the same as for a Gaussian
#.    prior. The mean and the median are the same for symetric distributions. (When the
#.    mean exists--look up the Cauchy distributions.) The mode will be the same as the
#.    mean and median, when the distribution is unimodal (and therefor when the mixture
#.    means are the same. There can also be two modes with the mixture prior!