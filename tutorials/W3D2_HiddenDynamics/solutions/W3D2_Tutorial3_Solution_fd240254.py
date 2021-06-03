
"""

1) When D is large, the state at time step t will depend heavily on the state at time
   step t_1. If we forget about the noise term, D = 2 would mean that the state at each
   time step is double the one before! So the state becomes huge and basically explodes towards
   infinity.

2) If D is a large negative number, the state at time t will be a different sign than the
   state at time step t_1. So the state will oscillate over the x axis.

3) When D is zero, the state at time t will not depend on the previous state, it will just
   be drawn from the noise distribution
"""