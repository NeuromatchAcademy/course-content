def plot_rdm_rows(ori_plot, rdm_dict, ori, ax):
  """Plot the dissimilarity of response to each stimulus with response to one
  specific stimulus

  Args:
    ori_plot (float): plot dissimilarity with response to stimulus with
      orientation closest to ori_plot
    rdm_dict (dict): RDM's from which to extract dissimilarities
    ori (np.ndarray): orientations corresponding to each row/column of RDM's in
      rdm_dict
    ax (matplotlib axes): where to plot
  
  """

  # Get index of orientation closest to ori_plot
  iori = np.argmin(np.abs(ori - ori_plot))

  # Plot dissimilarity curves in each RDM
  for label, rdm in rdm_dict.items():
    ax.plot(ori, rdm[iori, :], label=label)

  # Draw vertical line at stimulus we are plotting dissimilarity w.r.t.
  ax.set_ylim(ax.get_ylim())  # fix y-axis limits
  ax.plot([ori[iori], ori[iori]], ax.get_ylim(), color="0.7", zorder=-1)

  # Label axes
  ax.set_title(f'dissimilarity with response\nto {ori_plot: .0f}$^o$ stimulus')
  ax.set_xlabel('stimulus orientation ($^o$)')
  ax.set_ylabel('dissimilarity')
  ax.legend()

with plt.xkcd():
  # Plot dissimilarity curves for four different orientations
  ori_plot = [-75, -25, 25, 75]
  fig, axs = plt.subplots(1, len(ori_plot), figsize=(len(ori_plot) * 6, 6))
  for ori_p, ax in zip(ori_plot, axs):
    ax.set_title

    plot_rdm_rows(ori_p, rdm_dict, ori, ax)
    
  plt.tight_layout()