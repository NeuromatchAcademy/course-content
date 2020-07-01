############
## Solution
############
# sample n_frozen_trials state sequences
Xf = np.zeros(T, dtype=int)
Xf[0] = (psi.cumsum() > np.random.rand()).argmax()
for t in range(1, T):
    Xf[t] = (A[Xf[t - 1],:].cumsum() > np.random.rand()).argmax()

# switch to one-hot encoding of the state
Xf = np.eye(K, dtype=int)[Xf]  # (T,K)

# get the Y values
Rates = np.squeeze(L @ Xf[...,None]) * dt  # (T,C)
Rates = np.tile(Rates, [n_frozen_trials,1,1]) # (n_trials, T, C)
Yf = ss.poisson(Rates).rvs()  