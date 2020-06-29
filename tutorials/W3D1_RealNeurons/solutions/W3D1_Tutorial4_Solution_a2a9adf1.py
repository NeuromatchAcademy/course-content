def Delta_W(pars):
    """
    Plot STDP biphasic exponential decaying function
    
    Args:
      pars       : parameter dictionary
    
    Returns:
      dW         : instantaneous change in weights
    """
    
    # Get parameters
    A_plus, A_minus, tau_stdp = pars['A_plus'], pars['A_minus'], pars['tau_stdp']
    
    #pre_spike time - post_spike time
    time_diff = np.linspace(-5*tau_stdp, 5*tau_stdp, 50)
    
    #STDP change
    dW = np.zeros(len(time_diff))
    dW[time_diff<=0] = A_plus * np.exp(time_diff[time_diff<=0]/tau_stdp)  #LTP
    dW[time_diff>0] = -A_minus * np.exp(-time_diff[time_diff>0]/tau_stdp) #LTD

    with plt.xkcd():

      plt.figure()
      plt.plot([-5*tau_stdp,5*tau_stdp],[0,0],'k',linestyle=':')
      plt.plot([0,0],[-A_minus,A_plus],'k',linestyle=':')

      plt.plot(time_diff[time_diff<=0], dW[time_diff<=0], 'ro')
      plt.plot(time_diff[time_diff>0], dW[time_diff>0], 'bo')

      plt.xlabel(r't$_{\mathrm{pre}}$ - t$_{\mathrm{post}}$ (ms)')
      plt.title('Biphasic STDP', fontweight='bold')
      plt.show()
    
pars = default_pars_STDP()
Delta_W(pars)