
"""
1)  The prior exerts a strong influence over the posterior when it is very informative: when
    the probability of the school being on one side or the other. If the prior that the fish are
    on the left side is very high (like 0.9), the posterior probability of the state being left is
    high regardless of the measurement.

2)  When the likelihoods are similar, the information gained from catching a fish or not is less informative.
    Intuitively, if you were about as likely to catch a fish regardless of the true location, then catching a fish
    doesn't tell you very much! The differences between the likelihoods is a way of thinking about how much information
    we can gain. You can try to figure out why, as we've given you all the clues...

3)  Similarly to the prior, the likelihood exerts the most influence when it is informative: when catching
    a fish tells you a lot of information about which state is likely. For example, if the probability of the
    fisherperson catching a fish if he is fishing on the right side and the school is on the left is 0
    (p fish | s = left) = 0 and the probability of catching a fish if the school is on the right is 1, the
     prior does not affect the posterior at all. The measurement tells you the hidden state completely.
"""