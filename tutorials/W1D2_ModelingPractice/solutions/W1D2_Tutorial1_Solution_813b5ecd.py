
# this sets up a figure with some dotted lines on y=0 and x=0 for reference
with plt.xkcd():

  plt.figure(figsize=(8, 8))
  plt.plot([0, 0], [-0.5, 1.5], ':', color='xkcd:black')
  plt.plot([-0.5, 1.5], [0, 0], ':', color='xkcd:black')

  # determine which variables you want to look at
  plt.scatter(v_w,     # variable on the abscissa / x-axis
              v_s)     # variable on the ordinate / y-axis
  plt.xlabel('world-motion velocity [m/s]')
  plt.ylabel('self-motion velocity [m/s]')
  plt.show()