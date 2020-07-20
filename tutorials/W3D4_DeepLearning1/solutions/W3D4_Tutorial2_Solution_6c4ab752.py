def regularized_MSE_loss(output, target, weights=None, L2_penalty=0, L1_penalty=0):
  """loss function for MSE 

  Args:
    output (torch.Tensor): output of network
    target (torch.Tensor): neural response network is trying to predict
    weights (torch.Tensor): fully-connected layer weights of network (net.out_layer.weight)

  Returns:
    (torch.Tensor) mean-squared error with L1 and L2 penalties added

  """

  loss_fn = nn.MSELoss()
  loss = loss_fn(output, target)

  if weights is not None: # if the weights are passed to the function

    L2 = L2_penalty * torch.square(weights).sum() # add L2 penalty
    L1 = L1_penalty * torch.abs(weights).sum() # add L1 penalty
    loss += L1 + L2

  return loss

# Initialize network
net = ConvFC(n_neurons)

# Train network
train_loss, test_loss = train(net, regularized_MSE_loss, stim_binary, resp_train, 
                              test_data=stim_binary, test_labels=resp_test,
                              learning_rate=10, n_iter=500, 
                              L2_penalty=1e-4, L1_penalty=1e-6)

# Plot the training loss over iterations of GD
plt.plot(train_loss, 'y')
plt.plot(test_loss, '.', markersize=10, color='m')

plt.xlabel('iterations of gradient descent')
plt.ylabel('mean squared error')
plt.legend(['train loss', 'test loss'])
plt.show()