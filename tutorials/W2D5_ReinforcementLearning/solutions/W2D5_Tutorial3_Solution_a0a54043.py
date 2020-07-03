def q_learning(prev_state, action, reward, state, value, params):
  """Q-learning: updates the value function and returns it.
  
  Args:
    prev_state (int): the previous state identifier
    action (int): the action taken
    reward (float): the reward received
    state (int): the current state identifier
    value (ndarray): current value function of shape (n_states, n_actions)
    params (dict): a dictionary containing the default parameters
 
  Returns:
    ndarray: the updated value function of shape (n_states, n_actions)
  """
  # value of previous state-action pair
  prev_value = value[prev_state, action]

  # maximum Q-value at current state
  if state is None:
      max_value = 0
  else:
      max_value = np.max(value[state])
  
  # reward prediction error
  delta = reward + params['gamma'] * max_value - prev_value
  
  # update value of previous state-action pair
  value[prev_state, action] = prev_value + params['alpha'] * delta
  
  return value