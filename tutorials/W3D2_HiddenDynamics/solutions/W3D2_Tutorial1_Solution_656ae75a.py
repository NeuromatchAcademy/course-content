def simulate_accuracy_vs_threshold(sigma, threshold_list, num_sample):
  """Calculate the average decision accuracy vs. average decision speed by
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
      decision_speed_list: a list of average decision speeds
  """
  decision_speed_list = []
  accuracy_list = []
  for threshold in threshold_list:
    decision_time_list = []
    decision_list = []
    for i in range(num_sample):
      # run simulation and get decision of current simulation
      _, decision, Mvec = simulate_SPRT_threshold(sigma, threshold)
      decision_time = len(Mvec)
      decision_list.append(decision)
      decision_time_list.append(decision_time)

    # Calculate and store average decision speed and accuracy
    decision_speed = np.mean(1. / np.array(decision_time_list))
    decision_accuracy = sum(decision_list) / len(decision_list)
    decision_speed_list.append(decision_speed)
    accuracy_list.append(decision_accuracy)

  return accuracy_list, decision_speed_list


np.random.seed(100)
sigma = 3.75
num_sample = 200
alpha_list = np.logspace(-2, -0.1, 8)
threshold_list = threshold_from_errorrate(alpha_list)
with plt.xkcd():
  simulate_and_plot_accuracy_vs_threshold(sigma, threshold_list, num_sample)