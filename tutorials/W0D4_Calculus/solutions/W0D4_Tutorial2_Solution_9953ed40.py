p = np.arange(0, 100, 0.1)

with plt.xkcd():

  dpdt = 0.3*p
  fig = plt.figure(figsize=(6, 4))
  plt.plot(p, dpdt)
  plt.xlabel(r'Population $p(t)$ (millions)')
  plt.ylabel(r'$\frac{d}{dt}p(t)=\alpha p(t)$')
  plt.show()