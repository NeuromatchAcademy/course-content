
def value_function(measurement, act, cost_sw):
  """
  value function

  Args:
    act (numpy array of string): length T with each element
                                  taking value "stay" or "switch"
    cost_sw (float): the cost of switching side

  Returns:
    value (float): expected utility per unit time
  """
  act_int = (act == "switch").astype(int)
  T = len(measurement)
  # Calculate the value function
  value = np.sum(measurement - act_int * cost_sw) / T

  return value

test_value_function()