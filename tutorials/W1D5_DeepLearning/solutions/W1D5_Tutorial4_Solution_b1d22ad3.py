class ConvFC(nn.Module):
  """Deep network with one convolutional layer + one fully connected layer

  Attributes:
    conv (nn.Conv1d): convolutional layer
    dims (tuple): shape of convolutional layer output
    out_layer (nn.Linear): linear layer

  """

  def __init__(self, n_neurons, c_in=1, c_out=6, K=7, b=12*16,
               filters=None):
    """ initialize layer
    Args:
        c_in: number of input stimulus channels
        c_out: number of convolutional channels
        K: size of each convolutional filter
        h: number of stimulus bins, n_bins
    """
    super().__init__()
    self.conv = nn.Conv2d(c_in, c_out, kernel_size=K,
                          padding=K//2, stride=1)
    self.dims = (c_out, b)  # dimensions of conv layer output
    M = np.prod(self.dims) # number of hidden units
    self.out_layer = nn.Linear(M, n_neurons)

    # initialize weights
    if filters is not None:
      self.conv.weight = nn.Parameter(filters)
      self.conv.bias = nn.Parameter(torch.zeros((c_out,), dtype=torch.float32))

    nn.init.normal_(self.out_layer.weight, std=0.01) # initialize weights to be small

  def forward(self, s):
    """ Predict neural responses to stimuli s

    Args:
        s (torch.Tensor): n_stimuli x c_in x h x w tensor with stimuli

    Returns:
        y (torch.Tensor): n_stimuli x n_neurons tensor with predicted neural responses

    """
    a = self.conv(s)  # output of convolutional layer
    a = a.view(-1, np.prod(self.dims))  # flatten each convolutional layer output into a vector
    y = self.out_layer(a)
    return y


device = torch.device('cpu')

# (Optional) To speed up processing, go to "Runtime" menu and "Change runtime"
# and select GPU processing, then uncomment line below, otherwise runtime will
# be ~ 2 minutes
# device = torch.device('cuda')

# Initialize network
n_neurons = resp_train.shape[1]
## Initialize with filters from Tutorial 2
example_filters = filters(out_channels=6, K=7)

net = ConvFC(n_neurons, filters = example_filters)
net = net.to(device)

# Run GD on training set data
# ** this time we are also providing the test data to estimate the test loss
train_loss, test_loss = train(net, regularized_MSE_loss,
                              train_data=grating_stimuli.to(device), train_labels=resp_train.to(device),
                              test_data=grating_stimuli.to(device), test_labels=resp_test.to(device),
                              n_iter=200, learning_rate=2,
                              L2_penalty=5e-4, L1_penalty=1e-6)

# Visualize
with plt.xkcd():
  plot_training_curves(train_loss, test_loss)