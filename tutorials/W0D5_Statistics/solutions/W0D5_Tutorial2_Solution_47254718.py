
def generate_normal_samples(mu, sigma, num_samples):
  """ Generates a desired number of samples from a normal distribution,
  Normal(mu, sigma).

  Args:
    mu (scalar): mean parameter of the normal distribution
    sigma (scalar): standard deviation parameter of the normal distribution
    num_samples (int): number of samples drawn from normal distribution

  Returns:
    sampled_values (ndarray): a array of shape (samples, ) containing the samples
  """
  random_num_generator = default_rng(0)
  sampled_values = random_num_generator.normal(mu, sigma, num_samples)
  return sampled_values

def compute_likelihoods_normal(x, mean_vals, variance_vals):
  """ Computes the log-likelihood values given a observed data sample x, and
  potential mean and variance values for a normal distribution

    Args:
      x (ndarray): 1-D array with all the observed data
      mean_vals (ndarray): 1-D array with all potential mean values to
                              compute the likelihood function for
      variance_vales (ndarray): 1-D array with all potential variance values to
                              compute the likelihood function for

    Returns:
      likelihood (ndarray): 2-D array of shape (number of mean_vals,
                              number of variance_vals) for which the likelihood
                              of the observed data was computed
  """
  # Initialise likelihood collection array
  likelihood = np.zeros((mean_vals.shape[0], variance_vals.shape[0]))

  # Compute the likelihood for observing the gvien data x assuming
  # each combination of mean and variance values
  for idxMean in range(mean_vals.shape[0]):
    for idxVar in range(variance_vals.shape[0]):
      likelihood[idxVar,idxMean]= sum(np.log(norm.pdf(x, mean_vals[idxMean],
                                              variance_vals[idxVar])))

  return likelihood

# Generate data
mu = 5
sigma = 1  # since variance = 1, sigma = 1
x = generate_normal_samples(mu, sigma, 1000)

# You can calculate mean and variance through numpy as
print("This is the sample mean as estimated by numpy: " + str(np.mean(x)))
print("This is the sample standard deviation as estimated by numpy: " + str(np.std(x)))

# Let's look through possible mean and variance values for the highest likelihood
# using the compute_likelihood function
meanTest = np.linspace(1, 10, 10) # potential mean values to try
varTest = np.array([0.7, 0.8, 0.9, 1, 1.2, 1.5, 2, 3, 4, 5]) # potential variance values to try
likelihoods = compute_likelihoods_normal(x, meanTest, varTest)

# Uncomment once you've generated the samples and compute likelihoods
xspace = np.linspace(0, 10, 100)
with plt.xkcd():
  plot_gaussian_samples_true(x, xspace, mu, sigma, "x", "Count")
  plot_likelihoods(likelihoods, meanTest, varTest)