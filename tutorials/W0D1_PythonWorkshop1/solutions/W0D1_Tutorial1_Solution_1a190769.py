t = 0

# loop for 10 steps, variable 'step' takes values from 0 to 9
for step in range(10):
  t = step * dt
  i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))
  print(i)