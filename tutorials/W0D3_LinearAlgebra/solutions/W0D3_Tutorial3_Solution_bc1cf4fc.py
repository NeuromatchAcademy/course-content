
# 1) If both eigenvalues are above 1, the neural activities will eventually explode
#.   to infinity or negative infinity, depending on initial conditions. Tthe exact trajectory
#.   is drawn towards the eigenvector with the larger eigenvalue. This is because the larger eigenvalue
#.   will increasingly dominate the other one as it is raised to increasingly larger powers.

# 2) If both eigenvalues are below 1, the neural activity will eventually decay to 0.

#. 3) The activities will eventually explode to positive or negative infinity, unless
#.   the initial condition lies exactly on the eigenvector with the small eigenvalue. If the
#.   initial condition is near to that eigenvector, the trajectory will first go towards
#.   the origin before exploding.