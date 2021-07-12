"""
1) To make the system both oscillate and grow, real has to be positive,
and imaginary has to be not zero.

2) Stable oscillation of 0.5 Hz (half a cycle per unit time, or one cycle per two
unit time) is achieved with real = 0 and imagineary = +/- pi
(approximately 3.1 or -3.1).

Note: For really large values of the imaginary component, the numerical
integration scheme breaks down a bit, and we see non-stable oscillations
even when real=0. This is a numerical artifact of the forward Euler scheme.
Some of the students may discover this if they push the parameters, but I've
tried to constrain the widget so that it is not obvious, as it is not the point
of this exercise.

""";