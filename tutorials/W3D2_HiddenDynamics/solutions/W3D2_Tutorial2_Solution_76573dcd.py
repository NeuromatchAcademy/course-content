
def create_HMM(switch_prob=0.1, noise_level=1e-1, startprob=[1.0, 0.0]):
  """Create an HMM with binary state variable and 1D Gaussian measurements
  The probability to switch to the other state is `switch_prob`. Two
  measurement models have mean 1.0 and -1.0 respectively. `noise_level`
  specifies the standard deviation of the measurement models.

  Args:
      switch_prob (float): probability to jump to the other state
      noise_level (float): standard deviation of measurement models. Same for
      two components

  Returns:
      model (GaussianHMM instance): the described HMM
  """

  n_components = 2

  startprob_vec = np.asarray(startprob)

  # STEP 1: Transition probabilities
  transmat_mat = np.array([[1. - switch_prob, switch_prob], [switch_prob, 1. - switch_prob]]) # # np.array([[...], [...]])

  # STEP 2: Measurement probabilities

  # Mean measurements for each state
  means_vec = np.array([-1.0, 1.0])

  # Noise for each state
  vars_vec = np.ones(2) * noise_level * noise_level

  # Initialize model
  model = GaussianHMM1D(
    startprob = startprob_vec,
    transmat = transmat_mat,
    means = means_vec,
    vars = vars_vec,
    n_components = n_components
  )

  return model


def sample(model, T):
  """Generate samples from the given HMM

  Args:
    model (GaussianHMM1D): the HMM with Gaussian measurement
    T (int): number of time steps to sample

  Returns:
    M (numpy vector): the series of measurements
    S (numpy vector): the series of latent states

  """
  # Initialize S and M
  S = np.zeros((T,),dtype=int)
  M = np.zeros((T,))

  # Calculate initial state
  S[0] = np.random.choice([0,1],p=model.startprob)

  # Latent state at time `t` depends on `t-1` and the corresponding transition probabilities to other states
  for t in range(1,T):

    # STEP 3: Get vector of probabilities for all possible `S[t]` given a particular `S[t-1]`
    transition_vector = model.transmat[S[t-1],:]

    # Calculate latent state at time `t`
    S[t] = np.random.choice([0,1],p=transition_vector)

  # Calculate measurements conditioned on the latent states
  # Since measurements are independent of each other given the latent states, we could calculate them as a batch
  means = model.means[S]
  scales = np.sqrt(model.vars[S])
  M = np.random.normal(loc=means, scale=scales, size=(T,))

  return M, S

# Set random seed
np.random.seed(101)

# Set parameters of HMM
T = 100
switch_prob = 0.1
noise_level = 2.0

# Create HMM
model = create_HMM(switch_prob=switch_prob, noise_level=noise_level)

# Sample from HMM
M, S = sample(model,T)
assert M.shape==(T,)
assert S.shape==(T,)

# Print values
print(M[:5])
print(S[:5])