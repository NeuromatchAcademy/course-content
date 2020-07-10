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

    # integrate signal:
    ves = np.cumsum(ves * (1 / params['samplingrate']))

    # use running window to accumulate evidence:
    selfmotion = my_moving_window(ves, window=params['filterwindows'][0],
                                  FUN=params['FUN'])

    # final value:
    selfmotion = selfmotion[-1]

    # compare to threshold, set to 0 if lower
    if selfmotion < params['threshold']:
        selfmotion = 0
    else:
        selfmotion = 1

    return selfmotion