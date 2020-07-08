def pmf_from_counts(counts):
  """Given counts, normalize by the total to estimate probabilities."""
  pmf = counts / np.sum(counts)
  return pmf


pmf = pmf_from_counts(counts)
with plt.xkcd():
  plot_pmf(pmf,isi_range)