x = np.arange(-10, 10, 0.1)

def calculate_prior_array(x_points, stim_array, p_indep,
                          prior_mean_common=.0, prior_sigma_common=.5,
                          prior_mean_indep=.0, prior_sigma_indep=10):
    """
        'common' stands for common
        'indep' stands for independent
    """

    prior_common = my_gaussian(x_points, prior_mean_common, prior_sigma_common)
    prior_indep = my_gaussian(x_points, prior_mean_indep, prior_sigma_indep)

    prior_mixed = (1 - p_indep) * prior_common + (p_indep * prior_indep)
    prior_mixed /= np.sum(prior_mixed)  # normalize

    prior_array = np.tile(prior_mixed, len(stim_array)).reshape(len(stim_array), -1)
    return prior_array

p_independent=.05
prior_array = calculate_prior_array(x, hypothetical_stim, p_independent)

with plt.xkcd():
  plot_myarray(prior_array,
               'Hypothesized position $x$', 'Brain encoded position $\~x$',
               'Prior as a fcn of $\~x$ : $p(x|\~x)$')