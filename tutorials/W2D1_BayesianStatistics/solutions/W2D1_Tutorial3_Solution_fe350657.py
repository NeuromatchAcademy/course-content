def my_Bayes_model_mse(params):
    """
    Function fits the Bayesian model from Tutorial 4

    Args :
        params (list of positive floats):  parameters used by the model
        (params[0]  = posterior scaling)

    Returns :
        (scalar) negative log-likelihood :sum of log probabilities
    """

    # Create the prior array
    p_independent=params[0]
    prior_array = calculate_prior_array(x,
                                        hypothetical_stim,
                                        p_independent,
                                        prior_sigma_indep= 3.)

    # Create posterior array
    posterior_array = calculate_posterior_array(prior_array, likelihood_array)

    # Create Binary decision array
    binary_decision_array = calculate_binary_decision_array(x, posterior_array)

    # we will use trial_ll (trial log likelihood) to register each trial
    trial_ll = np.zeros_like(true_stim)

    # Loop over stimuli
    for i_stim in range(len(true_stim)):

        # create the input array with true_stim as mean
        input_array = np.zeros_like(posterior_array)
        for i in range(len(x)):
            input_array[:, i] = my_gaussian(hypothetical_stim, true_stim[i_stim], 1)
            input_array[:, i] = input_array[:, i] / np.sum(input_array[:, i])

        # calculate the marginalizations
        marginalization_array, marginal = my_marginalization(input_array,
                                                    binary_decision_array)

        action = behaviour[i_stim]
        idx = np.argmin(np.abs(x - action))

        # Get the marginal likelihood corresponding to the action
        marginal_nonzero = marginal[idx] + np.finfo(float).eps  # avoid log(0)
        trial_ll[i_stim] = np.log(marginal_nonzero)

    neg_ll = - trial_ll.sum()

    return neg_ll

with plt.xkcd():
  plot_my_bayes_model(my_Bayes_model_mse)