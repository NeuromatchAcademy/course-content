
def markov_forward(p0,A):
    """
    Calculate the forward predictive distribution in a discrete Markov chain

    Args:
        p0 (numpy vector): a discrete probability vector
        A (numpy matrix): the transition matrix, A[i,j] means the prob. to switch FROM i TO j

    Returns:
        p1 (numpy vector): the predictive probabilities in next time step
    """
    p1 = A.T @ p0
    return p1 

def entropy_categorical(p_vec):
    """
    Calculate the entropy (base 2) given a Categorical distribution

    Args:
        p_vec (numpy vector): paramter that characterize a Categorical distribution. Should sum up to one (will not be checked in this function)

    Returns:
        H (float): the entropy of this distribution in bits
    """
    H = - (p_vec * np.log2(p_vec + 1e-12)).sum()
    return H 

def simulate_prediction_only(model, nstep):
    """
    Simulate the diffusion of HMM with no observations

    Args:
        model (hmm.GaussianHMM instance): the HMM instance
        nstep (int): total number of time steps to simulate(include initial time)

    Returns:
        inforloss_vec (numpy vector of float): the information loss at each time step
        marginal_list (list of numpy vector): the list of marginal probabilities
    """
    entropy_list = []
    marginal_list = []
    prob = model.startprob_
    for i in range(nstep):
        # calculate entropy
        entropy = entropy_categorical(prob)
        entropy_list.append(entropy)
        marginal_list.append(prob)  
        # one step forward
        prob = markov_forward(prob, model.transmat_)  
    # calculate information loss w.r.t initial time 
    entropy_vec = np.asarray(entropy_list)
    infoloss_vec = entropy_vec - entropy_vec[0]
    return infoloss_vec, marginal_list

T = 100
switch_prob = 0.1
model = my_create_model(switch_prob=switch_prob,noise_level=2)
information_loss, marginal_list = simulate_prediction_only(model, T)
with plt.xkcd():
    plot_info_loss(information_loss, switch_prob)