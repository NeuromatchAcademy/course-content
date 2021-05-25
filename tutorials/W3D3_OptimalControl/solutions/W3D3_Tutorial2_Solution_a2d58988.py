"""
In Demo 1.2, you should have seen that the optimal control gain (L = -0.45) takes a
short amount of time to get to the goal, and then stays there. We can try to get
to the goal in an even shorter time using an 'over-ambitious' control gain (L < -0.45), but
this may actually overshoot the goal and may cause oscillations in the system,
thus increasing the MSE. On the other hand, an 'under-ambitious' control gain
takes a longer time to get to the goal and thus increases the MSE.
Finally, at L>0, the system runs away to infinity.

Why is L=-D/B optimal for reaching our goal? Recall that our next state is
(D+B*L)*s[t] + noise. Plugging that L=-D/B causes that leading term to become zero,
which is our goal. Since the noise has zero mean, it's not possible to do any better!

""";