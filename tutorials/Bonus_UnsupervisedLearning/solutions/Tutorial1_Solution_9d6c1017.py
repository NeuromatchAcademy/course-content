encoding_size = 2
n_epochs = 10
batch_size = 64

# set PyTorch RNG seed
torch_seed = 0

model = nn.Sequential(
    nn.Linear(input_size, encoding_size),
    nn.ReLU(),
    nn.Linear(encoding_size, input_size),
    nn.Sigmoid()
    )

encoder = model[:2]
decoder = model[2:]

# reset RNGs for weight initialization
torch.manual_seed(torch_seed)
np.random.seed(0)

# reset encoder weights and biases
encoder.apply(init_weights_kaiming_uniform)

# retrieve weights and biases from the encoder before training
encoder_w_init, encoder_b_init = get_layer_weights(encoder[0])
decoder_w_init, decoder_b_init = get_layer_weights(decoder[0])

# reset RNGs for minibatch sequence
torch.manual_seed(torch_seed)
np.random.seed(0)

# train the autoencoder
runSGD(model, input_train, input_test, criterion='bce',
       n_epochs=n_epochs, batch_size=batch_size)

# retrieve weights and biases from the encoder after training
encoder_w_train, encoder_b_train = get_layer_weights(encoder[0])
decoder_w_train, decoder_b_train = get_layer_weights(decoder[0])