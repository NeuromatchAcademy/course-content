
def value_function(measurement, act, cost_sw):
    """
    value function 
    """
    act_int = (act == "switch" ).astype(int)       # convert labels to binary
    T = len(measurement)   

    value = (np.sum(measurement) - np.sum(act_int) * cost_sw) / T     # rate of catching fish - costs

    return value
