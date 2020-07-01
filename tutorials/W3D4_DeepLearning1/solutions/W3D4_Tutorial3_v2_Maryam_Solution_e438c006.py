def RDM(resp):
  """Compute the representational dissimilarity matrix (RDM)

  Args:
    resp: S x N matrix with population responses to
      each stimulus in each row
  
  Returns:
    np.ndarray: S x S representational dissimilarity matrix
  """
  zresp = zscore(resp, axis=1)  # z-score responses to each stimulus
  return 1 - (zresp @ zresp.T) / zresp.shape[1]