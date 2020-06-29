def get_coarse_corr(n_groups, X):
    """
    A wrapper function for our correlation calculations between coarsely sampled
    A and R.

    Args:
        n_groups (int): the number of groups. should divide the number of neurons evenly
        X: the simulated system

    Returns:
        A single float correlation value representing the similarity between A and R
    """
    
    # solution
    coarse_X = X.reshape(n_groups, n_neurons//n_groups, timesteps).mean(1)
    R = correlation_for_all_neurons(coarse_X)
    coarse_A = A.reshape(n_groups, n_neurons//n_groups, n_groups, n_neurons//n_groups).mean(3).mean(1)
    corr = np.corrcoef(coarse_A.flatten(), R.flatten())[0,1]

    return corr

n_neurons = 128
timesteps = 5000
n_trials = 3
groups = [2**i for i in range(2,int(np.log2(n_neurons)))]

corr_data = np.zeros((n_trials, len(groups)))

for trial in range(n_trials):
    print("Trial {} out of {}".format(trial, n_trials))
    A = create_connectivity(n_neurons,random_state=trial)
    X = simulate_neurons(A, timesteps, random_state=trial)
    for j, n_groups in enumerate(groups):
        corr_data[trial, j] = get_coarse_corr(n_groups, X)

with plt.xkcd():

    corr_mean = corr_data.mean(axis=0)
    corr_std = corr_data.std(axis=0)

    plt.plot(np.divide(n_neurons, groups), corr_mean)
    plt.fill_between(np.divide(n_neurons, groups),
                     corr_mean - corr_std,
                     corr_mean + corr_std,
                     alpha=.2)

    plt.ylim([-0.2,1])
    plt.xlabel("Number of neurons per group (out of {} total)".format(n_neurons), 
            fontsize=15)
    plt.ylabel("Correlation of estimated effective connectivity")
    plt.show()