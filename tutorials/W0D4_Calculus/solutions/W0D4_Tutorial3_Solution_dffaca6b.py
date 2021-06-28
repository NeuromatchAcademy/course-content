
# Time step
dt = 1

# Make time range from 1 to 5 years with step size dt
t = np.arange(1, 5+dt/2, dt)

# Get number of steps
n = len(t)

# Initialize p array
p = np.zeros(n)
p[0] = np.exp(0.3*t[0]) # initial condition

# Loop over steps
for k in range(n-1):

  # Calculate the population step
    p[k+1] = p[k] + dt * 0.3 * p[k]

# Visualize
with plt.xkcd():
  visualize_population_approx(t, p)