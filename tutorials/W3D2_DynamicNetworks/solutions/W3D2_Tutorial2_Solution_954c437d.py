pars = default_pars()
x_fp_1 = my_fp(pars, 0.1, 0.1)
x_fp_2 = my_fp(pars, 0.3, 0.3)
x_fp_3 = my_fp(pars, 0.8, 0.6)

#print ('Fixed Point1 = (%.3f, %.3f)' %(x_fp_1[0], x_fp_1[1]))
#print ('Fixed Point2 = (%.3f, %.3f)' %(x_fp_2[0], x_fp_2[1]))
#print ('Fixed Point3 = (%.3f, %.3f)' %(x_fp_3[0], x_fp_3[1]))

with plt.xkcd():
  
  fig5 = plt.figure(figsize=(8, 5.5))
  my_plot_nullcline(pars)

  plt.plot(x_fp_1[0], x_fp_1[1], 'ko')
  plt.text(x_fp_1[0]+0.02, x_fp_1[1]+0.1, 'Fixed Point1=\n(%.3f, %.3f)' \
          %(x_fp_1[0], x_fp_1[1]), horizontalalignment='center', \
          verticalalignment='bottom')

  plt.plot(x_fp_2[0], x_fp_2[1], 'ko')
  plt.text(x_fp_2[0]+0.1, x_fp_2[1]-0.15, 'Fixed Point2=\n(%.3f, %.3f)' \
          %(x_fp_2[0], x_fp_2[1]), horizontalalignment='center', \
          verticalalignment='bottom')

  plt.plot(x_fp_3[0], x_fp_3[1], 'ko')
  plt.text(x_fp_3[0]+0.1, x_fp_3[1]-0.1, 'Fixed Point1=\n(%.3f, %.3f)' \
          %(x_fp_3[0], x_fp_3[1]), horizontalalignment='center', \
          verticalalignment='center', rotation=90)

  plt.xlabel('E')
  plt.ylabel('I')
  plt.legend(loc='best')

  plt.show()