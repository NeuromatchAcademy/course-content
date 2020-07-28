class ConvFC(nn.Module):
  """Deep network with one convolutional layer + one fully connected layer

  Attributes:
    conv (nn.Conv1d): convolutional layer
    dims (tuple): shape of convolutional layer output
    out_layer (nn.Linear): linear layer

  """

  def __init__(self, n_neurons, c_in=1, c_out=8, K=9, b=60):
    """ initialize layer
    Args:
        c_in: number of input stimulus channels
        c_out: number of convolutional channels
        K: size of each convolutional filter
        h: number of stimulus bins, n_bins
    """
    super().__init__()
    self.conv = nn.Conv1d(c_in, c_out, kernel_size=K, padding=K//2)
    self.dims = (c_out, b)  # dimensions of conv layer output
    M = np.prod(self.dims) # number of hidden units

    self.out_layer = nn.Linear(M, n_neurons)

    nn.init.normal_(self.out_layer.weight, std=0.01) # initialize weights to be small

  def forward(self, s):
    """ Predict neural responses to stimuli s

    Args:
        s (torch.Tensor): p x L tensor with stimuli

    Returns:
        torch.Tensor: p x N tensor with convolutional layer unit activations.

    """
    s = s.unsqueeze(1)  # p x 1 x L, add a singleton dimension for the single channel
    a = self.conv(s)  # output of convolutional layer
    a = a.view(-1, np.prod(self.dims))  # flatten each convolutional layer output into a vector

    y = self.out_layer(a)

    return y



# Choose loss function
MSE_loss = nn.MSELoss()

# Initialize network
net = ConvFC(n_neurons)

# Run GD on training set data
# ** this time we are also providing the test data to estimate the test loss
train_loss, test_loss = train(net, MSE_loss, stim_binary, resp_train,
                              test_data=stim_binary, test_labels=resp_test,
                              n_iter=500, learning_rate=20)

# Plot the training loss over iterations of GD
with plt.xkcd():
  plot_training_curves(train_loss, test_loss)