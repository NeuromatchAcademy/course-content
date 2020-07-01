
def control_policy_LQG(mean_estimated_state,control_gain):
    ## Code up the control action
    current_action =  control_gain * mean_estimated_state
    return current_action
  
    
def state_dynamics_LQG(D, B, process_noise_covariance, current_latent_state, current_action):
    ## Code up the state update with control input
    current_latent_state = np.dot(D, current_latent_state) + np.dot(B, current_action) + np.random.multivariate_normal(np.zeros(1),process_noise_covariance)
    return current_latent_state
