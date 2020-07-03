
encoding_size = 2

model = nn.Sequential(nn.Linear(input_size, int(input_size/2)),
                      nn.PReLU(),
                      nn.Linear(int(input_size/2), encoding_size*32),
                      nn.PReLU(),
                      nn.Linear(encoding_size*32, encoding_size),
                      nn.PReLU(),
                      nn.Linear(encoding_size, encoding_size*32),
                      nn.PReLU(),
                      nn.Linear(encoding_size*32, int(input_size/2)),
                      nn.PReLU(),
                      nn.Linear(int(input_size/2), input_size),
                      nn.Sigmoid())

encoder = model[:6]
decoder = model[6:]

optimizer = optim.Adam(model.parameters())
criterion = nn.BCELoss()

print('Autoencoder', '\n\n', model)
print('Encoder', '\n\n', encoder)
print('Decoder', '\n\n', decoder)