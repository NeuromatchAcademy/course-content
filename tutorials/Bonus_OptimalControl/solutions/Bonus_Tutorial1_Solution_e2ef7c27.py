
"""
* Manipulate the slider for `stay_prob`. How well does the belief explain the dynamics of the fish as
  you adjust the probability of the fish staying in one location (`stay_prob`)?

  The parameter (`stay_prob`) determines fish dynamics. If it is low, the fish are moving fast
  and you don't have much time to collect observations that might decrease your uncertainty about
  the actual location of the school. If it is high, you have more time to integrate evidence
  and the belief explains better the dynamics of the fish.

* Explore the extreme case where `high_rew_prob = 1` and `low_rew_prob = 0`.
  Now play around with these sliders. How accurate is the belief as these parameters change?

  In the extreme case, the belief explains the dynamics of the fish perfectly because
  our observations are perfect, i.e., catching a fish indicates with certainty the presence of the school.
  If the chances of catching a fish are very different between the two sides, then you get a lot of information
  for each fish you catch. The belief will then rise and fall steeply with each observation.
  If the two probabilities are similar, then the belief will change slowly even if the fish move quickly.

* Under what conditions is it informative to catch a fish? What about to *not* catch a fish?

  The bigger the difference in the two probabilities, the more information you get from measurements.
  If both probabilities are low (and different), then you learn a lot from catching a fish.
  But you still learn a little if you don't catch anything, particularly when catching a fish is probable in one case.
""";