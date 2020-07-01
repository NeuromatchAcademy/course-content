
def e_step(Y, psi, A, L, dt):
    """
    Args:
        Y (numpy 3d array): tensor of recordings, has shape (n_trials, T, C)
        psi (numpy vector): initial probabilities for each state
        A (numpy matrix): transition matrix, A[i,j] represents the prob to switch from i to j. Has shape (K,K)
        L (numpy matrix): Poisson rate parameter for different cells. Has shape (C,K)
        dt (float): duration of a time bin
        
    Returns:
        ll (float): data log likelihood
        gamma (numpy 3d array): singleton marginal distribution. Has shape (n_trials, T, K)
        xi (numpy 4d array): pairwise marginal distribution for adjacent nodes . Has shape (n_trials, T-1, K, K)
    """
    n_trials = Y.shape[0]
    T = Y.shape[1]
    K = psi.size
    log_a = np.zeros((n_trials, T, K))
    log_b = np.zeros((n_trials, T, K))

    log_A = np.log(A)
    log_obs = ss.poisson(L * dt).logpmf(Y[..., None]).sum(-2)  # n_trials, T, K

    # forward pass
    log_a[:, 0] = log_obs[:, 0] + np.log(psi)
    for t in range(1, T):
        tmp = log_A + log_a[:, t - 1, :,None]  # (n_trials, K,K)
        maxtmp = tmp.max(-2)  # (n_trials,K)
        log_a[:, t] = log_obs[:, t] + maxtmp + np.log(np.exp(tmp - maxtmp[:, None]).sum(-2))

    # backward pass
    for t in range(T - 2, -1, -1):
        # tmp = log_A + log_b[:, t + 1, None] + log_obs[:, t + 1, :, None]
        tmp = log_A + log_b[:, t + 1, None] + log_obs[:, t + 1, None]
        maxtmp = tmp.max(-1)
        log_b[:, t] = maxtmp + np.log(np.exp(tmp - maxtmp[..., None]).sum(-1))

    # data log likelihood 
    maxtmp = log_a[:, -1].max(-1)
    ll = np.log(np.exp(log_a[:, -1] - maxtmp[:, None]).sum(-1)) + maxtmp
    
    # singleton and pairwise marginal distributions 
    gamma = np.exp(log_a + log_b - ll[:, None, None])
    xi = np.exp(log_a[:, :-1, :, None] + (log_obs + log_b)[:, 1:, None] + log_A - ll[:, None, None, None])

    return ll.mean() / T / dt, gamma, xi