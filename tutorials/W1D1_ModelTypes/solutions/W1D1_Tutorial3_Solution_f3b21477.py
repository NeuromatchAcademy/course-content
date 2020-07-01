def pmf_from_counts(counts):
  """Given counts, normalize by the total to estimate probabilities."""
  pmf = counts / np.sum(counts)
  return pmf
pmf = pmf_from_counts(counts)
with plt.xkcd():
  histogram(pmf, bins, ax_args={
    'title': f"Neuron {neuron_idx}",
    'xlabel': "Inter-spike interval (s)",
    'ylabel': "Probability mass",
  })