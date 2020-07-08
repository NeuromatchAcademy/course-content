
# set random number generator
np.random.seed(2020)

# initialize step_end, n and v_n
step_end = int(t_max / dt)
n = 50
v_n = [el] * n

# initialize the figure
plt.figure()
plt.title('Multiple realizations of $V_m$')
plt.xlabel('time (s)')
plt.ylabel(r'$V_m$ (V)')

# loop for step_end steps
for step in range(step_end):
  t = step * dt
  plt.plot([t] * n, v_n, 'k.', alpha=0.05)

  # loop for n steps
  for j in range(0, n):
    i = i_mean * (1 + 0.1 * (t_max/dt)**(0.5) * (2* np.random.random() - 1))
    v_n[j] = v_n[j] + (dt / tau) * (el - v_n[j] + r*i)

plt.show()