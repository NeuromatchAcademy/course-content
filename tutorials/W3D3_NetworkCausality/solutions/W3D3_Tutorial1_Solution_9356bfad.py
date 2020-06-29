def simulate_neurons(A, timesteps, random_state=42):
    """
    Simulates a dynamical system for the specified number of neurons and timesteps.

    Args:
        A (np.array): the connectivity matrix
        timesteps (int): the number of timesteps to simulate our system.
        random_state (int): random seed for reproducibility
        
    Returns:
        - X has shape (n_neurons, timeteps). A schematic:
                   ___t____t+1___
                  |   0    1     |
                  |   1    0     |
       n_neurons  |   0 -> 1     |
                  |   0    0     |
                  |___1____0_____|

    """
    np.random.seed(random_state)
    
    n_neurons = len(A)
    X = np.zeros((n_neurons, timesteps))

    for t in range(timesteps-1):
        # solution
        epsilon = np.random.multivariate_normal(np.zeros(n_neurons), np.eye(n_neurons))
        X[:, t+1] = sigmoid(A.dot(X[:,t]) + epsilon) # we are using helper function sigmoid

        assert epsilon.shape == (n_neurons,)
    return X

### Now test it
timesteps = 5000 # Simulate for 5000 timesteps.

# Simulate our dynamical system for the given amount of time
X = simulate_neurons(A, timesteps)
with plt.xkcd():
  f, ax = plt.subplots()
  ax.imshow(X[:,:10])
  ax.set(xlabel='Timestep', ylabel='Neuron', title='Simulated Neural Activity')