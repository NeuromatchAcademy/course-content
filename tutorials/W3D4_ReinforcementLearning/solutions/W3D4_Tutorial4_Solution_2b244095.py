def dyna_q_model_update(model, state, action, reward, next_state):
  """ Dyna-Q model update

  Args:
    model (ndarray): An array of shape (n_states, n_actions, 2) that represents
                     the model of the world i.e. what reward and next state do
                     we expect from taking an action in a state.
    state (int): the current state identifier
    action (int): the action taken
    reward (float): the reward received
    next_state (int): the transitioned to state identifier

  Returns:
    ndarray: the updated model
  """
  # Update our model with the observed reward and next state
  model[state, action] = reward, next_state

  return model