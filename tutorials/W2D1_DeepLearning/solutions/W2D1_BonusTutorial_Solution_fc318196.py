
from scipy.ndimage import gaussian_filter1d

# first let's smooth the tuning curves resp_all to make sure we get
# an accurate peak that isn't just noise
# resp_all is size (n_stimuli, n_neurons)
resp_smoothed = gaussian_filter1d(resp_all, 5, axis=0)
# resp_smoothed is size (n_stimuli, n_neurons)

# find position of max response for each neuron
# aka preferred orientation for each neuron
preferred_orientation = resp_smoothed.argmax(axis=0)

## Resort W_in matrix by preferred orientation
isort = preferred_orientation.argsort()
W_in_sorted = W_in[:,isort]

# plot resorted W_in matrix
with plt.xkcd():
  visualize_weights(W_in_sorted, W_out)