def kalman_filter(data, params):
  """ Perform Kalman filtering (forward pass) on the data given the provided
  system parameters.

  Args:
    data (ndarray): a sequence of osbervations of shape(n_timesteps, n_dim_obs)
    params (dict): a dictionary of model paramters: (D, Q, H, R, mu_0, sigma_0)

  Returns:
    ndarray, ndarray: the filtered system means and noise covariance values
  """
  # pulled out of the params dict for convenience
  D = params['D']
  Q = params['Q']
  H = params['H']
  R = params['R']

  n_dim_state = D.shape[0]
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
      mu_pred = D @ mu[t-1]
      sigma_pred = D @ sigma[t-1] @ D.T + Q

    # write the expression for computing the Kalman gain
    K = sigma_pred @ H.T @ np.linalg.inv(H @ sigma_pred @ H.T + R)
    # write the expression for computing the filtered state mean
    mu[t] = mu_pred + K @ (y - H @ mu_pred)
    # write the expression for computing the filtered state noise covariance
    sigma[t] = (I - K @ H) @ sigma_pred

  return mu, sigma


filtered_state_means, filtered_state_covariances = kalman_filter(obs, params)
with plt.xkcd():
  plot_kalman(state, obs, filtered_state_means, title="my kf-filter",
              color='r', label='my kf-filter')