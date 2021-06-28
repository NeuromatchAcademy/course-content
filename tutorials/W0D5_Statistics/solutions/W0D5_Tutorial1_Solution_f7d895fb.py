
# Initialize random initial distribution
x_random = np.ones((1,3))/3

# Fill in the missing line to get the state matrix after 100 transitions, like above
x_average_time_spent = x_random @ np.linalg.matrix_power(transition_matrix, 100)
print("The proportion of time spend by the rat in each of the three states is: "
            + str(x_average_time_spent[0]))