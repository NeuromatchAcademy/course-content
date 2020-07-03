env = ClassicalConditioning(n_steps, reward_magnitude, reward_time) # Initialize the environment with n_steps; CS is presented ~1/4 along the way (e.g. for n_steps=10, CS is presented at t=9)

def td_learner(env, n_trials, gamma=0.98, alpha=0.001):
  V = np.zeros(env.n_steps) # Array to store values over states (time)
  TDE = np.zeros((env.n_steps, n_trials)) # Array to store TD errors

  for n in range(n_trials):
    
    state = 0 # Initial state
    for t in range(n_steps):

        next_state, reward = env.get_outcome(state) # Get next state and next reward
        is_delay  = env.state_dict[state][0] # Is the current state in the delay period (after CS)?
        ########################################################################
        # Insert code to calculate the TD-error.
        # Hint: This is the reward prediction *error*. When would we expect to see a reward?
        #  Comment out the last line in this block when you're done.
        TDE[state, n] = (reward + gamma * V[next_state] - V[state]) 
        # raise NotImplementedError("Student excercise: need to implement RPE")
        #################################################################################
        
        ########################################################################
        ## Insert code to update the Value Function V(st) below.
        #  Comment out the last line in this block when you're done.
        #  Hint: use the TD error you calculated above.
        V[state] += alpha * TDE[state, n] * is_delay
        #  raise NotImplementedError("Student excercise: need to implement Value update")
        #################################################################################
        state = next_state # Update state

  return V, TDE

V, TDE = td_learner(env, 20000)

with plt.xkcd():
  learning_summary_plot(V, TDE)