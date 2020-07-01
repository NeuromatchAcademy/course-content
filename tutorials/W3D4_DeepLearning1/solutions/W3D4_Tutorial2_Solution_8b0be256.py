### train network with train function
def train(net, train_data, train_labels, learning_rate=10, n_epochs=500, L2_penalty=0., L1_penalty=0.):
  """Run gradient descent for network without batches
  
  Args:
    net (nn.Module): deep network whose parameters to optimize with SGD
    train_data: training data (n_train x input features)
    train_labels: training labels (n_train x output features)
    learning_rate (float): learning rate for gradient descent
    n_epochs (int): number of epochs to run gradient descent
    L2_penalty (float): magnitude of L2 penalty
    L1_penalty (float): magnitude of L1 penalty
  """
  optimizer = optim.SGD(net.parameters(), lr=learning_rate, momentum=0.5) # Initialize PyTorch SGD optimizer
  loss_fn = nn.MSELoss(reduction='mean') # PyTorch mean squared error loss function
  track_loss = []  # Placeholder for loss
  pbar = progress_bar(n_epochs) # Progress bar to track progress

  # Loop over epochs
  for i in range(n_epochs):
    y_pred = net(train_data) # Forward pass: compute predicted y by passing train_data to the model.

    ### Compute loss
    loss = loss_fn(y_pred, train_labels)
    L2 = L2_penalty * torch.square(net.out_layer.weight).sum() # add L2 penalty
    L1 = L1_penalty * torch.abs(net.out_layer.weight).sum() # add L1 penalty
    loss += L2 + L1

    ### Update parameters
    optimizer.zero_grad() # zero out gradients
    loss.backward() # Backward pass: compute gradient of the loss with respect to model parameters
    optimizer.step() # step parameters in gradient direction
    track_loss.append(loss.item())  # .item() transforms the tensor to a scalar and does .detach() for us

    # Track progress
    if i%50==0:
      pbar.update()
      print('epoch %d: L1 loss %0.5f; L2 loss %0.5f; total loss %0.5f'%(i, L1.item(), L2.item(), loss.item()))

  ### Plot the loss
  plt.plot(track_loss)
  plt.xlabel('iterations of gradient descent')
  plt.ylabel('mean squared error loss')
  plt.show()


### initialize network
net = ConvFC(n_neurons)

### train network
with plt.xkcd():
  train(net, stim_binary, respbin_train, L1_penalty=1e-6, L2_penalty=1e-4, learning_rate=10, n_epochs=500)