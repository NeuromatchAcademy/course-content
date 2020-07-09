
# set random number generator
np.random.seed(2020)

# initialize n, v_n and step_end
step_end = int(t_max / dt)
n = 50
v_n = [el] * n

# initialize the figure
plt.figure()
plt.title('SAMPLE OUTPUT')
plt.xlabel('time (s)')
plt.ylabel(r'$V_m$ (V)')

# loop for step_end steps
for step in range(step_end):
  t = step * dt

  v_mean = sum(v_n) / n 
  plt.plot(n*[t], v_n, 'k.', alpha=0.05)
  plt.plot(t, v_mean, 'C0.', alpha=0.8, markersize=10)

  for j in range(0, n):
    i = i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * (2 * np.random.random() - 1))
    v_n[j] = v_n[j] + (dt / tau) * (el - v_n[j] + r*i)
    
plt.show()