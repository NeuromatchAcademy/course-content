auditory = my_gaussian(x, mu_auditory, sigma_auditory)
visual = my_gaussian(x, mu_visual, sigma_visual)
posterior_pointwise = visual * auditory
posterior_pointwise /= posterior_pointwise.sum()

with plt.xkcd():
    fig = plt.figure(figsize=(fig_w, fig_h))
    my_plot(x, auditory, visual, posterior_pointwise)
    plt.title('Sample output')
    plt.show()