class DeepCNN(nn.Module):
  """Convolutional neural network

    Attributes:
      conv1 (nn.Conv2d): first convolution layer
      pool1 (nn.MaxPool2d): first max pooling layer
      dims1 (tuple of ints): dimensions of output from pool1 layer
      conv2 (nn.Conv2d): second convolution layer
      pool2 (nn.MaxPool2d): second max pooling layer
      dims2 (tuple of ints): dimensions of output from pool2 layer
      fc (nn.Linear): fully connected layer
      out (nn.Linear): output layer
    
    """
  
  def __init__(self):
    super().__init__()

    # Convolution + pooling layer 1
    C_in = 1  # input stimuli have only 1 input channel
    C_out = 16  # number of output channels (i.e. of convolutional kernels to convolve the input with)
    K = 3   # size of each convolutional kernel
    Kpool = 2   # size of patches over which to pool
    self.conv1 = nn.Conv2d(C_in, C_out, kernel_size=K, padding=K//2)  # add padding to ensure that each channel has same dimensionality as input
    self.pool1 = nn.MaxPool2d(Kpool)
    self.dims1 = (C_out, h // Kpool, w // Kpool)  # dimensions of pool1 layer output

    # Convolution + pooling layer 2
    C_in = self.dims1[0]
    C_out = 4
    K = 7
    Kpool = 2
    self.conv2 = nn.Conv2d(C_in, C_out, kernel_size=K, padding=K//2)
    self.pool2 = nn.MaxPool2d(Kpool)
    self.dims2 = (C_out, self.dims1[1] // Kpool, self.dims1[2] // Kpool)
    
    # Fully connected layer
    self.fc = nn.Linear(np.prod(self.dims2), 10)  # flattened pool2 output --> 10D representation

    # Output layer
    self.out = nn.Linear(10, 1)  # 10D representation --> scalar

  def forward(self, x):
    """Classify grating stimulus as tilted right or left

    Args:
        x (torch.Tensor): p x 48 x 64 tensor with pixel grayscale values for
            each of p stimulus images.
    
    Returns:
        torch.Tensor: p x 1 tensor with network outputs for each input provided
            in x. Each output should be interpreted as the probability of the
            corresponding stimulus being tilted right.

    """
    x = x.unsqueeze(1)  # p x 1 x 48 x 64, add a singleton dimension for the single stimulus channel
    x = torch.relu(self.conv1(x))  # output of first convolutional layer
    x = self.pool1(x)  # output of first pooling layer
    x = torch.relu(self.conv2(x))  # output of first convolutional layer
    x = self.pool2(x)  # output of first pooling layer
    x = x.view(-1, np.prod(self.dims2))  # flatten each pooling layer output into a vector
    x = torch.relu(self.fc(x))  # output of fully connected layer
    x = torch.sigmoid(self.out(x))  # network output
    return x