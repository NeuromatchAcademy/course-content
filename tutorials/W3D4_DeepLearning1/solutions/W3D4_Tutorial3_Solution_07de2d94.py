def train(net):
  """Run stochastic gradient descent on binary cross-entropy loss for a given
  deep network
  
  Args:
    net (nn.Module): deep network whose parameters to optimize with SGD
  """

  # Set SGD hyperparameters
  n_iter = 200  # number of iterations of SGD
  learning_rate = 1e-3  # learning rate for SGD
  momentum = .99  # momentum parameter for SGD
  batch_size = 100  # number of data points in each mini-batch

  # Initialize binary cross-entropy loss function
  loss_fn = nn.BCELoss()

  # Initialize SGD optimizer with momentum
  optimizer = optim.SGD(net.parameters(), lr=learning_rate, momentum=momentum)

  # Placeholder to save loss at each iteration
  track_loss = []

  # Loop over iterations
  for i in range(n_iter):

    # Sample minibatch of oriented grating stimuli
    stimuli, tilt = sample_stimuli(batch_size)

    # Evaluate loss and update network weights
    out = net(stimuli)  # predicted probability of tilt right
    loss = loss_fn(out, tilt)  # evaluate loss
    optimizer.zero_grad()  # clear gradients
    loss.backward()  # compute gradients
    optimizer.step()  # update weights
    
    # Keep track of loss at each iteration
    track_loss.append(loss.item())

    # Track progress
    if (i + 1) % (n_iter / 10) == 0:
      print('iteration %i | loss: %.3f | percent correct: %.2f%%' % (i + 1, loss.item(), 100 * pcorrect(out, tilt)))
  
  # Plot loss
  plt.plot(track_loss)
  plt.xlabel('iterations of SGD')
  plt.ylabel('binary cross-entropy loss')
  plt.xlim([0, None])
  plt.ylim([0, None])
  plt.show()

# Initialize deep CNN and train it
net = DeepCNN()
with plt.xkcd():
  train(net)