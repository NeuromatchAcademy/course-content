def my_gaussian(x_points, mu, sigma):
    """
    Returns normalized Gaussian estimated at points `x_points`, with parameters:
     mean `mu` and std `sigma`
    
    Args:
        x_points (numpy array of floats): points at which the gaussian is
                                          evaluated
        mu (scalar): mean of the Gaussian
        sigma (scalar): std of the gaussian
    
    Returns: 
        (numpy array of floats) : normalized Gaussian evaluated at `x`
    """
    px = np.exp(- 1/2/sigma**2 * (mu - x_points) ** 2)
    px = px / px.sum() # this is the normalization: this part ensures the sum of
                       # the individual probabilities at each `x` add up to one.
                       # It makes a very strong assumption though:
                       # That the `x_points` cover the big portion of 
                       # probability mass around the mean.
                       # Please think/discuss when this would be a dangerous 
                       # assumption.
                       # E.g.: What do you think will happen to the values on 
                       # the y-axis 
                       # if the `x` values (x_point) range from -1 to 8 instead 
                       # of -8 to 8?
    return px

x = np.arange(-8, 9, 0.1)

px = my_gaussian(x, -1, 1)

with plt.xkcd():
  my_plot_single(x, px)
