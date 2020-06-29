
x_vec = np.linspace(x.min()-.5, x.max()+.5)

with plt.xkcd():
  plt.figure()

  for order in range(0, max_order+1):
    X_design = make_design_matrix(x_vec, order)
    plt.plot(x_vec, np.dot(X_design, theta_hat[order]));

  plt.ylabel('y')
  plt.xlabel('x')
  plt.plot(x, y, 'C0.');
  plt.legend([f'order {o}' for o in range(max_order+1)], loc=1)
  plt.title('polynomial fits')
  plt.show()