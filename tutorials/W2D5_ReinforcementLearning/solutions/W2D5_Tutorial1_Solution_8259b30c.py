def td_reset_learner(env, n_trials, alpha=0.25, gamma=0.98):
  """ Temporal Difference learning with reset

  Args:
    env (object): the environment to be learned
    n_trials (int): the number of trials to run
    gamma (float): temporal discount factor
    alpha (float): learning rate
  
  Returns:
    ndarray, ndarray: the value function and temporal difference error arrays
  """
  V = np.zeros(env.n_steps)
  TDE_reset = np.zeros((env.n_steps, n_trials))

  for n in range(n_trials):
    state = 0
    reset = False
    
    for t in range(env.n_steps):
      next_state, reward = env.get_outcome(state)
      is_delay  = env.state_dict[state][0]

      # Write an expression to compute the TD-error using the TD-reset rule
      if reset:
        TDE_reset[state] = 0
      else:
        TDE_reset[state] = reward + gamma * V[next_state] - V[state]
      
      # Set reset flag if we receive a reward > 0
      if reward > 0:
        reset = True
      
      # Write an expression to update the value function
      V[state] += alpha * TDE_reset[state,n] * is_delay
      
      # Update state
      state = next_state

  return V, TDE_reset


env = ProbabilisticCC(n_steps=40, reward_magnitude=10, reward_time=10,
                      p_reward=0.8)
V_reset, TDE_reset = td_reset_learner(env, n_trials=20000)
with plt.xkcd():
  learning_summary_plot(V_reset, TDE_reset)