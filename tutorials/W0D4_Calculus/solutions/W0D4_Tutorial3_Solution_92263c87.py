dt = 1
t = np.arange(1, 5+dt/2, dt) # Time from 0 to 10 years in 0.1 steps
n = len(t)
p = np.ones(n)
p[0] = np.exp(0.3*t[0]) # Initial Condition

with plt.xkcd():

  fig = plt.figure(figsize=(6, 4))
  plt.plot(t, np.exp(0.3*t), 'k', label='Exact Solution')

  for i in range(n-1):
    dp = dt * 0.3 * p[i]
    p[i+1] = p[i] + dp

  plt.plot(t, p,':o', label='Euler Estimate')
  plt.vlines(t, p, np.exp(0.3*t),
             colors='r', linestyles='dashed', label=r'Error $e_i$')

  plt.plot(t[0], p[0], 'go', label='Intial Condition')
  plt.ylabel('Population (millions)')
  plt.legend()
  plt.xlabel('Time (years)')
  plt.show()