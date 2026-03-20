
# Simulate random walks
np.random.seed(2020) # set random seed
sim = random_walk_simulator(5000, 1000, mu=0, sigma=1)

# Compute mean
mu = np.mean(sim, axis=0)

# Compute variance
var = np.var(sim, axis=0)

# Visualize
with plt.xkcd():
  plot_mean_var_by_timestep(mu, var)