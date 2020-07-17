def get_dGdE(pars, fp):
  """
  Simulate the Wilson-Cowan equations

  Args:
    pars : Parameter dictionary
    fp   : fixed point (E, I), array

  Returns:
    J    : the 2x2 Jacobian matrix
  """

  # get the parameters
  tau_E, a_E, theta_E = pars['tau_E'], pars['a_E'], pars['theta_E']
  wEE, wEI = pars['wEE'], pars['wEI']
  I_ext_E = pars['I_ext_E']

  # initialization
  rE = fp[0]
  rI = fp[1]

  # Calculate the J[0,0]
  dGdrE = (-1 + wEE * dF(wEE * rE - wEI * rI + I_ext_E, a_E, theta_E)) / tau_E

  return dGdrE


pars = default_pars()
x_fp_1 = my_fp(pars, 0.1, 0.1)
x_fp_2 = my_fp(pars, 0.3, 0.3)
x_fp_3 = my_fp(pars, 0.8, 0.6)

dGdrE1 = get_dGdE(pars, x_fp_1)
dGdrE2 = get_dGdE(pars, x_fp_2)
dGdrE3 = get_dGdE(pars, x_fp_3)

print(f'For the default case:')
print(f'dG/drE(fp1) = {dGdrE1:.3f}')
print(f'dG/drE(fp2) = {dGdrE2:.3f}')
print(f'dG/drE(fp3) = {dGdrE3:.3f}')

print('\n')

pars = default_pars()
pars['wEE'], pars['wEI'] = 6.4, 4.8
pars['wIE'], pars['wII'] = 6.0, 1.2
pars['I_ext_E'] = 0.8
x_fp_lc = my_fp(pars, 0.8, 0.8)

dGdrE_lc = get_dGdE(pars, x_fp_lc)

print('For the limit cycle case:')
print(f'dG/drE(fp_lc) = {dGdrE_lc:.3f}')