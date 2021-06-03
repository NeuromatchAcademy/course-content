t = np.arange(0, 10, 0.1) # Time from 0 to 10 years in 0.1 steps

with plt.xkcd():

  p = np.exp(0.3 * t)

  fig = plt.figure(figsize=(6, 4))
  plt.plot(t, p)
  plt.ylabel('Population (millions)')
  plt.xlabel('time (years)')
  plt.show()