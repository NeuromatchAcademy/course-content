
def regularized_loss(output, target, weights, L2_penalty=0, L1_penalty=0):
  """loss function with L2 and L1 regularization

  Args:
    output (torch.Tensor): output of network
    target (torch.Tensor): neural response network is trying to predict
    weights (torch.Tensor): linear layer weights from neurons to hidden units (net.in_layer.weight)
    L2_penalty : scaling factor of sum of squared weights
    L1_penalty : scalaing factor for sum of absolute weights

  Returns:
    (torch.Tensor) mean-squared error with L1 and L2 penalties added

  """

  loss_fn = nn.NLLLoss()
  loss = loss_fn(output, target)

  L2 = L2_penalty * torch.square(weights).sum()
  L1 = L1_penalty * torch.abs(weights).sum()
  loss += L1 + L2

  return loss

# Set random seeds for reproducibility
np.random.seed(1)
torch.manual_seed(1)

n_classes = 20

# Initialize network
net = DeepNetSoftmax(n_neurons, 20, n_classes)  # use M=20 hidden units

# Here you can play with L2_penalty > 0, L1_penalty > 0
train_loss, test_loss, predicted_test_labels = decode_orientation(net, n_classes,
                                                                  regularized_loss,
                                                                  resp_train, stimuli_train,
                                                                  resp_test, stimuli_test,
                                                                  n_iter=1000,
                                                                  L2_penalty=1e-2,
                                                                  L1_penalty=5e-4)

# Plot results
with plt.xkcd():
  plot_decoded_results(train_loss, test_loss, stimuli_test, predicted_test_labels)