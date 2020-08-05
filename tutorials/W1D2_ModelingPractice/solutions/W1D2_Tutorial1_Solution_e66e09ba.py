
# source variable you want to check
source_var = v_w

below = np.mean(source_var[np.where(np.invert(z_s))[0]])
above = np.mean(source_var[np.where(z_s)[0]] )

with plt.xkcd():
  plt.bar(x=[0, 1], height=[below, above])

  plt.xticks([0, 1], ['below', 'above'])
  plt.show()
