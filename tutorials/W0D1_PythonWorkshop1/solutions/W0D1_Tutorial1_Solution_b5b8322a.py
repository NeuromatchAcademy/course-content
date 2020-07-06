
# set random number generator
np.random.seed(2020)

# initialize step_end, n and v_n
step_end = int(t_max/dt)
n = 50
v_n = [el] * n

# initialize the figure
plt.figure()
plt.title('Multiple realizations of $V_m$')
plt.xlabel('time (s)')
plt.ylabel(r'$V_m$ (V)')

# loop for step_end steps
for step in range(step_end):
  t = step*dt

  v_mean = sum(v_n) / n
  v_var_n = [(v - v_mean)**2 for v in v_n]
  v_var = sum(v_var_n) / (n-1)
  v_std = np.sqrt(v_var)

  plt.plot(n*[t], v_n, 'k.', alpha=0.05)
  plt.plot(t, v_mean, 'C1.', alpha=0.8)
  plt.plot(t, v_mean + v_std, 'C7.', alpha=0.8)
  plt.plot(t, v_mean - v_std, 'C7.', alpha=0.8)

  for j in range(0, n):
    i = i_mean * (1 + 0.1*(t_max/dt)**(0.5)*(2*np.random.random()-1))
    v_n[j] = v_n[j] + dt/tau * (el - v_n[j] + r*i)

plt.show()