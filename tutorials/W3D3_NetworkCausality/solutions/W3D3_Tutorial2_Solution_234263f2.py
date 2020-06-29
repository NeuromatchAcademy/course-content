n_groups = 16
coarse_X = X.reshape(n_groups, n_neurons//n_groups, timesteps).mean(1)

assert coarse_X.shape == (n_groups, timesteps)

R = correlation_for_all_neurons(coarse_X)
coarse_A = A.reshape(n_groups, n_neurons//n_groups, n_groups, n_neurons//n_groups).mean(3).mean(1)

with plt.xkcd():
    fig, axs = plt.subplots(1,2, figsize=(10,5))
    plot_connectivity_matrix(coarse_A, ax=axs[0])
    plot_connectivity_matrix(R, ax=axs[1])
    axs[0].set_title("Coarse connectivity matrix")
    axs[1].set_title("Estimated coarse connectivity matrix")
    plt.show()
    print("Correlation: {}".format(np.corrcoef(coarse_A.flatten(), R.flatten())[0,1]))