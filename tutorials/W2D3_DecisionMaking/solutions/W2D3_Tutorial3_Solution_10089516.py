def kalman_filter(data, params):
  """ Perform Kalman filtering (forward pass) on the data given the provided
  system parameters.

  Args:
    data (ndarray): a sequence of osbervations of shape(n_timesteps, n_dim_obs)    
    params (dict): a dictionary of model paramters: (F, Q, H, R, mu_0, sigma_0)

  Returns:
    ndarray, ndarray: the filtered system means and noise covariance values
  """
  # pulled out of the params dict for convenience
  F = params['F']
  Q = params['Q']
  H = params['H']
  R = params['R']

  n_dim_state = F.shape[0]
  n_dim_obs = H.shape[0]
  I = np.eye(n_dim_state)  # identity matrix

  # state tracking arrays  
  mu = np.zeros((len(data), n_dim_state))
  sigma = np.zeros((len(data), n_dim_state, n_dim_state))

  # filter the data
  for t, y in enumerate(data):
    if t == 0:
      mu_pred = params['mu_0']
      sigma_pred = params['sigma_0']
    else:
      mu_pred = F @ mu[t-1]
      sigma_pred = F @ sigma[t-1] @ F.T + Q

    K = sigma_pred @ H.T @ np.linalg.inv(H @ sigma_pred @ H.T + R)
    mu[t] = mu_pred + K @ (y - H @ mu_pred)
    sigma[t] = (I - K @ H) @ sigma_pred
  
  return mu, sigma


with plt.xkcd():
    filtered_state_means, filtered_state_covariances = kalman_filter(obs, params)
    _ = plot_kalman(state[:,0],state[:,1],obs[:,0],obs[:,1], 
                    filtered_state_means[:,0], filtered_state_means[:,1], "r", title ="my kf-filter", label='my kf-filter')
    plt.axis('square');
    plt.tight_layout()