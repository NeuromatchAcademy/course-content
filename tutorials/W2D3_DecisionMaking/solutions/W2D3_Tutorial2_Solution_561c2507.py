
def create_model():
    """
    Create an HMM with binary state variable and 1D Gaussian observations
    The probability to switch to the other state is 1. Two observation models have 
    mean 1.0 and -1.0 respectively and almost zero standard deviation

    Returns:
        model (hmm.GaussianHMM instance): the described HMM
    """
    n_components = 2
    model = hmm.GaussianHMM(n_components=n_components, covariance_type="full")
    model.startprob_ = np.array([1.0, 0.0])
    model.transmat_ = np.array([[0.0, 1.0],[1.0, 0.0]])
    model.means_ = np.array([[1.0],[-1.0]])
    model.covars_ = np.tile(np.eye(1) * 1e-8 , (2, 1, 1))
    model.sample(1)
    return model


nstep = 15
model = create_model()
observations, states = model.sample(nstep)
observations = observations.flatten()

table = pd.DataFrame({"states": states,"observations":observations})
print(table)

with plt.xkcd():
    plot_hmm1(model, states, observations)
