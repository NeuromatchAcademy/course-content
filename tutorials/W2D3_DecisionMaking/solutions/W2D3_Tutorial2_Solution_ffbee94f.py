
############
## Solution
############
save_vals = []
lls = []
for e in range(epochs):
    # Run E-step
    ll, gamma, xi = e_step(Y, psi, A, L, dt)    
    lls.append(ll)  # log the data log likelihood for current cycle

    if e % print_every == 0: print(f'epoch: {e:3d}, ll = {ll}')  # log progress

    # Calculate new initial probabilities
    psi_new = gamma[:, 0].sum(0) / n_trials 
    psi_new /= psi_new.sum()
    # Calculate new transition matrix
    A_new = xi.sum(0).sum(0) / gamma[:, :-1].sum(0).sum(0)[:,None]
    # Calculate new firing rates
    L_new = (np.swapaxes(Y, -1, -2) @ gamma).sum(0) / gamma.sum(0).sum(0) / dt

    dp, dA, dL = psi_new - psi, A_new - A, L_new - L # Calculate the difference of parameters for later interpolation/extrapolation
    # Calculate LLs and ECLLs for later plotting
    if e in plot_epochs:        
        b_min = -min([np.min(psi[dp > 0] / dp[dp > 0]), np.min(A[dA > 0] / dA[dA > 0]), np.min(L[dL > 0] / dL[dL > 0])])
        b_max = -max([np.max(psi[dp < 0] / dp[dp < 0]), np.max(A[dA < 0] / dA[dA < 0]), np.max(L[dL < 0] / dL[dL < 0])])
        b_min = np.max([.99 * b_min, b_lims[0]])
        b_max = np.min([.99 * b_max, b_lims[1]])    
        bs = np.linspace(b_min, b_max, num_plot_vals)
        bs = sorted(list(set(np.hstack((bs, [0, 1])))))
        bs = np.array(bs)
        lls_for_plot = []
        eclls_for_plot = []
        for i, b in enumerate(bs):
            print(f'  saving for plot: {b_min:5.2f} ≤ {b:5.2f} ≤ {b_max:5.2f} ({i + 1} of {len(bs)})\r', end='')
            ll = e_step(Y, psi + b * dp, A + b * dA, L + b * dL, dt)[0]
            lls_for_plot.append(ll)
            ecll = (gamma[:, 0] @ np.log(psi + b * dp) + (xi * np.log(A + b * dA)).sum(-1).sum(-1).sum(-1) + (gamma * ss.poisson((L + b * dL) * dt).logpmf(Y[..., None]).sum(-2)).sum(-1).sum(-1)).mean() / T / dt
            eclls_for_plot.append(ecll)
            if b == 0:
                diff_ll = ll - ecll
        lls_for_plot = np.array(lls_for_plot)
        eclls_for_plot = np.array(eclls_for_plot) + diff_ll
        save_vals.append((bs, lls_for_plot, eclls_for_plot))
        print('')
    # return new parameter 
    psi, A, L = psi_new, A_new, L_new
    
ll = e_step(Y, psi, A, L, dt)[0]
lls.append(ll)
print(f'epoch: {epochs:3d}, ll = {ll}')