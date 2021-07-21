
"""
1) More samples means the distribution starts to look more symmetric.

2) Increasing lambda moves the distribution along the x-axis, essentialy changing the
   mean of the distribution. With lambda = 6 for example, we would expect to often see
   6 spike counts per interval.

3) It becomes asymmetric because the Poisson distribution is restricted to non-negative counts
   (you can't have negative numbers of spikes)
"""