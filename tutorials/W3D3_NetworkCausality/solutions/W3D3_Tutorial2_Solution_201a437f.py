n_trials = 5
timesteps = 1000 # shorter timesteps for faster running time

# solution
number_of_neurons = [5, 10, 25, 50, 100]

with plt.xkcd():
  plot_estimation_quality_vs_n_neurons(number_of_neurons)