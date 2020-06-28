def my_gaussian(x_points, mu, sigma):
    """
    Returns normalized Gaussian estimated at points `x_points`, with parameters: mean `mu` and std `sigma`
    
    Args:
        x_points (numpy array of floats): points at which the gaussian is evaluated
        mu (scalar): mean of the Gaussian
        sigma (scalar): std of the gaussian
    
    Returns: 
        (numpy array of floats) : normalized Gaussian evaluated at `x`
    """
    px = np.exp(- 1/2/sigma**2 * (mu - x) ** 2)
    px = px / px.sum() # this is the normalization part with a very strong assumption, that
                       # x_points cover the big portion of probability mass around the mean.
                       # Please think/discuss when this would be a dangerous assumption.
    return px

px = my_gaussian(x, -1, 1)

with plt.xkcd():
    fig = plt.figure(figsize=(fig_w, fig_h))
    my_plot_single(
        x,
        px
    )
    plt.title('Sample output')
    plt.show()
