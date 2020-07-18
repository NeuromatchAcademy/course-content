def mixture_prior(x, mean=0, sigma_common=0.5, sigma_independent=3, p_common=0.75):

  gaussian_common = my_gaussian(x, mean, sigma_common) 
  ###############################################################################
  ## Insert your code here to:
  ##   * Create a second gaussian representing the independent-cause component
  ##   * Combine the two priors, using the mixing weight p_common. Don't forget
  #      to normalize the result so it remains a proper probability density function
  #
  #    * Comment the line below to test out your function   
  #raise NotImplementedError("Please complete Exercise 1")
  ###############################################################################
  gaussian_independent = my_gaussian(x, mean, sigma_independent)
  
  mixture = p_common * gaussian_common + ((1-p_common) * gaussian_independent) 
  mixture = mixture / np.sum(mixture)
  
  return gaussian_common, gaussian_independent, mixture


x = np.arange(-10, 11, 0.1)

# Uncomment the lines below to visualize out your solution
common, independent, mixture = mixture_prior(x)
with plt.xkcd():
  plot_mixture_prior(x, common, independent, mixture)