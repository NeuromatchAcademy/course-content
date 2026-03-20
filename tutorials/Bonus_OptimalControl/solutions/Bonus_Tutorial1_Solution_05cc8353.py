
"""
* What happens when the fish and the agent (you!) are on the same or different locations?
  You catch fish with different probabilities.

* Where do you catch the most fish?
  When you're on the same side as the fish -- as long as high_rew_prob > low_rew_prob.

* Why isn't low_rew_prob + high_rew_prob = 1? What do these probabilities mean in the fishing story?
  These are not probabilities of mutually exclusive events. They are chances of one event (you catch fish)
  under two different conditions (you and the school of fish are on the same side or different sides).

* You _can_ move the sliders so `low_rew_prob > high_rew_prob`. This doesn't change the math,
  but it can change whether the math is a reasonable model of the physical problem. Why?
  It would be weird if you caught less fish when you're on the same side as the fish.
  But hey, maybe the fish warn each other when they're in a school together! Then they'd be harder to catch...
""";