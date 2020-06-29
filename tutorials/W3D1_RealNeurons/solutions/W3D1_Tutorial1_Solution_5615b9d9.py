pars = default_pars(T=100.) 
v, sp = run_LIF(pars, I = 300.)
with plt.xkcd():
  plot_volt_trace(pars, v, sp)
  plt.show()