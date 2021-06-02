dt = 1    # time-step
t_0 = 1   # initial time
p_0 = np.exp(0.3*t_0)    # initial population

dp = dt * 0.3 * p_0
p_1 = p_0 + dp
print(p_1)