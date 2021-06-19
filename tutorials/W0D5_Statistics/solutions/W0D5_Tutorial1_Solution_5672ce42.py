
# Initialize random initial distribution
x_random = np.ones((1,3))/3

# Transition matrix
transition_matrix = np.array([[ 0.2, 0.6, 0.2],[ .6, 0.3, 0.1], [0.8, 0.2, 0]])

# Fill in the missing line to get the state matrix after 100 transitions, like above
x_average_time_spent = x_random @ np.linalg.matrix_power(transition_matrix, 100)
print("The proportion of time spend by the rat in each of the three states is: "
            + str(x_average_time_spent[0]))