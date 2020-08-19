"""
While both sources of noise have an effect on the controlled state, the
process noise has a much larger effect. As the process noise w[t] increases,
state cost (MSE between state and goal) and  control cost increase drastically.
You can get an intuition as to why using the sliders in the demo above.  To make
matters worse, as the process noise gets larger, you will also need to put in
more effort to keep the system close to the goal.

The measurement noise v[t]  also has an effect on the accuracy of the
controlled state. As this noise increases, the MSE between the state and goal
increases. The cost of control in this case remains fairly constant with
increasing levels of measurement noise.
""";