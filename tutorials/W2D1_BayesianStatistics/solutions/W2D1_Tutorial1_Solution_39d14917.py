def compute_posterior_pointwise(prior, likelihood):
  ##############################################################################
  # Write code to compute the posterior from the prior and likelihood via
  # pointwise multiplication. (You may assume both are defined over the same x-axis)
  #
  # Comment out the line below to test your solution
  # raise NotImplementedError("Finish the simulation code first")
  ##############################################################################
  
  posterior = prior * likelihood
  posterior /= posterior.sum()

  return posterior


def localization_simulation(mu_auditory=3.0, sigma_auditory=1.5,
                            mu_visual=-1.0, sigma_visual=1.5):
  
  ##############################################################################
  ## Using the x variable below,
  ##      create a gaussian called 'auditory' with mean 3, and std 1.5
  ##      create a gaussian called 'visual' with mean -1, and std 1.5
  #
  ## Comment out the line below to test your solution
  #raise NotImplementedError("Finish the simulation code first")
  ###############################################################################
  x = np.arange(-8, 9, 0.1)

  auditory = my_gaussian(x, mu_auditory, sigma_auditory)
  visual = my_gaussian(x, mu_visual, sigma_visual)
  posterior = compute_posterior_pointwise(auditory, visual)
  
  return x, auditory, visual, posterior


# Uncomment the lines below to plot the results
x, auditory, visual, posterior_pointwise = localization_simulation()

with plt.xkcd():
  posterior_plot(x, auditory, visual, posterior_pointwise)