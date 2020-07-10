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

# Use the updated function to run the model and plot the data
# Uncomment below to test your function 
data = {'opticflow': opticflow, 'vestibular': vestibular}
params = {'threshold': 0.33, 'filterwindows': [100, 50], 'FUN': np.mean}
modelpredictions = my_train_illusion_model(sensorydata=data, params=params)

predictions = np.zeros(judgments.shape)
predictions[:, 0:3] = judgments[:, 0:3]
predictions[:, 3] = modelpredictions['selfmotion']
predictions[:, 4] = modelpredictions['worldmotion'] * -1
with plt.xkcd():
  my_plot_percepts(datasets={'predictions': predictions}, plotconditions=False)    