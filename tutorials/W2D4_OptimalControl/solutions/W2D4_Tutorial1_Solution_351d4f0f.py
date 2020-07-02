
def policy_threshold(threshold, belief, loc):
    """
    chooses whether to switch side based on whether the belief on the current site drops below the threshold

    Parameters
    ----------
    threshold (float): the threshold of belief on the current site, 
                        when the belief is lower than the threshold, switch side 
    belief (numpy array of float, 2-dimensional): the belief on the two sites at a certain time
    loc (int) : the location of the agent at a certain time
                -1 for left side, 1 for right side

    Returns
    -------
    act (string): "stay" or ""switch
    """

    if belief[(loc + 1 ) // 2]  <= threshold:
        act = "switch"
    else:
        act = "stay"

    return act
  
def policy_lazy(belief, loc):
    """
    This function is a lazy policy where stay is also taken
    """
    act = "stay"

    return act
