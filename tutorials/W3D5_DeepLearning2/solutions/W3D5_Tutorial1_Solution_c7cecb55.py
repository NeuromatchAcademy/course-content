
def minibatch_fn(net, loss_fn, optimizer, batch):
    """
    Trains network for a single batch.

    Args:
      net (torch network)
          ANN network (nn.Module)

      loss_fn (torch loss)
          loss function for SGD

      optimizer (torch optimizer)
          optimizer for SGD

      batch (torch.Tensor)
          vectorized input images
             
    Returns:
      Nothing.
    """

    output_train = net(batch)
    loss = loss_fn(output_train, batch)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    return(loss)

n_epochs = 3
batch_size = 64

encoding_size = 16

model = nn.Sequential(nn.Linear(input_size, encoding_size),
                      nn.PReLU(),
                      nn.Linear(encoding_size, input_size),
                      nn.Sigmoid())
with plt.xkcd():
  runSGD(model, input_train, input_test, criterion='mse',
        n_epochs=n_epochs, batch_size=batch_size, minibatch_fn=minibatch_fn)