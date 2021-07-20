
"""

* High switching cost means that you should be more certain that the other side
is better before committing to change sides. This means that beliefs must fall
below a threshold before acting. Conversely, a lower switching cost allows you
more flexibility to switch at less stringent thresholds. In the limit of _zero_
switching cost, you should always switch whenever you think the other side is
better, even if it's just 51%, and even if you switch every time step.
* Faster fish dynamics (lower `p_stay`) also promotes faster switching, because
you cannot plan as far into the future. In that case you must base your decisions
on more immediate evidence, but since you still pay the same switching cost that
cost is a higher fraction of your predictable rewards. And thus you should be more
conservative, and switch only when you are more confident.
* When `high_rew_p` and/or `low_rew_p` decreases, your predictions become less reliable,
 again encouraging you to require more confidence before committing to a switch.

"""