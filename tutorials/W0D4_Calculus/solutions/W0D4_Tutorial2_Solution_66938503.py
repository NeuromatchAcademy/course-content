
"""
  1. Initial Values of $V_{reset} < -75$ result in the solution increasing to
  -75mV because $\frac{dV}{dt} > 0$.
  2. Initial Values of $V_{reset} > -75$ result in the solution decreasing to
  -75mV because $\frac{dV}{dt}  < 0$.
  3. Initial Values of $V_{reset} = -75$ result in a constant $V = -75$ mV
  because $\frac{dV}{dt}  = 0$ (Stable point).
"""