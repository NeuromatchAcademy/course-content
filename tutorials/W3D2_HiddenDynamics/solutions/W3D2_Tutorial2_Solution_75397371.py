def create_model(switch_prob=0.1, noise_level=1e-8, startprob=[1.0, 0.0]):
    """Create an HMM with binary state variable and 1D Gaussian observations
    The probability to switch to the other state is `switch_prob`. Two
    observation models have mean 1.0 and -1.0 respectively. `noise_level`
    specifies the standard deviation of the observation models.

    Args:
        switch_prob (float): probability to jump to the other state
        noise_level (float): standard deviation of observation models. Same for
        two components

    Returns:
        model (hmm.GaussianHMM instance): the described HMM
    """
    n_components = 2
    model = hmm.GaussianHMM(n_components=n_components, covariance_type="full")
    model.startprob_ = np.asarray(startprob)
    # should be shape (2, 2), i.e., a transition matrix for 2 states
    model.transmat_ = np.array([[1. - switch_prob, switch_prob],
                                [switch_prob, 1. - switch_prob]])
    model.means_ = np.array([[1.0], [-1.0]])

    # should be shape (2, 1, 1), i.e., 2 1x1 covariance matrices
    model.covars_ = np.ones((2, 1, 1)) * noise_level
    model.sample(1)
    return model


np.random.seed(101)
nstep = 50
model = create_model()
observations, states = model.sample(nstep)
with plt.xkcd():
  plot_hmm1(model, states, observations)