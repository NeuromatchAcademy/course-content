def get_granger_causality(X, selected_neuron, alpha=0.05):
    """
    Estimates the lag-1 granger causality of the given neuron on the other neurons in the system.

    Args:
        X (np.ndarray): the matrix holding our dynamical system of shape (n_neurons, timesteps)
        selected_neuron (int): the index of the neuron we want to estimate granger causality for
        alpha (float): Bonferroni multiple comparisons correction

    Returns:
        A tuple (reject_null, p_vals)
        reject_null (list): a binary list of length n_neurons whether the null was
            rejected for the selected neuron granger causing the other neurons
        p_vals (list): a list of the p-values for the corresponding Granger causality tests
    """
    n_neurons = X.shape[0]
    max_lag = 1

    reject_null = []
    p_vals = []

    for target_neuron in range(n_neurons):
        ts_data = X[[target_neuron, selected_neuron], :].transpose()

        res = grangercausalitytests(ts_data, maxlag=max_lag, verbose=False)

        # Gets the p-value for the log-ratio test
        pval = res[1][0]['lrtest'][1]

        p_vals.append(pval)
        reject_null.append(int(pval < alpha))

    return reject_null, p_vals


# Set up small system
n_neurons = 6
timesteps = 5000
random_state = 42
selected_neuron = 1

A = create_connectivity(n_neurons, random_state)
X = simulate_neurons(A, timesteps, random_state)

# Uncomment below to test your function
reject_null, p_vals = get_granger_causality(X, selected_neuron)
with plt.xkcd():
  compare_granger_connectivity(A, reject_null, selected_neuron)