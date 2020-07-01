pars = default_parsE()
pars['wEE'] = 5.0
pars['I_ext_E'] = 0.5

def eig_E(pars, fp):
  """
  Args:
    pars : Parameter dictionary
    fp   : fixed point E
  
  Returns:
    eig : eigevalue of the linearized system
  """
  
  #get the parameters
  tau_E, a_E, theta_E = pars['tau_E'], pars['a_E'], pars['theta_E']
  wEE, I_ext_E = pars['wEE'],  pars['I_ext_E']
  # fixed point
  E = fp

  eig = (-1. + wEE*dF(wEE*E + I_ext_E, a_E, theta_E)) / tau_E 

  return eig

# Uncomment below lines after completing the eigE function
x_fp_1 = my_fpE(pars, 0.)
eig_E1 = eig_E(pars, x_fp_1)
print('Fixed point1=%.3f, Eigenvalue=%.3f' % (x_fp_1, eig_E1))

# Continue by finding the eigenvalues for all fixed points of Exercise 2
x_fp_2 = my_fpE(pars, 0.4)
eig_E2 = eig_E(pars, x_fp_2)
print('Fixed point2=%.3f, Eigenvalue=%.3f' % (x_fp_2, eig_E2))

x_fp_3 = my_fpE(pars, 0.9)
eig_E3 = eig_E(pars, x_fp_3)
print('Fixed point3=%.3f, Eigenvalue=%.3f' % (x_fp_3, eig_E3))