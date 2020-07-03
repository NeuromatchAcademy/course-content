
encoding_size = 16

model = nn.Sequential(nn.Linear(input_size, encoding_size),
                      nn.PReLU(),
                      nn.Linear(encoding_size, input_size),
                      nn.Sigmoid())

print(model)