
def simulate_info_gain(model,T):
    """
    Given HMM `model`, generate a sequence of observations from first component, and 
    calculate posterior marginal predictions and corresponding information gain(compared to no evidence) 
    of x_t for T-1 time steps ahead based on generated evidence

    Args:
        model (GaussianHMM instance): the HMM
        T (int): length of returned array

    Returns:
        posterior_probs (list of numpy vectors): the list of marginal probs. from time 0 to T-1
        information_gains (numpy array of floats): entropy decrease w.r.t no evidence
        information_losses (numpy array of floats): entropy increase w.r.t first time step
    """
    # First re-calculate the information loss for current model 
    information_losses, predictive_probs = simulate_prediction_only(model, T)
    # Generate an observation trajectory condtioned on that latent state x is always 1
    Y = np.asarray([model._generate_sample_from_state(0) for _ in range(T)])
    # Calculate marginal for each latent state x_t 
    pt = np.exp(model._compute_log_likelihood(Y[0:1]))[0] * model.startprob_
    pt /= np.sum(pt)
    posterior_probs = [pt]
    for t in range(1,T):
        prediction = model.transmat_ @ posterior_probs[t-1]
        likelihood = np.exp(model._compute_log_likelihood(Y[t:t+1]))[0]
        posterior = prediction * likelihood
        posterior /= np.sum(posterior)
        
        posterior_probs.append(posterior)

    # Calculate entropy for each posterior marginal 
    posterior_entropies = np.asarray(list(map(entropy_categorical,posterior_probs)))
    # Calculate infomation gain 
    information_gains = information_losses - posterior_entropies
    return posterior_probs, information_gains, information_losses

switch_prob = 0.06 
noise_level = 1.2
nsample = 50 
T = 160  
model = my_create_model(switch_prob, noise_level)

info_gain_list = [] 
for i in range(nsample):
    posterior_probs, information_gains, information_losses = simulate_info_gain(model,T)
    info_gain_list.append(information_gains)
info_gain_matrix = np.asarray(info_gain_list)


with plt.xkcd():
    plot_info_gain(info_gain_matrix, information_losses)