def generic_function(x):
  """Google style doc string. Brief summary of what function does here
  
  Args:
    x (ndarray): An array of shape (N,) that contains blah blah

  Returns:
    ndarray: The output is blah blah
  """

  # Have a comment for every line of code they need to write, and when possible have
  # variables written with ellipses where they should fill in or ellipses where they should
  # fill in inputs to functions
  y = multiply_array(x, 5)

  # Another comment because they need to add another line of code
  z = y + 6

  return z

# Uncomment below to test your function 
x = np.array([4, 5, 6])
z = generic_function(x)

# xkcd style for solution plot
with plt.xkcd():  
  plotting_z(z)
# we often invoke a plotting function hidden in Helper Functions so students don't 
# have to uncomment a lot of boilerplate matplotlib code