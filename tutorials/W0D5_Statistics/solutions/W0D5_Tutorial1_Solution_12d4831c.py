def generate_poisson_samples(lambda_val, num_samples):
  """ Generates a desired number of samples from a poisson distribution,
  Poisson(lambda).

  Args:
    lambda_val (scalar): parameter specifying the mean number of events in one "interval"
    num_samples (int): number of samples drawn from poisson distribution

  Returns:
    sampled_values (ndarray): a array of shape (samples, ) containing the samples
  """
  random_num_generator = default_rng(1)
  sampled_values = random_num_generator.poisson(lambda_val, num_samples)
  return sampled_values

# Let's draw 5 values to look at
spikes_samples_5 = generate_poisson_samples(4, 5)
print("The samples drawn from the Poisson distribution are " +
          str(spikes_samples_5))

# Now let's draw 10 samples and plot the histogram
spikes_samples_10 = generate_poisson_samples(4, 10)

# Uncomment once you've collected 10 samples
with plt.xkcd():
  count, bins = plot_hist(spikes_samples_10, 'Recorded spikes per second')