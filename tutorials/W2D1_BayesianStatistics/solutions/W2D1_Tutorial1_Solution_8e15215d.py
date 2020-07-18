def compare_computational_analytical_means():
  x = np.arange(-10, 11, 0.1)

  # Fixed auditory likelihood
  mu_auditory = 3
  sigma_auditory = 1.5
  likelihood = my_gaussian(x, mu_auditory, sigma_auditory)

  # Varying visual prior
  mu_visuals = np.linspace(-10, 10)
  sigma_visual = 1.5

  # Accumulate results here
  mus_by_integration = []
  mus_analytical = []

  for mu_visual in mu_visuals:
    prior = my_gaussian(x, mu_visual, sigma_visual)
    posterior = compute_posterior_pointwise(prior, likelihood)

    ############################################################################
    ## Add code that will find the posterior mean via numerical integration
    #
    ############################################################################
    mu_integrated = np.sum(x*posterior)

    ############################################################################
    ## Add more code below that will calculate the posterior mean analytically
    #
    # Comment out the line below to test your solution
    #raise NotImplementedError("Please add code to find the mean both ways first")
    ############################################################################
    mu_analytical = ((mu_auditory / sigma_auditory ** 2 + mu_visual / sigma_visual ** 2) / 
                  (1 / sigma_auditory ** 2 + 1 / sigma_visual ** 2))
        
    mus_by_integration.append(mu_integrated)
    mus_analytical.append(mu_analytical)

  return mu_visuals, mus_by_integration, mus_analytical


# Uncomment the lines below to visualize your results
mu_visuals, mu_computational, mu_analytical = compare_computational_analytical_means()

with plt.xkcd():
  plot_visual(mu_visuals, mu_computational, mu_analytical)