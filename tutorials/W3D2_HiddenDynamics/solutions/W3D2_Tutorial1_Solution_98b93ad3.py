
def simulate_accuracy_vs_stoptime(mu, sigma, stop_time_list, num_sample, no_numerical=False):
  """Calculate the average decision accuracy vs. stopping time by running
  repeated SPRT simulations for each stop time.

  Args:
      mu (float): absolute mean value of the symmetric observation distributions
      sigma (float): standard deviation for observation model
      stop_list_list (list-like object): a list of stopping times to run over
      num_sample (int): number of simulations to run per stopping time
      no_numerical (bool): flag that indicates the function to return analytical values only

  Returns:
      accuracy_list: a list of average accuracies corresponding to input
                      `stop_time_list`
      decisions_list: a list of decisions made in all trials
  """

  # Determine true state (1 or -1)
  true_dist = 1

  # Set up tracker of accuracy and decisions
  accuracies = np.zeros(len(stop_time_list),)
  accuracies_analytical = np.zeros(len(stop_time_list),)
  decisions_list = []

  # Loop over stop times
  for i_stop_time, stop_time in enumerate(stop_time_list):

    if not no_numerical:
      # Set up tracker of decisions for this stop time
      decisions = np.zeros((num_sample,))

      # Loop over samples
      for i in range(num_sample):

        # STEP 1: Simulate run for this stop time (hint: use output from last exercise)
        _, decision, _= simulate_SPRT_fixedtime(mu, sigma, stop_time, true_dist)

        # Log decision
        decisions[i] = decision

      # STEP 2: Calculate accuracy by averaging over trials
      accuracies[i_stop_time] = np.sum(decisions == true_dist) / decisions.shape[0]

      # Store the decisions
      decisions_list.append(decisions)

    # Calculate analytical accuracy
    # S_t is a normal variable with SNR scale as sqrt(stop_time)
    sigma_sum_gaussian = sigma / np.sqrt(stop_time)
    accuracies_analytical[i_stop_time] = 0.5 + 0.5 * erf(mu / np.sqrt(2) / sigma_sum_gaussian)

  return accuracies, accuracies_analytical, decisions_list


# Set random seed
np.random.seed(100)

# Set parameters of model
mu = 0.5
sigma = 4.65  # standard deviation for observation noise
num_sample = 100  # number of simulations to run for each stopping time
stop_time_list = np.arange(1, 150, 10) # Array of stopping times to use

# Calculate accuracies for each stop time
accuracies, accuracies_analytical, _ = simulate_accuracy_vs_stoptime(mu, sigma, stop_time_list,
                                                   num_sample)

# Visualize
with plt.xkcd():
  plot_accuracy_vs_stoptime(mu, sigma, stop_time_list, accuracies_analytical, accuracies)