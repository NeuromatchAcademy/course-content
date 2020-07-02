def test(net, test_data, test_labels):
  """Decode stimulus orientation from neural responses in test data and plot
  against the true stimulus orientations, in degrees

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

  # Plot
  plt.plot(ori_true, ori_decode, '.')  # plot true orientation vs decoded orientation
  plt.xlabel('true stimulus orientation ($^o$)')
  plt.ylabel('decoded stimulus orientation ($^o$)')
  axticks = np.linspace(0, 360, 5)
  plt.xticks(axticks)
  plt.yticks(axticks)
  plt.show()

with plt.xkcd():
  test(net, resp[itest], stimuli[itest])