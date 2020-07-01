
class LQR(LDS):
    def __init__(self, T, ini_state, noise_var, goal):
        super().__init__(T, ini_state, noise_var, goal)
    
    def control_gain_LQR(self, D, B, rho):
        P = np.zeros(self.T) # Riccati updates
        P[-1] = 1  
        
        L = np.zeros(self.T-1) # control gain 
        
        for t in range(self.T-1):
            P[self.T - t - 2] = (1 + 
                            P[self.T - t - 1] * D ** 2 - 
                            D * P[self.T - t - 1] * B / (
                                rho + P[self.T - t - 1] * B) * B ** 2 * P[self.T - t - 1] * D)

            L[self.T - t - 2] =  -(1 / (rho + P[self.T - t - 1] * B ** 2) * B * P[self.T - t - 1] * D) 
        
        return L

    def calculate_J_state(self, s):
        J_state = np.sum((s-self.goal) ** 2)
        return J_state      

    def calculate_J_control(self, a):
        J_control = np.sum(a ** 2) 
        return J_control
