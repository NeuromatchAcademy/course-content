def update_action_value(q, action, reward, alpha):
  """ Compute the updated action value given the learning rate and observed
  reward.

  Args:
    q (ndarray): an array of action values
    action (int): the action taken
    reward (float): the reward received for taking the action
    alpha (float): the learning rate

  Returns:
    float: the updated value for the selected action
  """
  # write an expression for the updated action value
  value = q[action] + alpha * (reward - q[action])
  return value


q = [-2, 5, 0, 1]
action = 2
print(f"Original q({action}) value = {q[action]}")
q[action] = update_action_value(q, 2, 10, 0.01)
print(f"Updated q({action}) value = {q[action]}")