sigma = 4.65  # standard deviation for observation noise
num_sample = 200  # number of simulations to run for each stopping time
stop_time_list = np.arange(1, 150, 10) # Stopping times to play with

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
  accuracy_list = []
  decisions_list = []
  for stop_time in stop_time_list:
    decision_list = []
    for i in range(num_sample):
      _, decision, _= simulate_SPRT_fixedtime(sigma, stop_time)
      decision_list.append(decision)

    # Calculate accuracy given the true decision is 1
    accuracy = sum(decision_list) / len(decision_list)
    accuracy_list.append(accuracy)
    decisions_list.append(decision_list)

  return accuracy_list, decisions_list


np.random.seed(100)
with plt.xkcd():
  simulate_and_plot_accuracy_vs_stoptime(sigma, stop_time_list, num_sample)