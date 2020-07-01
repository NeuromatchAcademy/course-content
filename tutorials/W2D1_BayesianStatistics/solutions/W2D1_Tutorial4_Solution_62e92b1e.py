
def my_Bayes_model_mse(params):
  """ Function fits the Bayesian model from Tutorial 4 
  
  Args : 
    params (list of positive floats):  parameters used by the model (params[0]  = posterior scaling)
            
  Returns :
    (scalar) negative log-likelihood :sum of log probabilities
  """
  trial_ll = np.zeros_like(true_stim)

  ## Create the prior Matrix outside of trial loop
  alpha=params[0]
  prior_mean = 0
  prior_sigma1  = 0.5
  prior_sigma2  = 3
  prior1 = my_gaussian(x, prior_mean, prior_sigma1)
  prior2 = my_gaussian(x, prior_mean, prior_sigma2)
  prior_combined = (1-alpha) * prior1 + (alpha * prior2) 
  prior_combined = prior_combined / np.sum(prior_combined)
  prior_matrix = np.tile(prior_combined, hypothetical_stim.shape[0]).reshape((hypothetical_stim.shape[0],-1))

  ## Create posterior matrix outside of trial loop
  posterior_matrix = np.zeros_like(likelihood_matrix)
  for i_posterior in np.arange(posterior_matrix.shape[0]):
      posterior_matrix[i_posterior,:] = np.multiply(prior_matrix[i_posterior,:], likelihood_matrix[i_posterior,:])
      posterior_matrix[i_posterior,:] = posterior_matrix[i_posterior,:] / np.sum(posterior_matrix[i_posterior,:])

  ## Create Binary decision matrix outside of trial loop
  binary_decision_matrix = np.zeros_like(posterior_matrix)
  for i_posterior in np.arange(posterior_matrix.shape[0]):
      mean, _, _ = moments_myfunc(x, posterior_matrix[i_posterior,:])
      idx = np.argmin(np.abs(x - mean))
      binary_decision_matrix[i_posterior,idx] = 1 

  # Loop over stimuli
  for i_stim in np.arange(true_stim.shape[0]):
    input_matrix = np.zeros_like(posterior_matrix)
    for i in np.arange(x.shape[0]):
      input_matrix[:, i] = my_gaussian(hypothetical_stim, true_stim[i_stim], 1)
      input_matrix[:, i] = input_matrix[:, i] / np.sum(input_matrix[:, i])

    marginalization_matrix = input_matrix * binary_decision_matrix

    marginal = np.sum(marginalization_matrix, axis=0)
    marginal = marginal / np.sum(marginal)

    action = behaviour[i_stim]
    idx = np.argmin(np.abs(x - action))

    trial_ll[i_stim] = np.log(marginal[idx] + np.finfo(float).eps)

  neg_ll = -np.sum(trial_ll)

  return neg_ll

with plt.xkcd():
  plot_my_bayes_model(my_Bayes_model_mse)