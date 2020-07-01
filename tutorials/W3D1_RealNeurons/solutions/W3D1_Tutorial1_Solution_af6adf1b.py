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
    plt.figure(figsize=(11, 4))
    my_bins = np.linspace(10, 30, 20)
    plt.subplot(1, 2, 1)
    plt.hist(isi1, bins=my_bins, color='b', alpha=0.5);
    plt.xlabel('ISI (ms)')
    plt.ylabel('number')
    plt.title(r'$\sigma=$%.1f, CV$_{\mathrm{isi}}$=%.3f' % (sig_gwn1, cv1))

    plt.subplot(1, 2, 2)
    plt.hist(isi2, bins=my_bins, color='b', alpha=0.5);
    plt.xlabel('ISI (ms)')
    plt.ylabel('number')
    plt.title(r'$\sigma=$%.1f, CV$_{\mathrm{isi}}$=%.3f' % (sig_gwn2, cv2))
    plt.tight_layout()
    plt.show()