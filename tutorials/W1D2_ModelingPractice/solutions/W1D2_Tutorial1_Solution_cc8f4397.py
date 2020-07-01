###################################################################
## Change the values in the lists below. 
## These act as X and Y coordinates for a scatter plot, so make sure
## the lists match in length.
################################################################### 

world_vel_exp = [0, 1] 
self_vel_exp  = [1, 0]

# the code below creates a figure with your predictions
expectations = {'world':world_vel_exp, 'self':self_vel_exp}

with plt.xkcd():
  my_plot_percepts(datasets={'expectations':expectations})