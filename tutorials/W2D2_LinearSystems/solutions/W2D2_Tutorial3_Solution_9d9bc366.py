lam = 0.9    # decay rate
sig = 0.1   # standard deviation of diffusive process
T = 500      # total Time duration in steps
x0 = 4.      # initial condition of x at time 0
xinfty = 1.  # x drifts towards this value in long time

# initiatialize variables
t = np.arange(0, T, 1.)
x = np.zeros_like(t)
x[0] = x0

# Step through in time
for k in range(len(t)-1):

    # Solution
    x[k+1] = xinfty + lam * (x[k] - xinfty) + sig * np.random.standard_normal(size=1) # remove later

with plt.xkcd():
  plot_ddm(t, x, xinfty, lam, x0)