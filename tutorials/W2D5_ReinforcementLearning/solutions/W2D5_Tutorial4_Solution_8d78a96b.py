def dyna_q_planning(model, value, params):
  """ Dyna-Q planning

  Args:
    model (ndarray): An array of shape (n_states, n_actions, 2) that represents
                     the model of the world i.e. what reward and next state do
                     we expect from taking an action in a state.
    value (ndarray): current value function of shape (n_states, n_actions)
    params (dict): a dictionary containing learning parameters

  Returns:
    ndarray: the updated value function of shape (n_states, n_actions)
  """
  # Perform k additional updates at random (planning)
  for _ in range(params['k']):
    # Find state-action combinations for which we've experienced a reward i.e.
    # the reward value is not NaN. The outcome of this expression is an Nx2
    # matrix, where each row is a state and action value, respectively.
    candidates = np.array(np.where(~np.isnan(model[:,:,0]))).T

    # Write an expression for selecting a random row index from our candidates
    idx = np.random.choice(len(candidates))

    # Obtain the randomly selected state and action values from the candidates
    state, action = candidates[idx]

    # Obtain the expected reward and next state from the model
    reward, next_state = model[state, action]

    # Update the value function using Q-learning
    value = q_learning(state, action, reward, next_state, value, params)

  return value