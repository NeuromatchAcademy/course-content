
# parameters
T = 500     # total Time duration
dt = 0.1   # timestep of our simulation
t = np.arange(0, T, dt)

# same parameters as above
# c2o: closed to open rate
# o2c: open to closed rate
c2o = 0.02
o2c = 0.1
A = np.array([[1 - c2o*dt, o2c*dt],
              [c2o*dt,     1 - o2c*dt]])

# initial condition: start as Closed
x0 = np.array([[1, 0]]) 
# x will be our array to keep track of x through time
x = x0

for k in range(len(t)-1):
    x_kp1 = np.dot(A, x[-1,:]) # remove later
    # stack this new state onto x to keep track of x through time steps
    x = np.vstack((x, x_kp1))

print(x.shape, t.shape)
with plt.xkcd():
  plot_state_probabilities(t,x)