
sigma = 3.95  
num_repeats = 500  # number of simulations to run for each error rate
alpha_list = np.power(10,list(range(-5,0)) + np.linspace(-0.9,-0.1,9).tolist())   # list of error rates

threshold_list = list(map(threshold_from_errorrate, alpha_list))

def simulate_accuracy_vs_speed(sigma, threshold_list, num_sample=100):
    """
    Calculate the average decision accuracy vs. average decision speed by running repeated SPRT simulations
    with thresholding stopping rule for each threshold

    Args:
        sigma (float): standard deviation for observation model 
        threshold_list (list-like object): a list of evidence thresholds to run over
        num_sample (int): number of simulations to run per stopping time 

    Returns:
        accuracy_list: a list of average accuracies corresponding to input `stop_time_list`
        decision_speed_list: a list of average decision speeds
    """
    decision_speed_list = []  # container for average decision speed for each alpha
    accuracy_list = [] # container for decision accuracy for each alpha
    for threshold in threshold_list:
        decision_time_list = [] # container for decision time for each simulation
        decision_list = [] # container for decision for every simulation
        for i in range(num_repeats):
            # run simulation and get decision of current simulation
            _, decision, data = simulate_SPRT_threshold(sigma, threshold)
            decision_time = len(data)
            decision_list.append(decision)
            decision_time_list.append(decision_time)
            
        decision_speed = np.mean(1.0 / np.asarray(decision_time_list))
        decision_accuracy = sum(decision_list) / len(decision_list)
        decision_speed_list.append(decision_speed)
        accuracy_list.append(decision_accuracy)

    return accuracy_list, decision_speed_list

accuracy_list, decision_speed_list = simulate_accuracy_vs_speed(sigma, threshold_list, num_sample=num_sample)

with plt.xkcd():
  simulate_and_plot_speed_vs_accuracy(sigma, threshold_list, num_sample)