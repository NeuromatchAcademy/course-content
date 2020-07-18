def bimodal_prior(x, mu_1=-3, sigma_1=1, mu_2=3, sigma_2=1):
  ################################################################################
  ## Finish this function so that it returns a bimodal prior, comprised of the
  # sum of two Gaussians
  #
  # Comment out the line below to test out your solution
  #raise NotImplementedError("Please implement the bimodal prior")
  ################################################################################
  prior = my_gaussian(x, mu_1, sigma_1) + my_gaussian(x, mu_2, sigma_2)
  prior /= prior.sum()

  return prior
  

def posterior_mode(x, posterior):
  ################################################################################
  ## Finish this function so that it returns the location of the mode
  #
  # Comment out the line below to test out your solution
  #raise NotImplementedError("Please implement the bimodal prior")
  ################################################################################
  mode = x[np.argmax(posterior)]

  return mode


def multimodal_simulation(x, mus_visual, sigma_visual=1):
  """
  Simulate an experiment where bimodal prior is held constant while
  a Gaussian visual likelihood is shifted across locations.
  Args:
        x:            array of points at which prior/likelihood/posterior are evaluated
        mus_visual:   array of means for the Gaussian likelihood
        sigma_visual: scalar standard deviation for the Gaussian likelihood

  Returns:
    posterior_modes:  array containing the posterior mode for each mean in mus_visual
  """
  
  prior = bimodal_prior(x, -3, 1, 3, 1)
  posterior_modes = []

  for mu in mus_visual:
    likelihood = my_gaussian(x, mu, 3)
    posterior = compute_posterior_pointwise(prior, likelihood)

    p_mode = posterior_mode(x, posterior)
    posterior_modes.append(p_mode)

  return posterior_modes


x = np.arange(-10, 10, 0.1)
mus = np.arange(-8, 8, 0.05)
# Uncomment the lines below to visualize your results
posterior_modes = multimodal_simulation(x, mus, 1)
with plt.xkcd():
  multimodal_plot(x,
                  bimodal_prior(x, -3, 1, 3, 1),
                  my_gaussian(x, 1, 1),
                  mus, posterior_modes)