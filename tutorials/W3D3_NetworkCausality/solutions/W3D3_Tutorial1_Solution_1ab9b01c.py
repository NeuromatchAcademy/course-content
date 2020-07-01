def get_perturbed_connectivity_single_neuron(perturbed_X, perturb_freq, selected_neuron):
    """
    Computes the connectivity matrix for the selected neuron using differences in means.

    Args:
        perturbed_X (np.ndarray): the perturbed dynamical system matrix of shape (n_neurons, timesteps)
        perturb_freq (int): the perturbation frequency (2 means perturb every other timestep)
        selected_neuron (int): the index of the neuron we want to estimate connectivity for

    Returns:
        estimated_connectivity (np.ndarray): estimated connectivity for the selected neuron, of shape (n_neurons,)
    """
    neuron_perturbations = perturbed_X[selected_neuron, ::perturb_freq] # extract the perturbations of neuron 1
    all_neuron_output = perturbed_X[:, 1::perturb_freq] # extract the observed outcomes of all the neurons

    estimated_connectivity = np.zeros(n_neurons) # our stored estimated connectivity matrix

    for neuron_idx in range(n_neurons):
        selected_neuron_output = all_neuron_output[neuron_idx, :]
        one_idx = np.argwhere(neuron_perturbations == 1)
        zero_idx = np.argwhere(neuron_perturbations == 0)

        difference_in_means = np.mean(selected_neuron_output[one_idx]) - np.mean(selected_neuron_output[zero_idx])

        estimated_connectivity[neuron_idx] = difference_in_means

    return estimated_connectivity

# Initialize the system
n_neurons = 6  
timesteps = 5000 # Simulate for 5000 timesteps.
perturb_freq = 2 # perturb the system every other time step

# Simulate our perturbed dynamical system for the given amount of time
perturbed_X = simulate_neurons_perturb(A, timesteps, perturb_freq=perturb_freq)

# we'll measure the connectivity of neuron 1
selected_neuron = 1
estimated_connectivity = get_perturbed_connectivity_single_neuron(perturbed_X, perturb_freq, selected_neuron)

#Now plot
with plt.xkcd():
  fig, axs = plt.subplots(1,2, figsize=(10,5))
  plot_connectivity_matrix(np.expand_dims(estimated_connectivity, axis=1), ax=axs[0])
  axs[0].set(title="Estimated connectivity", ylabel="Neuron")
  plot_connectivity_matrix(A[:, [selected_neuron]], ax=axs[1])
  axs[1].set(title="True connectivity")