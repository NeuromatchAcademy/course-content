
#.  1) No, no matter what parameters we choose for the Gaussian, the peak of the expected
#.    utility is the same. In other words, we would choose the same action (provide the same
#.    location estimate) for all 3 estimates.

#.  2) Yes, the peak of expected utility is in different locations for each loss when using
#.     a mixture of Gaussians distribution.

#.  3) When using mean-squared error, the peak is at the location of the mean. For
#.     absolute error, the peak is located at the median. And for zero-one loss, the
#.     peaks are at the two mode values.

#.  4) When a distribution has more than one maximum, it is multi-modal! This means
#.     it can have more than one mode. You will only ever have one mean and one median.