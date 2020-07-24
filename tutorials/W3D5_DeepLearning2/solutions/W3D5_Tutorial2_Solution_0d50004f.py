encoding_size = 2

model = nn.Sequential(
    nn.Linear(input_size, int(input_size / 2)),
    nn.PReLU(),
    nn.Linear(int(input_size / 2), encoding_size * 32),
    # Add activation function
    nn.PReLU(),
    # Add another layer
    nn.Linear(encoding_size * 32, encoding_size),
    # Add activation function
    nn.PReLU(),
    # Add another layer
    nn.Linear(encoding_size, encoding_size * 32),
    # Add activation function
    nn.PReLU(),
    # Add another layer
    nn.Linear(encoding_size * 32, int(input_size / 2)),
    # Add activation function
    nn.PReLU(),
    # Add another layer
    nn.Linear(int(input_size / 2), input_size),
    # Add activation function
    nn.Sigmoid()
    )

model[:-2].apply(init_weights_kaiming_normal)

print(f'Autoencoder \n\n {model}\n')

# Adjust the value n_l to split your model correctly
n_l = 6

# uncomment when you fill the code
encoder = model[:n_l]
decoder = model[n_l:]
print(f'Encoder \n\n {encoder}\n')
print(f'Decoder \n\n {decoder}')