encoding_size = 3

model = nn.Sequential(nn.Linear(input_size, int(input_size/2)),
                      nn.PReLU(),
                      nn.Linear(int(input_size/2), encoding_size*32),
                      nn.PReLU(),
                      nn.Linear(encoding_size*32, encoding_size),
                      nn.PReLU(),
                      NormalizeLayer(),
                      nn.Linear(encoding_size, encoding_size*32),
                      nn.PReLU(),
                      nn.Linear(encoding_size*32, int(input_size/2)),
                      nn.PReLU(),
                      nn.Linear(int(input_size/2), input_size),
                      nn.Sigmoid())

# Adjust the values to separate correctly your model
encoder = model[:7]
decoder = model[7:]

print('Autoencoder', '\n\n', model)
print('Encoder', '\n\n', encoder)
print('Decoder', '\n\n', decoder)