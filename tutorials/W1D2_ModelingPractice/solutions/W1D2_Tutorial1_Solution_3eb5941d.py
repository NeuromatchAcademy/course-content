

source_var = v_w

below = np.mean(source_var[np.where(np.invert(z_s))[0]])
above = np.mean(source_var[np.where(z_s)[0]])

# we plot solutions in xkcd format to set them apart from exercises
with plt.xkcd():
  plt.figure()
  plt.bar(x=[0, 1], height=[below, above])
  plt.xticks([0, 1], ['below', 'above'])
  plt.show()