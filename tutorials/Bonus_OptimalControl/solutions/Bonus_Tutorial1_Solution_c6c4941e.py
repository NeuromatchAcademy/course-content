
"""
* Qualitatively, how well does this policy follow the fish? What does it miss, and why?

  You generally follow the fish, but there can be a substantial difference in location.
  The belief is not generally very confident when the probabilities of catching fish on the
  two sides are not very different. Depending on your threshold, you might leave just
  from some unlucky times when you're still on the right side. Or you might stay even
  though you have not caught many fish, in the hopes that the fish haven't moved.

* How can you characterize the fishing strategy if the threshold is very low, or very high?

  If the threshold is low, you only switch when you have a very low belief that you're on the right side.
  Then you switch very rarely.
  If the threshold is high, then you switch whenever you're not extremely confident,
  so you change sides all the time.
""";