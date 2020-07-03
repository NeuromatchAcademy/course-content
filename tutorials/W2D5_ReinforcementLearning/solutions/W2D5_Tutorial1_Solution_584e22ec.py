
env = ProbabilisticCC(n_steps, reward_magnitude=10, reward_time=10, p_reward=0.8)
def td_reset_learner(env, n_trials, alpha=0.25, gamma=0.98):
  V = np.zeros(env.n_steps)
  TDE_reset = np.zeros((env.n_steps, n_trials))

  for n in range(n_trials):
    state = 0
    reset = False
    
    for t in range(env.n_steps):

        next_state, reward = env.get_outcome(state)
        is_delay  = env.state_dict[state][0]
        
        ########################################################################
        # Insert your code here to convert your TD learner into TD-reset
        # Hint: you can reuse much of your previous work. 
        TDE_reset[state] = reward + gamma * V[next_state] - V[state]
        
        if reset == True:
            TDE[state] = 0

        if reward:
            reset = True
        
        V[state] += alpha * TDE_reset[state,n] * is_delay
        #raise NotImplementedError("Student excercise: need to implement Value update")
        ########################################################################
            
        state = next_state

  return V, TDE_reset

V_reset, TDE_reset = td_reset_learner(env, n_trials)
learning_summary_plot(V_reset, TDE_reset)