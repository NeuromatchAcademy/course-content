
"""
Here excitation and inhibition are interacting additively. That is, if you change $\theta$ and $a$ for excitation,
it will not affect the derivative wrt to inhibition and vice versa.

The effect of varying $\theta$ and $a$ on the derivative wrt to excitation and inhibition is identical to what you for 1-D transfer function
$\theta$ shifts the neuron transfer function along the x-axis -- reducing $theta$ moves the transfer function leftwards.
So by changing $\theta$ for excitation you will shift the derivative surface left/right along the excitation axis. Same for inhibition.

$a$ controls the steepness of the neuron transfer function -- increasing $a$ makes the curve more steeper.
So by changing $a$ for excitation you will vary the width of the notch of the derivative surface.
For inhibition, by varying $a$ you will vary the width of the ridge in the drivative surface.
"""