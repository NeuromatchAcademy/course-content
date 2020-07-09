

def my_selfmotion(ves, params):
    """
    Estimates self motion for one vestibular signal

    Args:
        ves (numpy.ndarray): 1xM array with a vestibular signal
        params (dict): dictionary with named entries:
            see my_train_illusion_model() for details

    Returns:
        (float): an estimate of self motion in m/s
    """

    # 1. integrate vestibular signal
    # 2. running window function
    # 3. take final value
    # 4. compare to threshold

    # if higher than threshold: return value
    # if lower than threshold: return 0
    return output