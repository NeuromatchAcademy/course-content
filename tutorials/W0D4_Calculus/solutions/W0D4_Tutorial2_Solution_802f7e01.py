# Parameter definition
E_L = -75
tau_m = 10

# Range of Values of V
V = np.arange(-90, 0, 1)
dVdt = -(V - E_L) / tau_m

with plt.xkcd():

  fig = plt.figure(figsize=(6, 4))
  plt.plot(V, dVdt)
  plt.hlines(0, min(V), max(V), colors='black', linestyles='dashed')
  plt.vlines(-75, min(dVdt), max(dVdt), colors='black', linestyles='dashed')

  plt.text(-50, 1, 'Positive')
  plt.text(-50, -2, 'Negative')
  plt.text(E_L, max(dVdt) + 1, r'$E_L$')
  plt.xlabel(r'$V(t)$ (mV)')
  plt.ylabel(r'$\frac{dV}{dt}=\frac{-(V-E_L)}{\tau_m}$')
  plt.ylim(-8, 2)
  plt.show()