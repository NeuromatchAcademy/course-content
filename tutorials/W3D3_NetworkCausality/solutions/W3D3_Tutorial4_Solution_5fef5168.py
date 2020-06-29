def simulate_neurons_iv(n_neurons, timesteps, eta, random_state=42):
    """
    Simulates a dynamical system for the specified number of neurons and timesteps.

    Args:
        n_neurons (int): the number of neurons in our system.
        timesteps (int): the number of timesteps to simulate our system.
        eta (float): the strength of the instrument
        random_state (int): seed for reproducibility
        
    Returns:
        The tuple (A,X,Z) of the connectivity matrix, simulated system, and instruments.
        - A has shape (n_neurons, n_neurons)
        - X has shape (n_neurons, timesteps)
        - Z has shape (n_neurons, timesteps)
    """
    np.random.seed(random_state)
    A = create_connectivity(n_neurons, random_state)

    X = np.zeros((n_neurons, timesteps))
    Z = np.random.choice([0,1], size=(n_neurons, timesteps))
    for t in range(timesteps-1):
      # solution
      IV_on_this_timestep = (eta * Z[:,t+1])


      X[:, t+1] = sigmoid(A.dot(X[:,t]) + IV_on_this_timestep + np.random.multivariate_normal(np.zeros(n_neurons), np.eye(n_neurons)))

    return A, X, Z

# let's visualize the dynamics
timesteps = 5000 # Simulate for 5000 timesteps.
n_neurons = 100 # the size of our system
eta = 2 # the strength of our instrument, higher is stronger
# Simulate our dynamical system for the given amount of time
A, X, Z = simulate_neurons_iv(n_neurons, timesteps, eta)
with plt.xkcd():
  plt.imshow(X[:, :10],aspect='auto')
  plt.colorbar()
  plt.ylabel("Neuron", fontsize=15)
  plt.xlabel("Timestep", fontsize=15);
  plt.title("Our dynamical system with an IV")