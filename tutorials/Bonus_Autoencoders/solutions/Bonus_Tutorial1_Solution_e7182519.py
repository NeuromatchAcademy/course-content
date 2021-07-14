encoding_size = 32

model = nn.Sequential(
    nn.Linear(input_size, encoding_size),
    nn.ReLU(),
    # insert your code here to add the layer
    nn.Linear(encoding_size, input_size),
    # insert the activation function
    nn.Sigmoid()
    )

print(f'Model structure \n\n {model}')