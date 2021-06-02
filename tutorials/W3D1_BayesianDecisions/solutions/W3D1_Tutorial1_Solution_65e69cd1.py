
# 1) The probability of a fish being silver is the joint probability of it being
#.     small and silver plus the joint probability of it being large and silver:
#
#.    P(Y = silver) = P(X = small, Y = silver) + P(X = large, Y = silver)
#.     = 0.4 + 0.1
#.     = 0.5


# 2) This is all the possibilities as in this scenario, our fish can only be small
#.   or large, silver or gold. So the probability is 1 - the fish has to be at
#.   least one of these.


#. 3) First we compute the marginal probabilities
#.  P(X = small) = P(X = small, Y = silver) + P(X = small, Y = gold) = 0.6
#.  P(Y = gold) = P(X = small, Y = gold) + P(X = large, Y = gold) = 0.5
#.   We already know the joint probability: P(X = small, Y = gold) = 0.2
#.   We can now use the given formula:
#.   P( X = small or Y = gold) = P(X = small) + P(Y = gold) - P(X = small, Y = gold)
#.   = 0.6 + 0.5 - 0.2
#.   = 0.9