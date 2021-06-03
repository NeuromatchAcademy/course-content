def simulate_accuracy_vs_stoptime(sigma, stop_time_list, num_sample):
  """Calculate the average decision accuracy vs. stopping time by running
  repeated SPRT simulations for each stop time.

  Args:
      sigma (float): standard deviation for observation model
      stop_list_list (list-like object): a list of stopping times to run over
      num_sample (int): number of simulations to run per stopping time

  Returns:
      accuracy_list: a list of average accuracies corresponding to input
                      `stop_time_list`
      decisions_list: a list of decisions made in all trials
  """

  # Determine true state (1 or -1)
  true_dist = 1

  # Set up tracker of accuracy and decisions
  accuracies = np.zeros(len(stop_time_list),)
  decisions_list = []

  # Loop over stop times
  for i_stop_time, stop_time in enumerate(stop_time_list):

    # Set up tracker of decisions for this stop time
    decisions = np.zeros((num_sample,))

    # Loop over samples
    for i in range(num_sample):

      # Simulate run for this stop time (hint: last exercise)
      _, decision, _= simulate_SPRT_fixedtime(sigma, stop_time, true_dist)

      # Log decision
      decisions[i] = decision

    # Calculate accuracy
    accuracies[i_stop_time] = np.sum(decisions == true_dist) / decisions.shape[0]

    # Log decisions
    decisions_list.append(decisions)

  return accuracies, decisions_list


# Set random seed
np.random.seed(100)

# Set parameters of model
sigma = 4.65  # standard deviation for observation noise
num_sample = 200  # number of simulations to run for each stopping time
stop_time_list = np.arange(1, 150, 10) # Array of stopping times to use

# Calculate accuracies for each stop time
accuracies, _ = simulate_accuracy_vs_stoptime(sigma, stop_time_list,
                                                   num_sample)

# Visualize
with plt.xkcd():
  plot_accuracy_vs_stoptime(stop_time_list, accuracies)