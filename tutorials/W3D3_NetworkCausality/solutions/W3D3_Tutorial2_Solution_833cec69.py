def compute_connectivity_single_neuron(X, selected_neuron):
    """
    Computes the connectivity matrix for a single neuron neurons using correlations

    Args:
        X: the matrix of activities
    Returns:
        estimated_connectivity (np.ndarray): estimated connectivity for the selected neuron, of shape (n_neurons,)
    """

    next_activity = X[selected_neuron, 1:] # extract the next activities of a neuron, t+1
    current_activity = X[:, :-1] # extract the current activity, t

    estimated_connectivity = np.zeros(n_neurons) # our stored estimated connectivity matrix

    for neuron_idx in range(n_neurons):
        this_input_activity = current_activity[neuron_idx]

        # solution
        correlation = np.corrcoef(this_input_activity, current_activity)[0,1]

        estimated_connectivity[neuron_idx] = correlation

    return estimated_connectivity

# Simulate a 6 neuron system for 5000 timesteps again.
n_neurons = 6
timesteps = 5000
A = create_connectivity(n_neurons)

X = simulate_neurons(A, timesteps)

estimated_connectivity = compute_connectivity_single_neuron(X,1)

with plt.xkcd():
    fig, axs = plt.subplots(1,2, figsize=(10,5))
    plot_connectivity_matrix(X[:, [1]], ax=axs[0])
    axs[0].set_xticklabels([1])
    axs[0].set_title("True connectivity for neuron 1")

    plot_connectivity_matrix(np.expand_dims(estimated_connectivity, axis=1), ax=axs[1])
    axs[1].set_xticklabels([1])
    axs[1].set_title("Estimated connectivity for neuron 1")
    plt.show()