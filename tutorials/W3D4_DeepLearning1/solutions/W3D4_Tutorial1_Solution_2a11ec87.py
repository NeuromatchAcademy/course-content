def plot_tuning():
  """Plot the tuning curve of a random neuron"""

  neuron_indx = np.random.choice(n_neurons)  # pick random neuron
  plt.plot(np.rad2deg(stimuli), resp[:, neuron_indx], '.')  # plot its responses as a function of stimulus orientation
  
  plt.title('neuron %i' % neuron_indx)
  plt.xlabel('stimulus orientation ($^o$)')
  plt.ylabel('neural response')
  plt.xticks(np.linspace(0, 360, 5))
  plt.show()

with plt.xkcd():
  plot_tuning()