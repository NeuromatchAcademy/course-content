def sample_lds(n_timesteps, params, seed=0):
  """ Generate samples from a Linear Dynamical System specified by the provided
  parameters.

  Args:
  n_timesteps (int): the number of time steps to simulate
  params (dict): a dictionary of model paramters: (D, Q, H, R, mu_0, sigma_0)
  seed (int): a random seed to use for reproducibility checks

  Returns:
  ndarray, ndarray: the generated state and observation data
  """
  n_dim_state = params['D'].shape[0]
  n_dim_obs = params['H'].shape[0]

  # set seed
  np.random.seed(seed)

  # precompute random samples from the provided covariance matrices
  # mean defaults to 0
  mi = stats.multivariate_normal(cov=params['Q']).rvs(n_timesteps)
  eta = stats.multivariate_normal(cov=params['R']).rvs(n_timesteps)

  # initialize state and observation arrays
  state = np.zeros((n_timesteps, n_dim_state))
  obs = np.zeros((n_timesteps, n_dim_obs))

  # simulate the system
  for t in range(n_timesteps):
    # write the expressions for computing state values given the time step
    if t == 0:
      state[t] = stats.multivariate_normal(mean=params['mu_0'],
                                           cov=params['sigma_0']).rvs(1)
    else:
      state[t] = params['D'] @ state[t-1] + mi[t]

    # write the expression for computing the observation
    obs[t] = params['H'] @ state[t] + eta[t]

  return state, obs


state, obs = sample_lds(100, params)
print('sample at t=3 ', state[3])
with plt.xkcd():
  plot_kalman(state, obs, title='sample')