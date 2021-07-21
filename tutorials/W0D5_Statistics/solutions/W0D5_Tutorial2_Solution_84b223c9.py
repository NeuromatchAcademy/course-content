
# Initialize random initial distribution
p_random = np.ones((1,3))/3

# Fill in the missing line to get the state matrix after 100 transitions, like above
p_average_time_spent = p_random @ np.linalg.matrix_power(transition_matrix, 100)
print("The proportion of time spend by the rat in each of the three states is: "
            + str(p_average_time_spent[0]))