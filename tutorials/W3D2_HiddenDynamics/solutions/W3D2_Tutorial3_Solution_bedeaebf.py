
# Set random seed
np.random.seed(0)

# Set parameters
T = 50                  # Time duration
tau = 25                # dynamics time constant
process_noise = 2       # process noise in Astrocat's propulsion unit (standard deviation)
measurement_noise = 9   # measurement noise in Astrocat's collar (standard deviation)

# Auxiliary variables
process_noise_cov = process_noise**2          # process noise in Astrocat's propulsion unit (variance)
measurement_noise_cov = measurement_noise**2  # measurement noise in Astrocat's collar (variance)

# Initialize arrays
t = np.arange(0, T, 1)   # timeline
s = np.zeros(T)          # states
D = np.exp(-1/tau)       # dynamics multiplier (matrix if s is vector)

m = np.zeros(T)          # measurement
s_ = np.zeros(T)         # estimate (posterior mean)
cov_ = np.zeros(T)       # uncertainty (posterior covariance)

# Initial guess of the posterior at time 0
initial_guess = gaussian(0, process_noise_cov/(1-D**2))    # In this case, the initial guess (posterior distribution
                                                           # at time 0) is the equilibrium distribution, but feel free to
                                                           # experiment with other gaussians
posterior = initial_guess

# Sample initial conditions
s[0] = posterior.mean + np.sqrt(posterior.cov) * np.random.randn()   # Sample initial condition from posterior distribution at time 0
s_[0] = posterior.mean
cov_[0] = posterior.cov

# Loop over steps
for i in range(1, T):

    # Sample true states and corresponding measurements
    s[i] = D * s[i-1] + np.random.normal(0, process_noise)    # variable `s` records the true position of Astrocat
    m[i] = s[i] + np.random.normal(0, measurement_noise)      # variable `m` records the measurements of Astrocat's collar

    # Step 1. Shift yesterday's posterior to match the deterministic change of the system's dynamics,
    #         and broad it to account for the random change (i.e., add mean and variance of process noise).
    todays_prior = gaussian(D * posterior.mean, D**2 * posterior.cov + process_noise_cov)

    # Step 2. Now that yesterday's posterior has become today's prior, integrate new evidence
    #         (i.e., multiply gaussians from today's prior and likelihood)
    likelihood = gaussian(m[i], measurement_noise_cov)

    # Step 2a:  To find the posterior variance, add informations (inverse variances) of prior and likelihood
    info_prior = 1/todays_prior.cov
    info_likelihood = 1/likelihood.cov
    info_posterior = info_prior + info_likelihood

    # Step 2b: To find the posterior mean, calculate a weighted average of means from prior and likelihood;
    #          the weights are just the fraction of information that each gaussian provides!
    prior_weight = info_prior / info_posterior
    likelihood_weight = info_likelihood / info_posterior
    posterior_mean = prior_weight * todays_prior.mean  +  likelihood_weight * likelihood.mean

    # Don't forget to convert back posterior information to posterior variance!
    posterior_cov = 1/info_posterior
    posterior = gaussian(posterior_mean, posterior_cov)

    s_[i] = posterior.mean
    cov_[i] = posterior.cov

# Visualize
with plt.xkcd():
  paintMyFilter(D, initial_guess, process_noise_cov, measurement_noise_cov, s, m, s_, cov_)