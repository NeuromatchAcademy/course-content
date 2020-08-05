
def my_selfmotion(ves, params):
    """
    Estimates self motion for one vestibular signal

    Args:
        ves (numpy.ndarray): 1xM array with a vestibular signal
        params (dict)      : dictionary with named entries:
                             see my_train_illusion_model() for details

    Returns:
        (float)            : an estimate of self motion in m/s
    """

    # 1. integrate vestibular signal:
    ves = np.cumsum(ves * (1 / params['samplingrate']))

    # 2. running window function to accumulate evidence:
    selfmotion = my_moving_window(ves, window=params['filterwindows'][0])

    # 3. take final value of self-motion vector as our estimate
    selfmotion = selfmotion[-1]

    # 4. compare to threshold. Hint the threshodl is stored in
    # params['threshold']
    # if selfmotion is higher than threshold: return value
    # if it's lower than threshold: return 0

    if selfmotion < params['threshold']:
        selfmotion = 0

    return selfmotion