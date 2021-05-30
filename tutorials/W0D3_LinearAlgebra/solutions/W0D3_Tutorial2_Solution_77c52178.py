
# Define G
G = np.array([[0, 1], [2, 4], [5, 1]])

# Define W
W = np.array([[3, 2, 1], [1, 2, 7]])

# Compute V
# in Python, we can use @ for matrix multiplication: matrix1 @ matrix2
V = W @ G

# Print values of V
print(V)