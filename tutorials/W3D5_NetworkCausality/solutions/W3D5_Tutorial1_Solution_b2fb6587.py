def simulate_neurons(A, timesteps, random_state=42):
    """Simulates a dynamical system for the specified number of neurons and timesteps.

    Args:
        A (np.array): the connectivity matrix
        timesteps (int): the number of timesteps to simulate our system.
        random_state (int): random seed for reproducibility

    Returns:
        - X has shape (n_neurons, timeteps). A schematic:
                   ___t____t+1___
       neuron  0  |   0    1     |
                  |   1    0     |
       neuron  i  |   0 -> 1     |
                  |   0    0     |
                  |___1____0_____|

    """
    np.random.seed(random_state)

    n_neurons = len(A)
    X = np.zeros((n_neurons, timesteps))

    for t in range(timesteps - 1):

        # Create noise vector
        epsilon = np.random.multivariate_normal(np.zeros(n_neurons), np.eye(n_neurons))

        # Update activity vector for next step
        X[:, t + 1] = sigmoid(A @ X[:, t] + epsilon)  # we are using helper function sigmoid

    return X


# Set simulation length
timesteps = 5000

# Uncomment below to test your function

# Simulate our dynamical system
X = simulate_neurons(A, timesteps)

with plt.xkcd():
  plot_neural_activity(X)