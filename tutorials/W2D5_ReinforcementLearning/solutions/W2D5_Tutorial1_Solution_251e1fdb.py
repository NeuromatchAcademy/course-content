"""
The multi-reward and probabilistic reward enviroments are the same. You 
could simulate a probablalistic reward of 10 units, delivered 50% of the time, 
by having a mixture of 10 and 0 unit rewards, or vice versa.

Large values of alpha prevent the TD Learner from converging. As a result, the 
value function seems implausible: one state may have an extremely low value while
the neighboring ones remain high. This pattern persists even if training continues 
for hundreds of thousands of trials.
""";