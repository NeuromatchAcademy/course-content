def plot_tuning_curve(resp, ori, ax=None):
  """Plot single neuron responses as a function of stimulus orientation

  Args:
    resp (numpy array): n_stimuli x n_neurons matrix with responses of each
      neuron whose tuning curve to plot. Can also be a 1D array of length 
      n_stimuli to plot tuning curve of a single neuron.
    ori (numpy array): 1D array of length stimuli with orientations of each
      stimulus, in radians
    ax (matplotlib axes): axes onto which to plot

  """
  if ax is None:
    ax = plt.gca()
  
  ax.plot(np.rad2deg(ori), resp, '.-')
  
  ax.set_xticks(np.linspace(-90, 90, 5))
  ax.set_xlabel('stimulus orientation')
  ax.set_ylabel('neuron response')

def plot_dim_reduction(resp, ori, ax=None):
  """Plot dimensionality-reduced population responses (using tSNE)

  Args:
    resp (numpy array): n_stimuli x n_neurons matrix with population responses
    ori (numpy array): 1D array of length stimuli with orientations of each
      stimulus, in radians
    ax (matplotlib axes): axes onto which to plot

  """
  if ax is None:
    ax = plt.gca()

  # First do PCA to reduce dimensionality to 200 dimensions so that tSNE is faster
  resp_lowd = PCA(n_components=min(200, resp.shape[1])).fit_transform(resp)

  # Then do tSNE to reduce dimensionality to 2 dimensions
  resp_lowd = TSNE(n_components=2).fit_transform(resp_lowd)

  # Plot dimensionality-reduced population responses
  # on 2D axes, with each point colored by stimulus orientation
  scat = ax.scatter(resp_lowd[:, 0], resp_lowd[:, 1], c=np.rad2deg(ori), cmap='twilight')
  
  cbar = plt.colorbar(scat, ax=ax, label='stimulus orientation')
  ax.set_xlabel('dimension 1')
  ax.set_ylabel('dimension 2')
  ax.set_xticks([])
  ax.set_yticks([])

# Aggregate all responses into one dict
resp_dict = {}
resp_dict['V1 data'] = resp_v1
for k, v in resp_model.items():
  label = 'model\nlayer %s' % k
  resp_dict[label] = v

# Plot tuning curves and dimensionality-reduced responses next to each other
with plt.xkcd():
  figsize = 4
  fig, axs = plt.subplots(2, len(resp_dict), figsize=(len(resp_dict) * figsize, 2 * figsize))

  for i, (label, resp) in enumerate(resp_dict.items()):

    axs[0, i].set_title('%s responses' % label)

    # Plot tuning curves of three random neurons
    ineurons = np.random.choice(resp.shape[1], 3, replace=False)  # indices of three random neurons
    plot_tuning_curve(resp[:, ineurons], ori, axs[0, i])

    # Plot dimensionality-reduced population responses
    plot_dim_reduction(resp, ori, axs[1, i])

  plt.tight_layout()
  plt.show()