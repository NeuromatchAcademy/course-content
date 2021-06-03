def generate_input_array(x_points, stim_array, posterior_array,
                         mean=2.5, sigma=1.):

    input_array = np.zeros_like(posterior_array)

    for i in range(len(x_points)):
        input_array[:, i] = my_gaussian(stim_array, mean, sigma)

    return input_array

input_array = generate_input_array(x, hypothetical_stim, posterior_array)
with plt.xkcd():
  plot_myarray(input_array,
               'Hypothetical Stimulus $x$', '$\~x$',
               'Sample Distribution over Encodings:\n $p(\~x | x = 2.5)$')