def get_coarse_corr(n_groups, X):
    """
    A wrapper function for our correlation calculations between coarsely sampled
    A and R.

    Args:
        n_groups (int): the number of groups. should divide the number of neurons evenly
        X: the simulated system

    Returns:
        A single float correlation value representing the similarity between A and R
        ndarray: estimated connectivity matrix
        ndarray: true connectivity matrix
    """

    coarse_X = X.reshape(n_groups, n_neurons // n_groups, timesteps).mean(1)

    # Make sure coarse_X is the right shape
    assert coarse_X.shape == (n_groups, timesteps)

    # Estimate connectivity from coarse system
    R = correlation_for_all_neurons(coarse_X)

    # Compute true coarse connectivity
    coarse_A = A.reshape(n_groups, n_neurons // n_groups, n_groups, n_neurons // n_groups).mean(3).mean(1)

    # Compute true vs estimated connectivity correlation
    corr = np.corrcoef(coarse_A.flatten(), R.flatten())[0, 1]

    return corr, R, coarse_A


n_groups = 16

# Uncomment below to test your function
corr, R, coarse_A = get_coarse_corr(n_groups, X)
plot_true_vs_estimated_connectivity(R, coarse_A)
print("Correlation: {}".format(corr))