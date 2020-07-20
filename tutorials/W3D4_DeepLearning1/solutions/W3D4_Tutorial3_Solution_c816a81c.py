with plt.xkcd():
  fig, axs = plt.subplots(1, len(resp_dict), figsize=(len(resp_dict) * 6, 6))

  for i, (label, resp) in enumerate(resp_dict.items()):

    ax = axs[i]
    ax.set_title('%s responses' % label)

    # First do PCA to reduce dimensionality to 20 dimensions so that tSNE is faster
    resp_lowd = PCA(n_components=min(20, resp.shape[1])).fit_transform(resp)

    # Then do tSNE to reduce dimensionality to 2 dimensions
    resp_lowd = TSNE(n_components=2).fit_transform(resp_lowd)

    # Plot dimensionality-reduced population responses
    # on 2D axes, with each point colored by stimulus orientation
    scat = ax.scatter(resp_lowd[:,0], resp_lowd[:,1], c=ori, cmap='twilight', vmin=-90, vmax=90)  
    cbar = plt.colorbar(scat, ax=ax, ticks=np.linspace(-90, 90, 5), label='stimulus orientation')
    
    ax.set_xlabel('dimension 1')
    ax.set_ylabel('dimension 2')
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()