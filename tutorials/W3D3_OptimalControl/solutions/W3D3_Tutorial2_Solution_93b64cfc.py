"""
* rho=0 will get you the same cost and control gain as in Exercise 1 by
  zeroing out the cost term.
* A small value for rho will have a similar solution as in (a), but with
   potentially large values for |a[t]|.
* A large value for rho, like 2 will lead to small values for |a[t]|.
* The control gain becomes more time-varying (as opposed to fairly static)
  for large rho. For some parameter values, L[t] oscillates during the entire
  trajectory in order to keep $|a_t|$ low. Try D = 0.9, B = 2 and rho = 2.
""";