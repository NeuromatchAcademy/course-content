def epsilon_greedy(q, epsilon):
  """Epsilon-greedy policy: selects the maximum value action with probabilty
  (1-epsilon) and selects randomly with epsilon probability.

  Args:
    q (ndarray): an array of action values
    epsilon (float): probability of selecting an action randomly

  Returns:
    int: the chosen action
  """
  # write a boolean expression that determines if we should take the best action
  be_greedy = np.random.random() > epsilon
  if be_greedy:
    # write an expression for selecting the best action from the action values
    action = np.argmax(q)
  else:
    # write an expression for selecting a random action
    action = np.random.choice(len(q))

  return action


q = [-2, 5, 0, 1]
epsilon = 0.1
with plt.xkcd():
  plot_choices(q, epsilon, epsilon_greedy)