
"""

1) Higher noise, or higher sigma, means that the evidence accumulation varies up
   and down more widely. You are more likely to make a wrong decision with high noise
   as the cumulated log likelihood ratio is more likely to be negative at the end
   despite the true distribution being s = 1.

2) When sigma is very small, the cumulated log likelihood ratios are basically a linear
   diagonal line. This is because each new measurement will be very similar (since they are
   being drawn from a Gaussian with a tiny standard deviation)

3) You are more likely to be wrong with a small number of time steps before decision. There is
   more change that the noise will affect the decision. We will explore this in the next section.

"""