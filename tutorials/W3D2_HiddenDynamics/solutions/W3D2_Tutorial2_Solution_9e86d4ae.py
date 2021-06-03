def create_HMM(switch_prob=0.1, noise_level=1e-8, startprob=[1.0, 0.0]):
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

    # Initialize model
    model = hmm.GaussianHMM(n_components=n_components, covariance_type="full")
    model.startprob_ = np.asarray(startprob)

    # Make transition matrix, should be shape (2, 2), i.e., a transition matrix for 2 states
    model.transmat_ = np.array([[1. - switch_prob, switch_prob],
                                [switch_prob, 1. - switch_prob]])
    # Create means
    model.means_ = np.array([[1.0], [-1.0]])

    # Create covariance matrices, should be shape (2, 1, 1), i.e., 2 1x1 covariance matrices
    model.covars_ = np.ones((2, 1, 1)) * noise_level

    model.sample(1)

    return model


# Set random seed
np.random.seed(101)

# Number of steps
nstep = 50

# Create HMM
model = create_HMM()

# Sample from HMM
observations, states = model.sample(nstep)

# Visualize
with plt.xkcd():
  plot_hmm1(model, states, observations)