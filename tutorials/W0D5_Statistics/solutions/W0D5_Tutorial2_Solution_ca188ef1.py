
# Transition matrix
transition_matrix = np.array([[ 0.2, 0.6, 0.2],[ .6, 0.3, 0.1], [0.8, 0.2, 0]])

# Initial state, p0
p0 = np.array([0, 1, 0])

# Compute the probabilities 4 transitions later (use np.linalg.matrix_power to raise a matrix a power)
p4 = p0 @ np.linalg.matrix_power(transition_matrix, 4)

# The second area is indexed as 1 (Python starts indexing at 0)
print("The probability the rat will be in area 2 after 4 transitions is: " + str(p4[1]))