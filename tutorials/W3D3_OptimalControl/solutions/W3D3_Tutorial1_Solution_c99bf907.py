
"""
In Interactive Demo 1, you should see the school of fish switch sides less often when `stay_prob` is high.

* If the fish have already been on one side for a long time, does that change the chances of them switching sides?

  No. The telegraph process or binary switching process is Markovian.
  That means that the probabilities of changes depend only on the *current* state.
  States from further in the past do not matter for the chances of switching sides.
  Staying longer in one side is not a statement about the current state, but rather about the past,
  so it's irrelevant for the chances of switching.


* For what values of `p_stay` is the fish location most and least predictable?

  When `p_stay` is 1 then the fish never move. But when `p_stay` is 0 then the fish *always* move,
  oscillating back and forth deterministically every discrete time step.
""";