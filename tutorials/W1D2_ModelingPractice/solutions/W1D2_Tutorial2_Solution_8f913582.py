def my_worldmotion(vis, selfmotion, params):
    '''
    Estimates world motion based on the visual signal, the estimate of 

    Args:
        vis (numpy.ndarray): 1xM array with the optic flow signal
        selfmotion (float): estimate of self motion
        params (dict): dictionary with named entries:
            see my_train_illusion_model() for details

    Returns:
        (float): an estimate of world motion in m/s

    '''

    # 1. running window function
    # 2. take final value
    # 3. subtract selfmotion from value

    # return final value
    return output    