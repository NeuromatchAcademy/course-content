def kalman_smooth(data, params):
  """ Perform Kalman smoothing (backward pass) on the data given the provided
  system parameters.

  Args:
    data (ndarray): a sequence of osbervations of shape(n_timesteps, n_dim_obs)    
    params (dict): a dictionary of model paramters: (F, Q, H, R, mu_0, sigma_0)

  Returns:
    ndarray, ndarray: the smoothed system means and noise covariance values
  """
  # pulled out of the params dict for convenience
  F = params['F']
  Q = params['Q']
  H = params['H']
  R = params['R']

  n_dim_state = F.shape[0]
  n_dim_obs = H.shape[0]
  
  # first run the forward pass to get the filtered means and covariances
  mu, sigma = kalman_filter(data, params)

  # initialize state mean and covariance estimates
  mu_hat = np.zeros_like(mu)
  sigma_hat = np.zeros_like(sigma)
  mu_hat[-1] = mu[-1]
  sigma_hat[-1] = sigma[-1]
  
  # smooth the data
  for t in reversed(range(len(data)-1)):
    sigma_pred = F @ sigma[t] @ F.T + Q  # sigma_pred at t+1
    J = sigma[t] @ F.T @ np.linalg.inv(sigma_pred)
    mu_hat[t] = mu[t] + J @ (mu_hat[t+1] - F @ mu[t])
    sigma_hat[t] = sigma[t] + J @ (sigma_hat[t+1] - sigma_pred) @ J.T 

  return mu_hat, sigma_hat


with plt.xkcd():
  smoothed_state_means, smoothed_state_covariances = kalman_smooth(obs, params)
  ax = plot_kalman(state[:,0],state[:,1],obs[:,0],obs[:,1], 
                filtered_state_means[:,0], filtered_state_means[:,1], "r", label="my kf-filter")
  _ = plot_kalman(state[:,0],state[:,1],obs[:,0],obs[:,1], 
                smoothed_state_means[:,0], smoothed_state_means[:,1], "b", label="my kf-smoothed", ax=ax)