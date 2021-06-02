def calculate_binary_decision_array(x_points, posterior_array):

    binary_decision_array = np.zeros_like(posterior_array)

    for i in range(len(posterior_array)):
        # calculate mean of posterior using 'moments_myfunc'
        mean, _, _ = moments_myfunc(x_points, posterior_array[i])
        # find the postion of mean in x_points (closest position)
        idx = np.argmin(np.abs(x_points - mean))
        binary_decision_array[i, idx] = 1

    return binary_decision_array

binary_decision_array = calculate_binary_decision_array(x, posterior_array)
with plt.xkcd():
  plot_myarray(binary_decision_array,
               'Chosen position $\hat x$', 'Brain-encoded Stimulus $\~ x$',
               'Sample Binary Decision Array')