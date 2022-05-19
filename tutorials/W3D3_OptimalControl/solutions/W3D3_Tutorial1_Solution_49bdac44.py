
def get_value(rewards, actions, cost_sw):
  """
  Args:
    rewards (numpy array of length T): whether a reward is obtained (1) or not (0) at each time step
    actions (numpy array of length T): action, "stay" or "switch", taken at each time step.
    cost_sw (float): the cost of switching to the other location

  Returns:
    value (float): expected utility per unit time
  """
  actions_int = (actions == "switch").astype(int)

  # Calculate the value function
  value = np.sum(rewards - actions_int * cost_sw) / len(rewards)

  return value


# Test your function
test_value_function()