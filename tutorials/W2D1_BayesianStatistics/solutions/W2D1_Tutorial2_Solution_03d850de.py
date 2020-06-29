
x = np.arange(-10, 11, 0.1)

prior_mean = 0.
prior_sigma1  = .5
prior_sigma2  = 3.
prior1 = my_gaussian(x, prior_mean, prior_sigma1)
prior2 = my_gaussian(x, prior_mean, prior_sigma2)

alpha = 0.05
prior_combined = (1-alpha) * prior1 + (alpha * prior2) 
prior_combined = prior_combined / np.sum(prior_combined)

with plt.xkcd():
    fig = plt.figure(figsize=(fig_w*1.2, fig_h*1.2))
    plot_my_composed_prior(
        x,
        prior1/np.sum(prior1),
        prior2/np.sum(prior2),
        prior_combined
    )
    plt.title('Sample output')
    plt.show()