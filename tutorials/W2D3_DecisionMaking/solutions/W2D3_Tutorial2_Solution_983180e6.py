############
## Solution
###########
def my_create_model(switch_prob=0.1,noise_level=0.5):
    """
    Create an HMM with binary state variable and 1D Gaussian observations
    The probability to switch to the other state is `switch_prob`. Two observation models have 
    mean 1.0 and -1.0 respectively. `noise_level` specifies the standard deviation of the observation
    models.

    Args:
        switch_prob (float): probability to jump to the other state
        noise_level (float): standard deviation of observation models. Same for two components
    Returns:
        model (hmm.GaussianHMM instance): the described HMM
    """
    n_components = 2
    model = hmm.GaussianHMM(n_components=n_components, covariance_type="full")
    model.startprob_ = np.array([1.0, 0.0])
    model.transmat_ = np.array([[1.0-switch_prob, switch_prob],
                                [switch_prob, 1.0-switch_prob]])
    model.means_ = np.array([[1.0],[-1.0]])
    model.covars_ = np.tile(np.eye(1) *np.power(noise_level,2)  , (2, 1, 1))
    model.sample(1)
    return model

nstep = 100
model = my_create_model()
observations, states = model.sample(nstep)
observations = observations.reshape(-1)

table = pd.DataFrame({"states": states,"observations":observations})
print(table)

with plt.xkcd():
  plot_hmm1(model, states, observations)
