def get_granger_causality(X, neuron_idx, alpha=0.05):
    """
    Estimates the lag-1 granger causality of the given neuron on the other neurons in the system.

    Args:
        X (np.ndarray): the matrix holding our dynamical system of shape (n_neurons, timesteps)
        neuron_idx (int): the index of the neuron we want to estimate granger causality for
        observed_ratio (float): the proportion of n_neurons observed, must be betweem 0 and 1.
        regression_args (dict): dictionary of lasso regression arguments and hyperparameters

    Returns:
        A tuple (reject_null, p_vals)
        reject_null (list): a binary list of length n_neurons whether the null was 
            rejected for the selected neuron granger causing the other neurons
        p_vals (list): a list of the p-values for the corresponding Granger causality tests
    """
    n_neurons = X.shape[0]
    max_lag = 1
    alpha = alpha #/ (n_neurons* max_lag) # Bonferroni multiple comparisons correction

    reject_null = []   
    p_vals = []

    for target_neuron in range(n_neurons):
        ts_data = X[[neuron_idx, target_neuron], :].transpose()

        """solution"""
        res = grangercausalitytests(ts_data, maxlag=max_lag, verbose=False)
        # gets the p-value for the log-ratio test 
        pval = res[1][0]['lrtest'][1]

        p_vals.append(pval)
        reject_null.append(int(pval < alpha))

    return reject_null, p_vals