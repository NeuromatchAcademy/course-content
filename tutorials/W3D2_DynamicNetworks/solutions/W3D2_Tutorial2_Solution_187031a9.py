
pars = default_pars()

x = np.arange(0,10,.1)
with plt.xkcd():
  fig1 = plt.figure(figsize=(8, 5.5))
  plt.plot(x,F(x,pars['a_E'],pars['theta_E']), 'b', label='E population')
  plt.plot(x,F(x,pars['a_I'],pars['theta_I']), 'r', label='I population')
  plt.legend(loc='lower right')
  plt.xlabel('x (a.u.)')
  plt.ylabel('F(x)')
  plt.show()