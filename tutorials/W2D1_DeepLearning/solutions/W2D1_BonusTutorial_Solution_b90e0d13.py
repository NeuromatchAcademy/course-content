
def decode_orientation(net, n_classes, loss_fn,
                       train_data, train_labels, test_data, test_labels,
                       n_iter=1000, L2_penalty=0, L1_penalty=0):
  """ Initialize, train, and test deep network to decode binned orientation from neural responses

  Args:
    net (nn.Module): deep network to run
    n_classes (scalar): number of classes in which to bin orientation
    loss_fn (function): loss function to run
    train_data (torch.Tensor): n_train x n_neurons tensor with neural
      responses to train on
    train_labels (torch.Tensor): n_train x 1 tensor with orientations of the
      stimuli corresponding to each row of train_data, in radians
    test_data (torch.Tensor): n_test x n_neurons tensor with neural
      responses to train on
    test_labels (torch.Tensor): n_test x 1 tensor with orientations of the
      stimuli corresponding to each row of train_data, in radians
    n_iter (int, optional): number of iterations to run optimization
    L2_penalty (float, optional): l2 penalty regularizer coefficient
    L1_penalty (float, optional): l1 penalty regularizer coefficient

  Returns:
    (list, torch.Tensor): training loss over iterations, n_test x 1 tensor with predicted orientations of the
      stimuli from decoding neural network
  """

  # Bin stimulus orientations in training set
  train_binned_labels = stimulus_class(train_labels, n_classes)
  test_binned_labels = stimulus_class(test_labels, n_classes)


  # Run GD on training set data, using learning rate of 0.1
  # (add optional arguments test_data and test_binned_labels!)
  train_loss, test_loss = train(net, loss_fn, train_data, train_binned_labels,
                                learning_rate=0.1, test_data=test_data,
                                test_labels=test_binned_labels, n_iter=n_iter,
                                L2_penalty=L2_penalty, L1_penalty=L1_penalty)

  # Decode neural responses in testing set data
  out = net(test_data)
  out_labels = np.argmax(out.detach(), axis=1)  # predicted classes

  frac_correct = (out_labels==test_binned_labels).sum() / len(test_binned_labels)
  print(f'>>> fraction correct = {frac_correct:.3f}')

  return train_loss, test_loss, out_labels

# Set random seeds for reproducibility
np.random.seed(1)
torch.manual_seed(1)

n_classes = 20

# Initialize network
net = DeepNetSoftmax(n_neurons, 20, n_classes)  # use M=20 hidden units

# Initialize built-in PyTorch negative log likelihood loss function
loss_fn = nn.NLLLoss()

# Train network and run it on test images
# this function uses the train function you wrote before
train_loss, test_loss, predicted_test_labels = decode_orientation(net, n_classes, loss_fn,
                                                                  resp_train, stimuli_train, resp_test, stimuli_test)

# Plot results
with plt.xkcd():
  plot_decoded_results(train_loss, test_loss, stimuli_test, predicted_test_labels)