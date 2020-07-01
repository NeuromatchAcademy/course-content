def log_likelihood_ratio(xvec,p0,p1):
    """
    Given a sequence(vector) of observed data, calculate the log of likelihood ratios under 
    distributions p0 and p1

    Args:
        xvec (numpy vector): a vector of scalar measurements 
        p0 (Gaussian random variable): a normal random variable with `logpdf` method 
        p1 (Gaussian random variable): a normal random variable with `logpdf` method 

    Returns:
        llvec: a vector of log likelihood ratios for each input data point
    """
    return p1.logpdf(xvec) - p0.logpdf(xvec)


def simulate_SPRT_fixedtime(sigma, stop_time, true_dist=1):
    """
    Simulate a Sequential Probability Ratio Test with fixed time stopping rule.
    Two observation models are 1D Gaussian distributions N(1,sigma^2) and N(-1,sigma^2).

    Args:
        sigma (float): standard deviation 
        stop_time (int): number of samples to take before stopping

    Returns:
        evidence_history (numpy vector): the history of cumulated evidence given generated data
        decision (int): 1 for pR, 0 for pL
        data (numpy vector): the generated sequences of data in this trial 
    """
    muL = -1.0
    muR = 1.0 
    
    pL = stats.norm(muL, sigma) 
    # student
    pR = stats.norm(muR, sigma)

    # Generate a random sequence of data 
    if true_dist == 1:
        data = pR.rvs(size=stop_time)
    else: 
        data = pL.rvs(size=stop_time)
    
    # Calculate cumulated evidence
    ll_vec = log_likelihood_ratio(data, pL, pR)
    evidence_history = np.cumsum(ll_vec)

    # Make decision
    if evidence_history[-1] >0:
        decision = 1
    elif evidence_history[-1] <0:
        decision = 0 
    else: 
        decision = np.random.randint(2)
    
    return evidence_history, decision, data 

sigma = 3.5  
num_sample = 10  # number of simulations to run for each stopping time
stop_time = 146 

with plt.xkcd():
  simulate_and_plot_SPRT_fixedtime(sigma, stop_time, num_sample)