def m_step(gamma, xi, dt):
  """Calculate the M-step updates for the HMM spiking model.
  Args:
    gamma ():       Number of epochs of EM to run
    xi (numpy 3d array): Tensor of recordings, has shape (n_trials, T, C)
    dt (float):         Duration of a time bin
  Returns:
    psi_new (numpy vector): Updated initial probabilities for each state
    A_new (numpy matrix):   Updated transition matrix, A[i,j] represents the
                            prob. to switch from j to i. Has shape (K,K)
    L_new (numpy matrix):   Updated Poisson rate parameter for different
                            cells. Has shape (C,K)
  """
  # Calculate and normalize the new initial probabilities, psi_new
  psi_new = gamma[:, 0].mean(axis=0)
  # Make sure the probabilities are normalized

  psi_new /= psi_new.sum()
  # Calculate new transition matrix
  A_new = xi.sum(axis=(0, 1)) / gamma[:, :-1].sum(axis=(0, 1))[:, np.newaxis]
  # Calculate new firing rates
  L_new = (np.swapaxes(Y, -1, -2) @ gamma).sum(axis=0) / gamma.sum(axis=(0, 1)) / dt
  return psi_new, A_new, L_new