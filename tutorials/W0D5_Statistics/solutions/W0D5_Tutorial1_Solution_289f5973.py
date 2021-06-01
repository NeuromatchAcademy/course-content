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

# To check it works, draw 5 samples and print them
mu = 5
sigma = 1
x_5 = generate_normal_samples(mu, sigma, 5)
print("The samples drawn from the normal distribution are: " + str(x_5))

# Now, let's draw 20
x_20 = generate_normal_samples(mu, sigma, 20)

# Uncomment once you draw 20 samples to plot the data
xspace = np.linspace(0, 10, 100)
with plt.xkcd():
  plot_gaussian_samples_true(x_20, xspace, mu, sigma,
                        'orientation (degrees)', 'probability')