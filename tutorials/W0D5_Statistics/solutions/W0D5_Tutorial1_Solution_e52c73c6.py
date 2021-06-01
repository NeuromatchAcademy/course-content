
# Fill out transition matrix with matching table values
# in the form np.array([ [...], [...], [...] ])
transition_matrix = np.array([[ 0.2, 0.6, 0.2],[ .6, 0.3, 0.1], [0.8, 0.2, 0]])

# Initial state, x0
x0 = np.array([0, 1, 0])

# Then multiply initial state by the matrix 4 times, or equivalently raise the
# matrix to the 4th power before multiplying it to the initial state
x4 = x0 @ np.linalg.matrix_power(transition_matrix, 4)

# The second area is indexed as 1 (Python starts indexing at 0)
print("The probability the rat will be in area 2 after 4 transitions is: " + str(x4[1]))