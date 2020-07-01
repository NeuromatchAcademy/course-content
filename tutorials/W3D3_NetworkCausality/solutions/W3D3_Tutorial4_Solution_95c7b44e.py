n_neurons = 20 # the size of the system
timesteps = 10000
n_trials = 3

etas = [2, 1, 0.5, 0.25, 0.12]

corr_data = np.zeros((n_trials, len(etas)))
for trial in range(n_trials):
    print("Trial {} of {}".format(trial+1, n_trials))
    for j, eta in enumerate(etas):
        # solution
        A, X, Z = simulate_neurons_iv(n_neurons, timesteps, eta, trial)
        iv_V = get_iv_estimate(X, Z)
        corr_data[trial, j] = np.corrcoef(A.flatten(), iv_V.flatten())[1,0]


# Visualize IV performance as instrument strength varies
with plt.xkcd():
    corr_mean = corr_data.mean(axis=0)
    corr_std = corr_data.std(axis=0)

    plt.plot(etas, corr_mean)
    plt.fill_between(etas,
                  corr_mean - corr_std,
                  corr_mean + corr_std,
                  alpha=.2)   
    plt.xlim([etas[0], etas[-1]])
    plt.title("IV performance as a function of instrument strength")
    plt.ylabel("Correlation b.t. IV and true connectivity")
    plt.xlabel("Strength of instrument (eta)")
    plt.show()