
"""
In Exercise 3, you should have noticed that:
* The system follows time varying goals rather well, with little change to the
   cost function and the control equations.

* Setting rho=0 leads to noise in the first part of the time series.
  Here, we see that the control cost in fact acts as a regularizer.

* Larger values of the process noise variance lead to a higher MSE between the
  state and the desired goal.
""";