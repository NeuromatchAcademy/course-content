def plot_resp_lowd(resp_dict):
    """Plot a low-dimensional representation of each dataset in resp_dict."""
    n_col = len(resp_dict)
    fig, axs = plt.subplots(1, n_col, figsize=(4.5 * len(resp_dict), 4.5))
    for i, (label, resp) in enumerate(resp_dict.items()):

      ax = axs[i]
      ax.set_title('%s responses' % label)

      # First do PCA to reduce dimensionality to 20 dimensions so that tSNE is faster
      resp_lowd = PCA(n_components=min(20, resp.shape[1])).fit_transform(resp)

      # Then do tSNE to reduce dimensionality to 2 dimensions
      resp_lowd = TSNE(n_components=2).fit_transform(resp_lowd)

      # Plot dimensionality-reduced population responses
      # on 2D axes, with each point colored by stimulus orientation
      x, y = resp_lowd[:, 0], resp_lowd[:, 1]
      pts = ax.scatter(x, y, c=ori, cmap='twilight', vmin=-90, vmax=90)
      fig.colorbar(pts, ax=ax, ticks=np.linspace(-90, 90, 5), label='Stimulus orientation')

      ax.set_xlabel('Dimension 1')
      ax.set_ylabel('Dimension 2')
      ax.set_xticks([])
      ax.set_yticks([])

with plt.xkcd():
  plot_resp_lowd(resp_dict)