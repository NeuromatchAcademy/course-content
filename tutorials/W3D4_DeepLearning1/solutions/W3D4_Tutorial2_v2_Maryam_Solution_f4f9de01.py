
### convolutional parameters
K = 49 # size of convolutional filter
stride = 1 # how often to compute the convolution along the stim axis
pad = K // 2 # we will need to pad stimulus with zeros to perform convolution

### stimulus is 0 in all places except stimulus orientation
ori = 135#np.random.choice(360)
stimulus = np.zeros(360+2*pad) # pad stimulus by -pad / +pad
stimulus[ori+pad] = 1.0

### f is a gaussian
# we will use the code from W2D1 (bayes day) to create this!
# mean of gaussian mu=0
i = np.arange(-pad, pad)
f = my_gaussian(i, 0.0, sigma=10)

### compute the convolution
a = np.nan * np.zeros(360) # initialize convolutional output
for x in np.arange(0+pad, 360+pad, stride, int): # loop over positions x
  # compute element-wise multiplication between filter and stimulus
  a[x-pad] = (f * stimulus[x-pad : x+pad]).sum()

with plt.xkcd():
  fig = plt.figure(figsize=(15,3))
  plot_conv(pad, stimulus, f, a)
  plt.show()