with plt.xkcd():
  
    mu_posteriors = []
    max_posteriors = []

    for mu_visual in mu_visuals:
        max_posterior = compute_mode_posterior_multiply(x, 
                                                    mu_auditory, sigma_auditory, 
                                                    mu_visual, sigma_visual)

        mu_posterior = ((mu_auditory / sigma_auditory ** 2 + 
                        mu_visual / sigma_visual ** 2) / 
                        (1 / sigma_auditory ** 2 + 
                        1 / sigma_visual ** 2))
        
        mu_posteriors.append(mu_posterior)
        max_posteriors.append(max_posterior)

    plot_visual(mu_visuals, mu_posteriors, max_posteriors)
    plt.show()