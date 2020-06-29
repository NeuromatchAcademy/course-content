dt = 1/10
a = gamma.pdf( np.arange(0,10,dt), 2.5, 0 )
t = np.arange(0,10,dt)

# what should go into the np.cumsum() function?
v = np.cumsum(a*dt)

# this just plots your velocity:
with plt.xkcd():
  plt.figure(figsize=(10,6))
  plt.plot(t,a,label='acceleration [$m/s^2$]')
  plt.plot(t,v,label='velocity [$m/s$]')
  plt.xlabel('time [s]')
  plt.ylabel('[motion]')
  plt.legend(facecolor='xkcd:white')
  plt.show()