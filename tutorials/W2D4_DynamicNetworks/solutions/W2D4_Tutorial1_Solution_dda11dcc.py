def eig_single(fp, tau, a, theta, w, I_ext, **other_pars):
  """
  Args:
    fp   : fixed point r_fp
    tau, a, theta, w, I_ext : Simulation parameters

  Returns:
    eig : eigevalue of the linearized system
  """
  # Compute the eigenvalue
  eig = (-1. + w * dF(w * fp + I_ext, a, theta)) / tau

  return eig


# Find the eigenvalues for all fixed points
pars = default_pars_single(w=5, I_ext=.5)
r_guess_vector = [0, .4, .9]
x_fp = my_fp_finder(pars, r_guess_vector)

for fp in x_fp:
  eig_fp = eig_single(fp, **pars)
  print(f'Fixed point1 at {fp:.3f} with Eigenvalue={eig_fp:.3f}')