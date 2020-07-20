def RDM(resp):
  """Compute the representational dissimilarity matrix (RDM)

  Args:
    resp (ndarray): S x N matrix with population responses to
      each stimulus in each row
  
  Returns:
    ndarray: S x S representational dissimilarity matrix
  """

  zresp = zscore(resp, axis=1)  # z-score responses to each stimulus
  return 1 - (zresp @ zresp.T) / zresp.shape[1]


with plt.xkcd():
  fig, axs = plt.subplots(1, len(resp_dict), figsize=(4 * len(resp_dict), 4))

  # Compute RDM's for each set of responses and plot
  rdm_dict = {}
  for i, (label, resp) in enumerate(resp_dict.items()):

    rdm_dict[label] = RDM(resp)
    plot_corr_matrix(rdm_dict[label], axs[i])

  axs[i].set_title(label)
 