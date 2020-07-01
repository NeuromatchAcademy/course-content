def get_iv_estimate(X,Z):
    """
    Estimates the connectivity matrix from 2-stage least squares regression 
    using an instrument

    Args:
        X (np.ndarray): our simulated system of shape (n_neurons, timesteps)
        Z (np.ndarray): our observed instruments of shape (n_neurons, timesteps)

    Returns:
    
        V (np.ndarray): the estimated connectivity matrix
    """
    n_neurons = X.shape[0]
    # stage 1: regress X on Z
    stage1 = MultiOutputRegressor(LinearRegression(fit_intercept=True), n_jobs=-1)
    stage1.fit(Z.transpose(), X.transpose())
    X_hat = stage1.predict(Z.transpose())

    Y = X[:, 1:].transpose()
    # apply inverse sigmoid transformation
    Y = logit(Y)
    
    X_hat = X_hat[:-1, :]

    # stage 2: regress Y on X_hat
    # solution
    stage2 = MultiOutputRegressor(LinearRegression(fit_intercept=True), n_jobs=-1)
    stage2.fit(X_hat,Y)

    V = np.zeros((n_neurons, n_neurons))

    for i, estimator in enumerate(stage2.estimators_):
        V[i, :] = estimator.coef_

    return V

# Now let's examine IV estimates in a small system
n_neurons = 6
timesteps = 10000
random_state = 42
eta = 2

A, X, Z = simulate_neurons_iv(n_neurons, timesteps, eta, random_state)
V = get_iv_estimate(X,Z)
print("IV estimated correlation: {:.3f}".format(np.corrcoef(A.flatten(), V.flatten())[1,0]))

with plt.xkcd():
    fig, axs = plt.subplots(1,2, figsize=(10,5)) 

    im = axs[0].imshow(A, cmap="coolwarm")
    fig.colorbar(im, ax=axs[0],fraction=0.046, pad=0.04)
    axs[0].title.set_text("True connectivity matrix")

    im = axs[1].imshow(V, cmap="coolwarm")
    fig.colorbar(im, ax=axs[1],fraction=0.046, pad=0.04)
    axs[1].title.set_text("IV estimated connectivity matrix")
    plt.show()