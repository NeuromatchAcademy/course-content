def my_train_illusion_model(sensorydata, params):
    '''
    Generate predictions of perceived self motion and perceived world motion 
    based on the visual and vestibular signals. 
    
    Args:

        sensorydata: (dict) dictionary with two named entries:
            opticalfow: (numpy.ndarray of float) NxM array with N trials on rows
            and M visual signal samples in columns 

        vestibular: (numpy.ndarray of float) NxM array with N trials on rows and 
            M vestibular signal samples in columns
      
        params: (dict) dictionary with named entries:
            threshold: (float) vestibular threshold for credit assignment

            filterwindow: (list of int) determines the strength of filtering for
                the visual and vestibular signals, respectively

            integrate (bool): whether to integrate the vestibular signals, will 
                be set to True if absent

            FUN (function): function used in the filter, will be set to 
                np.mean if absent

            samplingrate (float): the number of samples per second in the 
                sensory data, will be set to 10 if absent

    Returns:

      dict with two entries:

        selfmotion: (numpy.ndarray) vector array of length N, with predictions
            of perceived self motion 
            
        worldmotion: (numpy.ndarray) vector array of length N, with predictions
            of perceived world motion 
    '''

    # sanitize input a little
    if not('FUN' in params.keys()):
        params['FUN'] = np.mean
    if not('integrate' in params.keys()):
        params['integrate'] = True
    if not('samplingrate' in params.keys()):
        params['samplingrate'] = 10

    # number of trials:
    ntrials = sensorydata['opticflow'].shape[0]
    
    # set up variables to collect output
    selfmotion = np.empty(ntrials)
    worldmotion = np.empty(ntrials)

    # loop through trials
    for trialN in range(ntrials):
        vis = sensorydata['opticflow'][trialN,:]
        ves = sensorydata['vestibular'][trialN,:]
        
        ########################################################
        # get predicted perception in respective output vectors:
        ########################################################
        
        selfmotion[trialN], worldmotion[trialN] = my_perceived_motion( vis=vis, ves=ves, params=params)
        
    return {'selfmotion':selfmotion, 'worldmotion':worldmotion}

# here is a mock version of my_perceived motion
# now you can test my_train_illusion_model()
def my_perceived_motion(*args, **kwargs):
    return np.random.rand(2)

##let's look at the preditions we generated for n=2 sample trials (0,100)
##we should get a 1x2 vector of self-motion prediction and another for world-motion
sensorydata={'opticflow':opticflow[[0,100],:0], 'vestibular':vestibular[[0,100],:0]}
params={'threshold':0.33, 'filterwindow':[100,50]}
my_train_illusion_model(sensorydata=sensorydata, params=params)