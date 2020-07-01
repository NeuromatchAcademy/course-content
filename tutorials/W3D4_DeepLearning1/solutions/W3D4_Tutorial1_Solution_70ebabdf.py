net = DeepNetReLU(20)  # initialize deep network, using DeepNetReLU()
istim = np.random.choice(n_stimuli, 100)  # indices of 100 random stimuli
out = net(resp[istim])  # use network to decode orientation from neural responses
loss = loss_fn(out, stimuli[istim])  # evaluate mean squared error using loss_fn()
print('mean squared error: %.2f' % loss)