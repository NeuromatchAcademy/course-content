def td_learner(env, n_trials, gamma=0.98, alpha=0.001):
  """ Temporal Difference learning

  Args:
    env (object): the environment to be learned
    n_trials (int): the number of trials to run
    gamma (float): temporal discount factor
    alpha (float): learning rate

  Returns:
    ndarray, ndarray: the value function and temporal difference error arrays
  """
  V = np.zeros(env.n_steps) # Array to store values over states (time)
  TDE = np.zeros((env.n_steps, n_trials)) # Array to store TD errors

  for n in range(n_trials):
    state = 0 # Initial state
    for t in range(env.n_steps):
      # Get next state and next reward
      next_state, reward = env.get_outcome(state)
      # Is the current state in the delay period (after CS)?
      is_delay = env.state_dict[state][0]

      # Write an expression to compute the TD-error
      TDE[state, n] = (reward + gamma * V[next_state] - V[state])

      # Write an expression to update the value function
      V[state] += alpha * TDE[state, n] * is_delay

      # Update state
      state = next_state

  return V, TDE


env = ClassicalConditioning(n_steps=40, reward_magnitude=10, reward_time=10)
V, TDE = td_learner(env, n_trials=20000)
with plt.xkcd():
  learning_summary_plot(V, TDE)