
# Compute median spike count
median_spike_count = np.median(total_spikes_per_neuron)  # Hint: Try the function np.median

# Visualize median, mean, and histogram
with plt.xkcd():
  plt.hist(total_spikes_per_neuron, bins=50, histtype="stepfilled")
  plt.axvline(median_spike_count, color="limegreen", label="Median neuron")
  plt.axvline(mean_spike_count, color="orange", label="Mean neuron")
  plt.xlabel("Total spikes per neuron")
  plt.ylabel("Number of neurons")
  plt.legend()