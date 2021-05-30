
# Create P (using np array)
P = np.array([[1, 3], [2, 1]])

# Create v_p (using np array)
v_p = np.array([16, 7])

# Solve for g (using np.linalg.inv)
g = np.linalg.inv(P) @ v_p

# Print g
print(g)