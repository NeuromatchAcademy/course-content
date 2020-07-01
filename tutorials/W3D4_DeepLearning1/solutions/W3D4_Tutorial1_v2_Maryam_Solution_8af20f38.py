def decoding_error(net, test_data, test_labels):
  """Plot decoding error as a function of true stimulus orientation, in degrees

  Args:
    net (nn.Module): deep network to use to decode stimulus orientation
    test_data (torch.Tensor): n_test x n_neurons tensor with neural
      responses to decode
    test_labels (torch.Tensor): n_test x 1 tensor with orientations of the
      stimuli corresponding to each row of test_data, in radians

  """

  out = net(test_data)  # decode stimulus orientation for each population response in test set
  ori_decode = np.rad2deg(out.detach())  # transform from radians to degrees
  ori_true = np.rad2deg(test_labels)  # true stimulus orientations, in degrees
  error = ori_decode - ori_true  # decoding error, in degrees
  plt.plot(ori_true, error, '.')   # plot decoding error as a function of true orientation

  plt.xlabel('true stimulus orientation ($^o$)')
  plt.ylabel('decoding error ($^o$)')
  plt.xticks(np.linspace(0, 360, 5))
  plt.yticks(np.linspace(-360, 360, 9))
  plt.show()

with plt.xkcd():
  decoding_error(net, resp[itest], stimuli[itest])