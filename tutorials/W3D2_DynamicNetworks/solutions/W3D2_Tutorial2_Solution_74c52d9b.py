
def get_dGdE(pars, fp):  
  """
  Simulate the Wilson-Cowan equations 
  
  Expects:
    pars : Parameter dictionary
    fp   : fixed point (E, I), array
  
  Returns:
    J    : the 2x2 Jacobian matrix
  """
  
  #get the parameters
  tau_E, a_E, theta_E = pars['tau_E'], pars['a_E'], pars['theta_E']
  wEE, wEI = pars['wEE'], pars['wEI'] 
  I_ext_E = pars['I_ext_E']

  #initialization
  E = fp[0]
  I = fp[1]
  
  # calculate the J[0, 0]
  dGdE = (-1 + wEE*dF(wEE*E-wEI*I+I_ext_E,a_E,theta_E))/tau_E #dGE_dE

  
  return dGdE


pars = default_pars()
x_fp_1 = my_fp(pars, 0.1, 0.1)
dGdE1 = get_dGdE(pars, x_fp_1)
x_fp_2 = my_fp(pars, 0.3, 0.3)
dGdE2 = get_dGdE(pars, x_fp_2)
x_fp_3 = my_fp(pars, 0.8, 0.6)
dGdE3 = get_dGdE(pars, x_fp_3)

print ('For the default case:')
print ('dG/dE(fp1) = %.3f' %(dGdE1))
print ('dG/dE(fp2) = %.3f' %(dGdE2))
print ('dG/dE(fp3) = %.3f' %(dGdE3))

print ('\n')

pars = default_pars()
pars['wEE'], pars['wEI'] = 6.4, 4.8
pars['wIE'], pars['wII'] = 6.0, 1.2
pars['I_ext_E'] = 0.8
x_fp_lc = my_fp(pars, 0.8, 0.8)
dGdE_lc = get_dGdE(pars, x_fp_lc)
print ('For the limit cycle case:')
print ('dG/dE(fp_lc) = %.3f' %(dGdE_lc))