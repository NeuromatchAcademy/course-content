def random_walk_simulator(N, T, mu=0, sigma=1):
    '''Simulate N random walks for T time points. At each time point, the step
       is drawn from a Gaussian distribution with mean mu and standard deviation
       sigma.

    Args:
      T (integer) : Duration of simulation in time steps
      N (integer) : Number of random walks
      mu (float) : mean of step distribution
      sigma (float) : standard deviation of step distribution

    Returns:
      (numpy array) : NxT array in which each row corresponds to trajectory
    '''
    # generate all the random steps for all steps in all simulations in one go
    # produces a N x T array
    steps = np.random.normal(mu, sigma, size=(N, T))

    # compute the cumulative sum of all the steps over the time axis
    sim = np.cumsum(steps, axis=1)

    return sim

np.random.seed(2020) # set random seed

# simulate 1000 random walks for 10000 time steps
sim = random_walk_simulator(1000, 10000,  mu=0, sigma=1)

# take a peek at the first 10 simulations
with plt.xkcd():
  plot_random_walk_sims(sim, nsims=10)