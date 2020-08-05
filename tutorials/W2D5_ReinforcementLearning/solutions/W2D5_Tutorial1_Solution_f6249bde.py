"""
Alpha determines how fast the model learns. In the simple, deterministic world
we're using here, this allows the moodel to quickly converge onto the "true"
model that heavily values the conditioned stimulus. In more complex environments,
however, excessively large values of alpha can slow, or even prevent, learning,
as we'll see later.

Gamma effectively controls how much the model cares about the future: larger values of
gamma cause the model to weight future rewards nearly as much as present ones. At gamma=1,
the model weights all rewards, regardless of when they occur, equally and when greater than one, it
starts to *prefer* rewards in the future, rather than the present (this is rarely good).
When gamma=0, however, the model becomes greedy and only considers rewards that
can be obtained immediately.
 """;