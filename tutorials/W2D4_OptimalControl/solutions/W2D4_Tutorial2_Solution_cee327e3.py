
goal = np.sin(np.arange(T) * 2 * np.pi * 5 /T) 

lqr_sine= LQR_tracking(T, ini_state, noise_var, goal)
L = lqr_sine.control_gain_LQR(D, B, rho)
s_lqr_sine, a_lqr_sine, a_bar_lqr_sine = lqr_sine.dynamics_tracking(D, B, L)
