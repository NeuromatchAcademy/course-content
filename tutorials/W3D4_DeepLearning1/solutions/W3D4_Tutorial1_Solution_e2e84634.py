
def decode_orientation(n_classes, train_data, train_labels, test_data, test_labels):
  """ Initialize, train, and test deep network to decode binned orientation from neural responses

  Args:
    n_classes (scalar): number of classes in which to bin orientation
    train_data (torch.Tensor): n_train x n_neurons tensor with neural
      responses to train on
    train_labels (torch.Tensor): n_train x 1 tensor with orientations of the
      stimuli corresponding to each row of train_data, in radians
    test_data (torch.Tensor): n_test x n_neurons tensor with neural
      responses to train on
    test_labels (torch.Tensor): n_test x 1 tensor with orientations of the
      stimuli corresponding to each row of train_data, in radians

  Returns:
    (list, torch.Tensor): training loss over iterations, n_test x 1 tensor with predicted orientations of the
      stimuli from decoding neural network
  """

  # Bin stimulus orientations in training set
  train_binned_labels = stimulus_class(train_labels, n_classes)

  # Initialize network
  net = DeepNetSoftmax(n_neurons, 20, n_classes)  # use M=20 hidden units

  # Initialize built-in PyTorch MSE loss function
  loss_fn = nn.NLLLoss()

  # Run GD on training set data, using learning rate of 0.1
  train_loss = train(net, loss_fn, train_data, train_binned_labels, learning_rate=0.1)

  # Decode neural responses in testing set data
  out = net(resp_test)
  out_labels = np.argmax(out.detach(), axis=1)  # predicted classes

  return train_loss, out_labels


# Set random seeds for reproducibility
np.random.seed(1)
torch.manual_seed(1)

n_classes = 12  # start with 12, then (bonus) try making this as big as possible! does decoding get worse?

# Initialize, train, and test network
train_loss, predicted_test_labels = decode_orientation(n_classes, resp_train, stimuli_train, resp_test, stimuli_test)

# Plot results
with plt.xkcd():
  plot_decoded_results(train_loss, stimuli_test, predicted_test_labels)