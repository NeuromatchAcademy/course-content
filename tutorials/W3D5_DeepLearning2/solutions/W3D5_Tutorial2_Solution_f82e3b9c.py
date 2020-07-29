encoding_size = 3

model = nn.Sequential(
    nn.Linear(input_size, int(input_size / 2)),
    nn.PReLU(),
    nn.Linear(int(input_size / 2), encoding_size * 32),
    nn.PReLU(),
    nn.Linear(encoding_size * 32, encoding_size),
    nn.PReLU(),
    # add the normalization layer
    NormalizeLayer(),
    nn.Linear(encoding_size, encoding_size * 32),
    nn.PReLU(),
    nn.Linear(encoding_size * 32, int(input_size / 2)),
    nn.PReLU(),
    nn.Linear(int(input_size / 2), input_size),
    nn.Sigmoid()
    )

model[:-2].apply(init_weights_kaiming_normal)

print(f'Autoencoder \n\n {model}\n')

# Adjust the value n_l to split your model correctly
n_l = 7

# uncomment when you fill the code
encoder = model[:n_l]
decoder = model[n_l:]
print(f'Encoder \n\n {encoder}\n')
print(f'Decoder \n\n {decoder}')