
"""
* Try a very high switching cost. What is the best threshold? How does that make sense?

  You should see that there is a best threshold:
  If it is too small, then you never move, missing opportunities to follow the fish.
  If it is too large, then you move too often and pay a large cost for the switching.
  When the switching cost is extremely high, it's never worth moving, so the optimal threshold is at zero.

* Try a zero switching cost. What's different?

  When the switching cost is zero, it's not best to always switch, but rather to follow
  the optimal inference about the fish location.

* Generally, how does the best threshold change with the switching cost?

  As the switching cost rises, the threshold should fall because
  you have even more incentive to avoid switches.
""";