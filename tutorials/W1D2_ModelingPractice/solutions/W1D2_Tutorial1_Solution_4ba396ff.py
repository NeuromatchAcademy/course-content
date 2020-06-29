with plt.xkcd():
  plt.figure(figsize=(8,6))

  #####################################
  ## determine which variables you want to look at, replace question marks

  # determine which variables you want to look at, replace question marks
  plt.hist(s_ves, label='a', alpha=0.5) # set the first argument here
  plt.hist(s_opt, label='b', alpha=0.5) # set the first argument here
  # change labels if you need them
  #####################################

  plt.legend(facecolor='xkcd:white')
  plt.show()