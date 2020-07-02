class DeepNetReLU(nn.Module):

  def __init__(self, n_hidden):
    super().__init__()  # needed to invoke the properties of the parent class nn.Module
    self.in_layer = nn.Linear(n_neurons, n_hidden)
    self.out_layer = nn.Linear(n_hidden, 1)

  def forward(self, x):
    h = torch.relu(self.in_layer(x))
    y = self.out_layer(h)
    return y