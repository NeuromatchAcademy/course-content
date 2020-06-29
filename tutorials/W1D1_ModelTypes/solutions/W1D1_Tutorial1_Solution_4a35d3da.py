single_neuron_idx = 283
single_neuron_spikes = spike_times[single_neuron_idx]
single_neuron_isis = np.diff(single_neuron_spikes)
with plt.xkcd():
  plt.hist(single_neuron_isis, n_bins, histtype="stepfilled")
  plt.xlabel("ISI duration (s)")
  plt.ylabel("Number of spikes")
  plt.axvline(single_neuron_isis.mean(), color="orange", label="Mean ISI")
  plt.legend()