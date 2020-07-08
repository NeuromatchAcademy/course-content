
# initialize step_end and v
step_end = 10
v = el

# loop for step_end steps
for step in range(step_end):
  t = step * dt
  i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))
  print(f"{t:.3f} {v:.4e}") 
  v = v + dt/tau * (el - v + r*i)