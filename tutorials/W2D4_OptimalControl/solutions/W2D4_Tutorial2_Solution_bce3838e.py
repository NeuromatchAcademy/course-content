
class LDS:
    def __init__(self, T, ini_state, noise_var, goal):
        self.T = T
        self.goal = goal
        self.ini_state = ini_state
        self.noise_var = noise_var
    
    
    def dynamics(self, D, B):

        s = np.zeros(self.T) # states initialization
        s[0] = self.ini_state

        noise = np.random.normal(0, self.noise_var, self.T)
        
        for t in range(self.T - 1):
            s[t + 1] = D * s[t] + noise[t]
        
        return s

    def dynamics_openloop(self, D, B, a):

        s = np.zeros(self.T) # states initialization
        s[0] = self.ini_state

        noise = np.random.normal(0, self.noise_var, self.T)
        
        for t in range(self.T - 1):
            s[t + 1] = D * s[t] + B * a[t] + noise[t]
        
        return s
  
    def dynamics_closedloop(self, D, B, L):

        s = np.zeros(self.T) # states initialization
        s[0] = self.ini_state

        noise = np.random.normal(0, self.noise_var, self.T)
        a = np.zeros(self.T - 1)

        for t in range(self.T - 1):
            a[t] =  L[t] * s[t] 
            s[t + 1] = D * s[t] + B * a[t] + noise[t]
        
        return s, a   
