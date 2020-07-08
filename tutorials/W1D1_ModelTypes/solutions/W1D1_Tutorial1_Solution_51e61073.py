
median_spike_count = np.median(total_spikes_per_neuron)

with plt.xkcd():
  # XKCD mode forces white outlines on a bar histogram, which is confusing
  # because you wouldn't see them in a "correct" student exercise.
  # Draw with stepfilled so this looks like what we want the students to make,
  # but it's fine for students to leave that parameter out.
  plt.hist(total_spikes_per_neuron, bins=50, histtype="stepfilled")
  plt.axvline(median_spike_count, color="limegreen", label="Median neuron")
  plt.axvline(mean_spike_count, color="orange", label="Mean neuron")
  plt.xlabel("Total spikes per neuron")
  plt.ylabel("Number of neurons")
  plt.legend()