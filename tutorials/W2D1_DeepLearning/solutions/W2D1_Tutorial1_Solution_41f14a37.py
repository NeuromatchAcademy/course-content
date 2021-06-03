
def train(net, loss_fn, train_data, train_labels,
          n_iter=50, learning_rate=1e-4,
          test_data=None, test_labels=None,
          L2_penalty=0, L1_penalty=0):
  """Run gradient descent to opimize parameters of a given network

  Args:
    net (nn.Module): PyTorch network whose parameters to optimize
    loss_fn: built-in PyTorch loss function to minimize
    train_data (torch.Tensor): n_train x n_neurons tensor with neural
      responses to train on
    train_labels (torch.Tensor): n_train x 1 tensor with orientations of the
      stimuli corresponding to each row of train_data
    n_iter (int, optional): number of iterations of gradient descent to run
    learning_rate (float, optional): learning rate to use for gradient descent
    test_data (torch.Tensor, optional): n_test x n_neurons tensor with neural
      responses to test on
    test_labels (torch.Tensor, optional): n_test x 1 tensor with orientations of
      the stimuli corresponding to each row of test_data
    L2_penalty (float, optional): l2 penalty regularizer coefficient
    L1_penalty (float, optional): l1 penalty regularizer coefficient

  Returns:
    (list): training loss over iterations

  """

  # Initialize PyTorch SGD optimizer
  optimizer = optim.SGD(net.parameters(), lr=learning_rate)

  # Placeholder to save the loss at each iteration
  train_loss = []
  test_loss = []

  # Loop over epochs
  for i in range(n_iter):

    # compute network output from inputs in train_data
    out = net(train_data)  # compute network output from inputs in train_data

    # evaluate loss function
    if L2_penalty==0 and L1_penalty==0:
      # normal loss function
      loss = loss_fn(out, train_labels)
    else:
      # custom loss function from bonus exercise 3.3
      loss = loss_fn(out, train_labels, net.in_layer.weight,
                     L2_penalty, L1_penalty)

    # Clear previous gradients
    optimizer.zero_grad()
    # Compute gradients
    loss.backward()

    # Update weights
    optimizer.step()

    # Store current value of loss
    train_loss.append(loss.item())  # .item() needed to transform the tensor output of loss_fn to a scalar

    # Get loss for test_data, if given (we will use this in the bonus exercise 3.2 and 3.3)
    if test_data is not None:
      out_test = net(test_data)
      # evaluate loss function
      if L2_penalty==0 and L1_penalty==0:
        # normal loss function
        loss_test = loss_fn(out_test, test_labels)
      else:
        # (BONUS code) custom loss function from Bonus exercise 3.3
        loss_test = loss_fn(out_test, test_labels, net.in_layer.weight,
                            L2_penalty, L1_penalty)
      test_loss.append(loss_test.item())  # .item() needed to transform the tensor output of loss_fn to a scalar

    # Track progress
    if (i + 1) % (n_iter // 5) == 0:
      if test_data is None:
        print(f'iteration {i + 1}/{n_iter} | loss: {loss.item():.3f}')
      else:
        print(f'iteration {i + 1}/{n_iter} | loss: {loss.item():.3f} | test_loss: {loss_test.item():.3f}')

  if test_data is None:
    return train_loss
  else:
    return train_loss, test_loss

# Set random seeds for reproducibility
np.random.seed(1)
torch.manual_seed(1)

# Initialize network with 10 hidden units
net = DeepNetReLU(n_neurons, 10)

# Initialize built-in PyTorch MSE loss function
loss_fn = nn.MSELoss()

# Run GD on data
train_loss = train(net, loss_fn, resp_train, stimuli_train)

# Plot the training loss over iterations of GD
with plt.xkcd():
  plt.plot(train_loss)
  plt.xlim([0, None])
  plt.ylim([0, None])
  plt.xlabel('iterations of gradient descent')
  plt.ylabel('mean squared error')
  plt.show()