def get_eig_Jacobian(pars, fp):
  """
  Simulate the Wilson-Cowan equations 
  
  Args:
    pars : Parameter dictionary
    fp   : fixed point (E, I), array
  
  Returns:
    evals : 2x1 vector of eigenvalues of the Jacobian matrix
  """
  
  #get the parameters
  tau_E, a_E, theta_E = pars['tau_E'], pars['a_E'], pars['theta_E']
  tau_I, a_I, theta_I = pars['tau_I'], pars['a_I'], pars['theta_I']
  wEE, wEI = pars['wEE'], pars['wEI'] 
  wIE, wII = pars['wIE'], pars['wII']
  I_ext_E, I_ext_I = pars['I_ext_E'], pars['I_ext_I']

  #initialization
  E = fp[0]
  I = fp[1]
  J = np.zeros((2,2))
  
  #Jacobian matrix
  J[0,0] = (-1 + wEE*dF(wEE*E-wEI*I+I_ext_E,a_E,theta_E))/tau_E #dGE_dE
  J[0,1] = (-wEI*dF(wEE*E-wEI*I+I_ext_E,a_E,theta_E))/tau_E     #dGE_dI
  J[1,0] = (wIE*dF(wIE*E-wII*I+I_ext_I,a_I,theta_I))/tau_I      #dGI_dE
  J[1,1] = (-1 - wII*dF(wIE*E-wII*I,a_I+I_ext_I,theta_I))/tau_I #dGI_dI        
  
  # Eigenvalues
  evals = np.linalg.eig(J)[0]
  
  return evals

eig_1 = get_eig_Jacobian(pars, x_fp_1)
eig_2 = get_eig_Jacobian(pars, x_fp_2)
eig_3 = get_eig_Jacobian(pars, x_fp_3)
print(eig_1, 'Stable point')
print(eig_2, 'Unstable point')
print(eig_3, 'Stable point')