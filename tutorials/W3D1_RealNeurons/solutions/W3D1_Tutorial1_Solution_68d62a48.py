pars = default_pars(T=1000.)
mu_gwn  = 250.

sig_gwn1 = 0.5
I_GWN = my_GWN(pars, mu = mu_gwn, sig=sig_gwn1, myseed=2020)
v, sp1 = run_LIF(pars, I=I_GWN)
isi1 = np.diff(sp1)
cv1 = isi1.std()/isi1.mean()

sig_gwn2 = 3.0
I_GWN = my_GWN(pars, mu = mu_gwn, sig=sig_gwn2, myseed=2020)
v, sp2 = run_LIF(pars, I=I_GWN)
isi2 = np.diff(sp2)
cv2 = isi2.std()/isi2.mean()

with plt.xkcd():
  my_hists(isi1, isi2, cv1, cv2)