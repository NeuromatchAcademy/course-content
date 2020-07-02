def train(net, train_data, train_labels):
  """Run stochastic gradient descent for a given network
  
  Args:
    net (nn.Module): deep network whose parameters to optimize with SGD
    train_data (torch.Tensor): n_train x n_neurons tensor with neural
      responses to train on
    train_labels (torch.Tensor): n_train x 1 tensor with orientations of the
      stimuli corresponding to each row of train_data, in radians

  """

  # Set SGD hyperparameters
  learning_rate = 1e-3  # learning rate for SGD
  n_epochs = 10  # number of epochs to run SGD
  batch_size = 250  # number of data points in each mini-batch

  # Initialize PyTorch SGD optimizer
  optimizer = optim.SGD(net.parameters(), lr=learning_rate)

  # Placeholder to save MSE at each iteration
  train_mse = []

  # Loop over epochs (cf. appendix)
  for i in range(n_epochs):

    # Split up training data into random non-overlapping mini-batches
    ishuffle = torch.randperm(train_data.shape[0])  # random ordering of training data
    minibatch_data = torch.split(train_data[ishuffle], batch_size)  # split train_data into minibatches
    minibatch_labels = torch.split(train_labels[ishuffle], batch_size)  # split train_labels into minibatches

    # Loop over mini-batches
    for r, ori in zip(minibatch_data, minibatch_labels):

      # Evaluate mean squared error loss
      out = net(r)  # use network to decode orientation from neural responses in this minibatch
      loss = loss_fn(out, ori)  # evaluate mean squared error for this minibatch

      # Store current mean squared error
      train_mse.append(loss.item())  # .item() transforms the tensor to a scalar and does .detach() for us

      # Compute gradients
      optimizer.zero_grad()  # clear gradients
      loss.backward()

      # Update weights
      optimizer.step()

    # Track progress
    print(f'epoch {i + 1}/{n_epochs} | loss on last mini-batch: {loss.item():.3f}')

  
  # Plot the loss
  plt.plot(train_mse)
  plt.xlim([0, None])
  plt.ylim([0, None])
  plt.xlabel('iterations of stochastic gradient descent')
  plt.ylabel('mean squared error\non training data')
  plt.show()

# Split data into training set and testing set
n_train = int(0.75 * n_stimuli)  # putting 75% of data into training set
ishuffle = torch.randperm(n_stimuli)
itrain = ishuffle[:n_train]  # indices of data samples to include in training set
itest = ishuffle[n_train:]  # indices of data samples to include in testing set

# Initialize network and train it on training set
net = DeepNetReLU(20)  # use M=20 hidden units
with plt.xkcd():
  train(net, resp[itrain], stimuli[itrain])