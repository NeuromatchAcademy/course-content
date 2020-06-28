auditory1 = my_gaussian(x, mu1_auditory, std_auditory)
auditory2 = my_gaussian(x, mu2_auditory, std_auditory)

auditory_bimodal = auditory1 + auditory2
auditory_bimodal = auditory_bimodal / np.sum(auditory_bimodal)
mode_posteriors = []

for mu_visual in mu_visuals:
    visual = my_gaussian(x, mu_visual, std_visual)
    posterior_pointwise = auditory_bimodal * visual
    mode_posteriors.append(x[posterior_pointwise.argmax()])

visual = my_gaussian(x, mu_visual, std_visual)
posterior_pointwise = auditory_bimodal * visual

with plt.xkcd():
    fig = plt.figure(figsize=(fig_w, 2*fig_h))

    # Plot the last instance that we tried.
    plt.subplot(2, 1, 1)
    my_plot(x,
        auditory_bimodal,
        visual,
        posterior_pointwise / np.sum(posterior_pointwise)
    )
    plt.title('Sample solution')

    plt.subplot(2, 1, 2)
    plt.plot(mu_visuals, mode_posteriors, '-g' , label='argmax')
    plt.xlabel('Visual stimulus position')
    plt.ylabel('Posterior max')
    plt.tight_layout()
    plt.show()