
def generate_binomial_samples(n, p, num_samples):
  """ Generates a desired number of samples from a binomial distribution,
  Binomial(n, p).

  Args:
    n (int): number of trials in binomial distribution
    p (float): probability of desired event occuring (should be between [0, 1])
    num_samples (int): number of samples drawn from binomial distribution

  Returns:
    sampled_values (ndarray): a array of shape (samples, ) containing the samples
  """
  random_num_generator = default_rng(0)
  sampled_values = random_num_generator.binomial(n, p, num_samples)
  return sampled_values

# Select parameters for conducting binomial trials
n = 10
p = 0.5

left_turn_samples_10 = generate_binomial_samples(n, p, 10)
print("The samples drawn from the binomial distribution are: "
                + str(left_turn_samples_10))

# Now draw 1000 samples by calling the function again
left_turn_samples_1000 = generate_binomial_samples(n, p, 1000)

# Uncomment once you've collected 1000 random samples
with plt.xkcd():
  count, bins = plot_hist(left_turn_samples_1000, 'Number of left turns in sample')