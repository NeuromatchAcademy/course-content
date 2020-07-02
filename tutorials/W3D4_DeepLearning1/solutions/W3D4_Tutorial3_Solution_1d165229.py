def correlate_rdms(rdm1, rdm2):
  """Correlate off-diagonal elements of two RDM's

  Args:
    rdm1 (np.ndarray): S x S representational dissimilarity matrix
    rdm2 (np.ndarray): S x S representational dissimilarity matrix to
      correlate with rdm1
  
  Returns:
    float: correlation coefficient between the off-diagonal elements
      of rdm1 and rdm2
    
  """
  
  # Extract off-diagonal elements of each RDM
  ioffdiag = np.triu_indices(rdm1.shape[0], k=1)  # indices of off-diagonal elements
  rdm1_offdiag = rdm1[ioffdiag]
  rdm2_offdiag = rdm2[ioffdiag]

  # Compute correlation coefficient
  return zscore(rdm1_offdiag) @ zscore(rdm2_offdiag) / len(rdm2_offdiag)