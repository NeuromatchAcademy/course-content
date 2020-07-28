def regularized_MSE_loss(output, target, weights=None, L2_penalty=0, L1_penalty=0):
  """loss function for MSE

  Args:
    output (torch.Tensor): output of network
    target (torch.Tensor): neural response network is trying to predict
    weights (torch.Tensor): fully-connected layer weights of network (net.out_layer.weight)
    L2_penalty : scaling factor of sum of squared weights
    L1_penalty : scalaing factor for sum of absolute weights

  Returns:
    (torch.Tensor) mean-squared error with L1 and L2 penalties added

  """

  loss_fn = nn.MSELoss()
  loss = loss_fn(output, target)

  if weights is not None:
    L2 = L2_penalty * torch.square(weights).sum()
    L1 = L1_penalty * torch.abs(weights).sum()
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
with plt.xkcd():
  plot_training_curves(train_loss, test_loss)