
"""
In top-left A, both eigenvalues are imaginary (no real component, the two
eigenvalues are complex conjugate pairs), so the solutions are all stable
oscillations. The eigenvectors are also complex conjugate pairs (that's why
we see them plotted on top of each other). They point in the direction of the
major axis of the elliptical trajectories.

In the top-right A, both eigenvalues are positive, so they are growing. The larger
eigenvalue direction (red) grows faster than the other direction (blue),
so trajectories all eventually follow the red eigenvector direction. Those that
start close to the blue direction follow blue for a bit initially.

In the bottom-left A, both eigenvalues are negative, so they are both decaying.
All solutions decay towards the origin [0, 0]. The red eigenvalue is larger in
magnitude, so decay is faster along the red eigenvector.

In the bottm-right A, one eigenvalue is positive (red) and one eigenvalue is negative
(blue). This makes the shape of the landscape the shape of a saddle (named after
the saddle that one puts on a horse for a rider). Trajectories decay along the
blue eigenvector but grow along the red eigenvector.


""";