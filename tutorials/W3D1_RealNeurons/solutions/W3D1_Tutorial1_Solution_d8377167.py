pars = default_pars(T=100.)
sig_gwn = 5.
mu_gwn  = 250.
I_GWN = my_GWN(pars, mu = mu_gwn, sig=sig_gwn, myseed=2020)
v, sp = run_LIF(pars, I=I_GWN)

with plt.xkcd():
    plt.figure(figsize=(12, 4))
    plt.subplot(1,2,1)
    plt.plot(pars['range_t'][::3], I_GWN[::3], 'b')
    plt.xlabel('Time (ms)')
    plt.ylabel(r'$I_{GWN}$ (pA)')
    plt.subplot(1,2,2)
    plot_volt_trace(pars, v, sp)
    plt.tight_layout()
    plt.show()