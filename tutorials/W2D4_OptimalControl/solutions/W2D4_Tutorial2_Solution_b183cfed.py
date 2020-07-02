
L = -np.ones(T) * (min_error_controlgain+0.4)

s_closed_loop, a_closed_loop = lds.dynamics_closedloop(D, B, L)

with plt.xkcd():
    fig = plt.figure(figsize=(8, 6))
    plot_vs_time(s_closed_loop,'Closed Loop state','b',goal)
    plt.title('Closed Loop State Evolution with Over-Ambitious Control Gain')
    plt.show()
