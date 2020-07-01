
def threshold_from_errorrate(alpha):
    """
    Calculate log likelihood ratio threshold from desired error rate `alpha`

    Args:
        alpha (float): in (0,1), the desired error rate

    Return:
        threshold: corresponding evidence threshold
    """
    threshold = np.log((1-alpha)/alpha)
    return threshold

def simulate_SPRT_threshold(sigma, threshold , true_dist=1, batch_size=100):
    """
    Simulate a Sequential Probability Ratio Test with thresholding stopping rule.
    Two observation models are 1D Gaussian distributions N(1,sigma^2) and N(-1,sigma^2).

    Args:
        sigma (float): standard deviation 
        threshold (float): desired log likelihood ratio threshold to achieve before making decision
        batch_size (int): generate and process data in batches instead of serially for speed. The size of each batch

    Returns:
        evidence_history (numpy vector): the history of cumulated evidence given generated data
        decision (int): 1 for pR, 0 for pL 
        data (numpy vector): the generated sequences of data in this trial 
    """
    muL = -1.0
    muR = 1.0 
    
    pL = stats.norm(muL, sigma) 
    pR = stats.norm(muR, sigma)

    has_enough_data = False 
    
    data = np.zeros(0)  
    evidence_history = np.zeros(0)
    current_evidence = 0.0
    while not has_enough_data:
        # generate a batch of data 
        if true_dist == 1:
            data_batch = pR.rvs(size=batch_size)
        else: 
            data_batch = pL.rvs(size=batch_size)

        # individual log likelihood ratios
        ll_batch = log_likelihood_ratio(data_batch, pL, pR)
        # cumulated evidence for this batch
        evidence_history_batch = np.cumsum(ll_batch) + current_evidence
        # update the collection of all data
        data = np.concatenate([ data, data_batch])
        # update the collection of all cumulated evidence history
        evidence_history = np.concatenate([evidence_history, evidence_history_batch])
        current_evidence = evidence_history[-1]
        
        # check if we've got enough data
        if np.abs(current_evidence) > threshold:
            has_enough_data = True 

    # find earliest time to cross threshold
    id_crossing = np.argmax( np.abs(evidence_history)> threshold)
    # discard redundant data because of batching
    if len(data)-1 > id_crossing:
        data = data[:id_crossing + 1]
        evidence_history = evidence_history[:id_crossing+1]

    # Make decision 
    if evidence_history[-1] >0:
        decision = 1
    elif evidence_history[-1] <0:
        decision = 0 
    else: 
        decision = np.random.randint(2)

    return evidence_history, decision, data



sigma = 3.35  
num_sample = 10
log10_alpha = -4  #log10(alpha)
alpha = np.power(10.0,log10_alpha)

simulate_and_plot_SPRT_fixedthreshold(sigma, num_sample, alpha)