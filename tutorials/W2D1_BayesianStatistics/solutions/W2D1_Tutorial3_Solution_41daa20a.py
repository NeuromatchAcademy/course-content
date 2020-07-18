def generate_input_array(x_points, stim_array, posterior_array,
                         mean=-2.5, sigma=1.):

    input_array = np.zeros_like(posterior_array)

    for i in range(len(x_points)):
        input_array[:, i] = my_gaussian(stim_array, mean, sigma)
        input_array[:, i] /= np.sum(input_array[:, i])
    
    return input_array

input_array = generate_input_array(x, hypothetical_stim, posterior_array)
with plt.xkcd():
  plot_myarray(input_array,
               'hypothetical stimulus $x$', '$\~x$',
               'Sample Input Matrix: $p(\~x | x = -2.5)$')