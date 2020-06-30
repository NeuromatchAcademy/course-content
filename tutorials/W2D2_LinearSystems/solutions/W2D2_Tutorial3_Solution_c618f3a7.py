# simulate random walks
sim = random_walk_simulator(5000, 1000, mu=0, sigma=1)

# compute the mean and variance of trajectory positions at every time point
mu = np.mean(sim, axis=0)
var = np.var(sim, axis=0)

with plt.xkcd():
  plot_mean_var_by_timestep(mu, var)