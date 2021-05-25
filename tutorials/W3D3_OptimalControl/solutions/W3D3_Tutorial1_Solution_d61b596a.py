def policy_threshold(threshold, belief, loc):
  """
  chooses whether to switch side based on whether the belief
      on the current site drops below the threshold

  Args:
    threshold (float): the threshold of belief on the current site,
                        when the belief is lower than the threshold, switch side
    belief (numpy array of float, 2-dimensional): the belief on the
                                                  two sites at a certain time
    loc (int) : the location of the agent at a certain time
                -1 for left side, 1 for right side

  Returns:
    act (string): "stay" or "switch"
  """
  # Write the if statement
  if belief[(loc + 1) // 2] <= threshold:
    # action below threshold
    act = "switch"
  else:
    # action above threshold
    act = "stay"

  return act


test_policy_threshold()