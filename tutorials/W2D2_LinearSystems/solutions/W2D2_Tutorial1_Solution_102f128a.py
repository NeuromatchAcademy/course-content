
"""
1) For a<0, the solution decays in time.
For a>0, the solution grows in time.
For a=0, the solution stays at 1 (and is stable).

2) For small-ish dt, the solution still looks the same.
As dt gets bigger, the solution starts to look choppier and is no longer smooth,
but still has mostly the right trends.
For a = 0.15, as dt gets above 0.7 or so, we start to see the forward Euler
integration start to actually break down. Specifically, the solution is no
longer decreasing monotonically and has developed an erroneous dip below zero.

The more general lesson is that, for each system, there is a dt threshold
above which the simulation introduces numerical artifacts and no longer behaves
as an accurate estimate of the true underlying system. We may tolerate some
choppiness in the solution, but eventually qualitatively wrong things creep in!
""";