
############
## Solution
############
# EM doesn't guarantee the order of learnt latent states are the same as that of true model
#  so we need to sort learnt parameters

sort = []
for i in range(K):
    minval = np.inf
    for j in range(K):
        if np.abs(L_true[:, i] - L[:, j]).max() < minval:
            minval = np.abs(L_true[:, i] - L[:, j]).max()
            minj = j
    sort.append(minj)
psi = psi[sort]
A = A[sort]
A = A[:, sort]
L = L[:, sort]
