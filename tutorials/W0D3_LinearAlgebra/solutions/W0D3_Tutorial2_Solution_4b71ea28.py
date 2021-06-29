
# Define R
R = np.array([[0, 1], [2, 4], [5, 1]])

# Define W
W = np.array([[3, 2, 1], [1, 2, 7]])

# Compute G
# in Python, we can use @ for matrix multiplication: matrix1 @ matrix2
G = W @ R

# Print values of G
print(G)