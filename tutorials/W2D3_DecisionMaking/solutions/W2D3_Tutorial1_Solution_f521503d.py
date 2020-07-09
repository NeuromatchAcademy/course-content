def simulate_accuracy_vs_threshold(sigma, threshold_list, num_sample):
    """
    Calculate the average decision accuracy vs. average decision length by
    running repeated SPRT simulations with thresholding stopping rule for each
    threshold.

    Args:
        sigma (float): standard deviation for observation model 
        threshold_list (list-like object): a list of evidence thresholds to run
                                           over
        num_sample (int): number of simulations to run per stopping time 

    Returns:
        accuracy_list: a list of average accuracies corresponding to input
                       `threshold_list`
        decision_length_list: a list of average decision lengths
    """
    decision_length_list = []
    accuracy_list = []
    for threshold in threshold_list:
        decision_time_list = []
        decision_list = []
        for i in range(num_sample):
            # run simulation and get decision of current simulation
            _, decision, data = simulate_SPRT_threshold(sigma, threshold)
            decision_time = len(data)
            decision_list.append(decision)
            decision_time_list.append(decision_time)

        # Calculate and store average decision length and accuracy
        decision_length = np.mean(decision_time_list)
        decision_accuracy = sum(decision_list) / len(decision_list)
        decision_length_list.append(decision_length)
        accuracy_list.append(decision_accuracy)

    return accuracy_list, decision_length_list

np.random.seed(100)
sigma = 3.75
num_sample = 100
log_alphas = np.concatenate([np.linspace(-5, -1, 4), np.linspace(-0.7, -0.1, 3)])
alpha_list = np.power(10, log_alphas)
threshold_list = threshold_from_errorrate(alpha_list)

with plt.xkcd():
  simulate_and_plot_accuracy_vs_threshold(sigma, threshold_list, num_sample)