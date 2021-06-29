
"""
The first step is to calculute:
𝑃(𝑣+|ℎ0)=𝑃(ℎ0|𝑣+)𝑃(𝑣+)/𝑃(ℎ0)=(1−0.1)∗0.3/(1−0.4)=0.45

Then use the property of marginalisation (discrete version)

𝑃(𝑎)=∑𝑖𝑃(𝑎|𝑏=𝑖)𝑃(𝑏=𝑖)

𝑃(𝑣+)=𝑃(𝑣+|ℎ+)𝑃(ℎ+)+𝑃(𝑣+|ℎ0)𝑃(ℎ0)=0.075∗0.4+0.45∗(1−0.4)=0.3

Phew, we recovered the correct value!
"""