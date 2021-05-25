def get_perturbed_connectivity_from_single_neuron(perturbed_X, selected_neuron):
    """
    Computes the connectivity matrix from the selected neuron using differences in means.

    Args:
        perturbed_X (np.ndarray): the perturbed dynamical system matrix of shape (n_neurons, timesteps)
        selected_neuron (int): the index of the neuron we want to estimate connectivity for

    Returns:
        estimated_connectivity (np.ndarray): estimated connectivity for the selected neuron, of shape (n_neurons,)
    """
    # Extract the perturbations of neuron 1 (every other timestep)
    neuron_perturbations = perturbed_X[selected_neuron, ::2]

    # Extract the observed outcomes of all the neurons (every other timestep)
    all_neuron_output = perturbed_X[:, 1::2]

    # Initialize estimated connectivity matrix
    estimated_connectivity = np.zeros(n_neurons)

    # Loop over neurons
    for neuron_idx in range(n_neurons):

        # Get this output neurons (neuron_idx) activity
        this_neuron_output = all_neuron_output[neuron_idx, :]

        # Get timesteps where the selected neuron == 0 vs == 1
        one_idx = np.argwhere(neuron_perturbations == 1)
        zero_idx = np.argwhere(neuron_perturbations == 0)

        difference_in_means = np.mean(this_neuron_output[one_idx]) - np.mean(this_neuron_output[zero_idx])

        estimated_connectivity[neuron_idx] = difference_in_means

    return estimated_connectivity


# Initialize the system
n_neurons = 6
timesteps = 5000
selected_neuron = 1

# Simulate our perturbed dynamical system
perturbed_X = simulate_neurons_perturb(A, timesteps)


## Uncomment below to test your function

# Measure connectivity of neuron 1
estimated_connectivity = get_perturbed_connectivity_from_single_neuron(perturbed_X, selected_neuron)

with plt.xkcd():
  plot_true_vs_estimated_connectivity(estimated_connectivity, A, selected_neuron)