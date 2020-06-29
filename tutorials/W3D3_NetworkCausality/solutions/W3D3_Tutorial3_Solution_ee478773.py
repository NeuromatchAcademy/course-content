def get_regression_estimate(X, neuron_idx):
    """
    Estimates the connectivity matrix using lasso regression.

    Args:
        X (np.ndarray): our simulated system of shape (n_neurons, timesteps)
        neuron_idx (int):  a neuron index to compute connectivity for
    Returns:
        V (np.ndarray): estimated connectivity matrix of shape (n_neurons, n_neurons).
                        if neuron_idx is specified, V is of shape (n_neurons,).
    """
    n_neurons = X.shape[0]

    # Extract Y and W as defined above
    W = X[:, :-1].transpose()
    Y = X[[neuron_idx], 1:].transpose()
    # apply inverse sigmoid transformation
    Y = logit(Y)

    # fit regression
    # solution
    regression = Lasso(fit_intercept=False, alpha=0.01)   

    regression.fit(W,Y)

    V = regression.coef_

    return V