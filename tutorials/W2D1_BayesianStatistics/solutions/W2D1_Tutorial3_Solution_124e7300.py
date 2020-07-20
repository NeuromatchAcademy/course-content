def calculate_posterior_array(prior_array, likelihood_array):

    posterior_array = prior_array * likelihood_array
    posterior_array /= posterior_array.sum(axis=1, keepdims=True)

    return posterior_array

posterior_array = calculate_posterior_array(prior_array, likelihood_array)
with plt.xkcd():
  plot_myarray(posterior_array,
               'Hypothesized Position $x$',
               'Brain encoded Stimulus $\~x$',
               'Posterior as a fcn of $\~x$ : $p(x | \~x)$')