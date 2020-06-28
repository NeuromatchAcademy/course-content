
x = np.arange(-10,11,0.1)

visual_mean = np.arange(-8,9,0.2)
visual_sigma  = 1

mode_posterior = np.zeros_like(visual_mean)

for i_visual in np.arange(visual_mean.shape[0]):
    visual = my_gaussian(x, visual_mean[i_visual], visual_sigma)

    posterior_pointwise = prior_combined * visual
    mode_posterior[i_visual] = x[np.argmax(posterior_pointwise)]
    #my_dynamic_plot(x, prior_combined, visual/visual.sum(), posterior_pointwise/posterior_pointwise.sum())

with plt.xkcd():
    fig = plt.figure(figsize=(fig_w, 2*fig_h))
    plt.subplot(2, 1, 1)
    plt.plot(x, prior_combined, '-r', LineWidth=2, label='Prior')
    plt.plot(x, visual/np.sum(visual), '-b', LineWidth=2, label='Likelihood')
    plt.plot(x, posterior_pointwise/np.sum(posterior_pointwise), '-g', LineWidth=2, label='Posterior')
    plt.ylabel('Probability')
    plt.xlabel('Orientation (Degrees)')
    plt.legend()  
    plt.title('Sample output')
    plt.subplot(2, 1, 2)
    plt.plot(visual_mean, mode_posterior, '-r', label='Mode')
    plt.legend()
    plt.xlabel('Visual stimulus position')
    plt.ylabel('Posterior mode')
    plt.tight_layout()
    plt.show()