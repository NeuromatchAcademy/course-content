
def my_gaussian(x_points, mu, sigma):
  """ Returns normalized Gaussian estimated at points `x_points`, with parameters:
  mean `mu` and standard deviation `sigma`

  Args:
      x_points (ndarray of floats): points at which the gaussian is evaluated
      mu (scalar): mean of the Gaussian
      sigma (scalar): standard deviation of the gaussian

  Returns:
      (numpy array of floats) : normalized Gaussian evaluated at `x`
  """
  px = 1/(2*np.pi*sigma**2)**1/2 *np.exp(-(x_points-mu)**2/(2*sigma**2))

  # as we are doing numerical integration we may have to remember to normalise
  # taking into account the stepsize (0.1)
  px = px/(0.1*sum(px))
  return px

def compute_posterior_pointwise(prior, likelihood):
  """ Compute the posterior probability distribution point-by-point using Bayes
  Rule.

    Args:
      prior (ndarray): probability distribution of prior
      likelihood (ndarray): probability distribution of likelihood

    Returns:
      posterior (ndarray): probability distribution of posterior
  """

  posterior = likelihood * prior
  posterior =posterior/ (0.1*posterior.sum())

  return posterior

def localization_simulation(mu_auditory = 3.0, sigma_auditory = 1.5,
                            mu_visual = -1.0, sigma_visual = 1.5):
  """ Perform a sound localization simulation with an auditory prior.

    Args:
      mu_auditory (float): mean parameter value for auditory prior
      sigma_auditory (float): standard deviation parameter value for auditory
                                prior
      mu_visual (float): mean parameter value for visual likelihood distribution
      sigma_visual (float): standard deviation parameter value for visual
                                likelihood distribution

    Returns:
      x (ndarray): range of values for which to compute probabilities
      auditory (ndarray): probability distribution of the auditory prior
      visual (ndarray): probability distribution of the visual likelihood
      posterior_pointwise (ndarray): posterior probability distribution
  """

  x = np.arange(-8, 9, 0.1)

  auditory = my_gaussian(x, mu_auditory, sigma_auditory)
  visual = my_gaussian(x, mu_visual, mu_visual)
  posterior = compute_posterior_pointwise(auditory, visual)

  return x, auditory, visual, posterior

# Uncomment the lines below to plot the results
x, auditory, visual, posterior_pointwise = localization_simulation()
with plt.xkcd():
  _ = posterior_plot(x, auditory, visual, posterior_pointwise)