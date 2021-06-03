
from scipy.ndimage import gaussian_filter1d

# first let's smooth the tuning curves to make sure we get an accurate peak
# that isn't just noise
resp_smoothed = gaussian_filter1d(resp_all, 5, axis=0)

###################################################
## TO DO for students: find preferred orientation and resort W_in
###################################################

# find position of max response for each neuron
# aka preferred orientation for each neuron
preferred_orientation = resp_smoothed.argmax(axis=0)

# resort W_in matrix by preferred orientation
isort = preferred_orientation.argsort()
W_in_sorted = W_in[:,isort]

# plot resorted W_in matrix
with plt.xkcd():
  plt.figure(figsize=(10,4))
  plt.subplot(1,2,1)
  plt.imshow(W_in_sorted, aspect='auto', cmap='bwr', vmin=-1e-2, vmax=1e-2)
  plt.xlabel('sorted neurons')
  plt.ylabel('hidden units')
  plt.colorbar()
  plt.title('$W_{in}$')

  plt.subplot(1,2,2)
  plt.imshow(W_out.T, cmap='bwr', vmin=-3, vmax=3)
  plt.xticks([])
  plt.xlabel('output')
  plt.ylabel('hidden units')
  plt.colorbar()
  plt.title('$W_{out}$')

  plt.show()