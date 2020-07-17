def eig_single(pars, fp):
  """
  Args:
    pars : Parameter dictionary
    fp   : fixed point r_fp

  Returns:
    eig : eigevalue of the linearized system
  """

  # get the parameters
  tau, a, theta = pars['tau'], pars['a'], pars['theta']
  w, I_ext = pars['w'], pars['I_ext']
  print(tau, a, theta, w, I_ext)

  # Compute the eigenvalue
  eig = (-1. + w * dF(w * fp + I_ext, a, theta)) / tau

  return eig


pars = default_pars_single()
pars['w'] = 5.0
pars['I_ext'] = 0.5

# Find the eigenvalues for all fixed points of Exercise 2

x_fp_1 = my_fp_single(pars, 0.).item()
eig_fp_1 = eig_single(pars, x_fp_1).item()
print(f'Fixed point1 at {x_fp_1:.3f} with Eigenvalue={eig_fp_1:.3f}')

x_fp_2 = my_fp_single(pars, 0.4).item()
eig_fp_2 = eig_single(pars, x_fp_2).item()
print(f'Fixed point2 at {x_fp_2:.3f} with Eigenvalue={eig_fp_2:.3f}')

x_fp_3 = my_fp_single(pars, 0.9).item()
eig_fp_3 = eig_single(pars, x_fp_3).item()
print(f'Fixed point3 at {x_fp_3:.3f} with Eigenvalue={eig_fp_3:.3f}')