def compute_connectivity_from_single_neuron(X, selected_neuron):
    """
    Computes the connectivity matrix from a single neuron neurons using correlations

    Args:
        X (ndarray): the matrix of activities
        selected_neuron (int): the index of the selected neuron

    Returns:
        estimated_connectivity (ndarray): estimated connectivity for the selected neuron, of shape (n_neurons,)
    """

    # Extract the current activity of selected_neuron, t
    current_activity = X[selected_neuron, :-1]

    # Extract the observed outcomes of all the neurons
    next_activity = X[:, 1:]

    # Initialize estimated connectivity matrix
    estimated_connectivity = np.zeros(n_neurons)

    # Loop through all neurons
    for neuron_idx in range(n_neurons):

        # Get the activity of neuron_idx
        this_output_activity = next_activity[neuron_idx]

        # Compute correlation
        correlation = np.corrcoef(this_output_activity, current_activity)[0, 1]

        # Store this neuron's correlation
        estimated_connectivity[neuron_idx] = correlation

    return estimated_connectivity

# Simulate a 6 neuron system for 5000 timesteps again.
n_neurons = 6
timesteps = 5000
selected_neuron = 1

# Invoke a helper function that generates our nxn causal connectivity matrix
A = create_connectivity(n_neurons)

# Invoke a helper function that simulates the neural activity
X = simulate_neurons(A, timesteps)

# Uncomment below to test your function
estimated_connectivity = compute_connectivity_from_single_neuron(X, selected_neuron)

with plt.xkcd():
  plot_true_vs_estimated_connectivity(estimated_connectivity, A, selected_neuron)