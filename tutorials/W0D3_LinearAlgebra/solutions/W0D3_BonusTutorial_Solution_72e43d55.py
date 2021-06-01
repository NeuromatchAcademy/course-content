
# 1) With the eigenvalue = 2, the activities of the neurons explode towards infinity, along
#.   the eigenvector.

# 2) At eigenvalue = 1, there is a shift in what happens. With the eigenvalue above 1,
#.  the activites always explode. Once the eigenvalue is below 1, the activities decay to 0.
#.  If the eigenvalue equals 1, the activities never differ from the initial condition.
#.  This makes sense with the equation above. Lambda is raised to a power when computing activities:
#.  if it's a fraction, this term will get smaller so the activities will. If above 1, this term
#.   will explore so the activities will.

# 3) If the eigenvalue is between -1 and 0, the neural activities jump across the
#.   origin repeatedly along the eigenvector but eventually decay to 0. If the eigenvalue is below -1, the
#.   activities jump across the origin repeatedly along the eigenvector but explode to
#.   positive or negative infinity. Once again, this makes sense if you think through the equation above.