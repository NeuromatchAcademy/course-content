
# 1).  The prior exerts a strong influence over the posterior when it is very informative: when
#.   the probability of the school being on one side or the other. If the prior that the fish are
#.   on the left side is very high (like 0.9), the posterior probability of the state being left is
#.   high regardless of the measurement.

# 2).  The prior does not exert a strong influence when it is not informative: when the probabilities
#.     of the school being on the left vs right are similar (both are 0.5 for example). In this case,
#.     the posterior is more driven  by the collected data (the measurement) and more closely resembles
#.     the likelihood.


#.  3) Similarly to the prior, the likelihood exerts the most influence when it is informative: when catching
#.    a fish tells you a lot of information about which state is likely. For example, if the probability of the
#.    fisherperson catching a fish if he is fishing on the right side and the school is on the left is 0
#.    (p fish | s = left) = 0 and the probability of catching a fish if the school is on the right is 1, the
#.    prior does not affect the posterior at all. The measurement tells you the hidden state completely.