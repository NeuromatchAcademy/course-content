
class MyKalmanFilter():
    def __init__(self, n_dim_state, n_dim_obs, transition_matrices, transition_covariance, observation_matrices,
                observation_covariance, initial_state_mean, initial_state_covariance, control_matrices):
        """
        @param n_dim_state: dimension of the laten variables
        @param n_dim_obs: dimension of the observed variables
        @param transition_matrices: state update matrix
        @param transition_covariance: process noise
        @param observation_matrices: measurement matrix
        @param observation_covariance: measurement noise
        @param initial_state_mean: initial state estimate
        @param initial_state_covariance: initial estimate on state variance
        @param control_matrices: control weights on state updates
        """
        self.n_dim_state = n_dim_state 
        self.n_dim_obs = n_dim_obs
        self.transition_matrices = transition_matrices #np.eye(n_dim_state)
        self.transition_covariance = transition_covariance #np.eye(n_dim_state) 
        self.observation_matrices = observation_matrices #np.eye(n_dim_obs, n_dim_state)
        self.observation_covariance = observation_covariance #np.eye(n_dim_obs)
        self.initial_state_mean = initial_state_mean #np.zeros(n_dim_state)
        self.initial_state_covariance = initial_state_covariance #np.eye(n_dim_state)
        
        self.control_matrices = control_matrices #np.eye(n_dim_state)
        

    def filter_control(self, n_timesteps, control_gain, use_myfilter=True):
        """
        Method that performs Kalman filtering and LQG controller
        @param n_timesteps: length of the data sample
        @param control_gain: a numpy array whose dimension is [n_timesteps, self.n_dim_state]
        @output: filtered_state_means: a numpy array whose dimension is [n_timesteps, self.n_dim_state]
        @output: filtered_state_covariances: a numpy array whose dimension is [n_timesteps, self.n_dim_state, self.n_dim_state]
        @output: latent_state: a numpy array whose dimension is [n_timesteps, self.n_dim_state]
        @output: observed_state: a numpy array whose dimension is [n_timesteps, self.n_dim_obs]
        @output: control: a numpy array whose dimension is [n_timesteps, self.n_dim_state]
        """

        # validate inputs
        #n_example, observed_dim = X.shape
        #assert observed_dim == self.n_dim_obs
        
        n_example = n_timesteps
        observed_dim = self.n_dim_obs
        latent_state = []
        observed_state = []
        control = []
        
        current_latent_state = self.initial_state_mean #initial_state
        control.append(self.initial_state_mean)
        latent_state.append(current_latent_state)
        observed_state.append(np.dot(self.observation_matrices, current_latent_state) +
                                  np.random.multivariate_normal(np.zeros(self.n_dim_obs), self.observation_covariance))



        # create holders for outputs
        filtered_state_means = np.zeros([n_example, self.n_dim_state])
        filtered_state_covariances = np.zeros([n_example, self.n_dim_state, self.n_dim_state])


        if use_myfilter:
            # the first state mean and state covar is the initial expectation
            filtered_state_means[0] = self.initial_state_mean
            filtered_state_covariances[0] = self.initial_state_covariance

            # initialize internal variables
            current_state_mean = self.initial_state_mean.copy()
            current_state_covar = self.initial_state_covariance.copy()
            self.p_n_list = np.zeros((n_example, self.n_dim_obs, self.n_dim_obs))
            
            for i in range(1, n_example):
                #print(current_latent_state)
                
                ################### LQG #################################
                current_action =  control_gain[i] * current_state_mean
                control.append(current_action)    
                ##########################################################
                
                ################## sample ################################
                latent_state.append(np.dot(self.transition_matrices, current_latent_state) +
                                    np.dot(self.control_matrices, current_action) + 
                                    np.random.multivariate_normal(np.zeros(self.n_dim_state),
                                                                  self.transition_covariance))
                current_latent_state = latent_state[-1]

                # use observation_matrices and observation_covariance to calculate next observed state
                observed_state.append(np.dot(self.observation_matrices, current_latent_state
                                            ) + np.random.multivariate_normal(np.zeros(self.n_dim_obs), self.observation_covariance))
               
                current_observed_data = observed_state[-1]
                ##########################################################

                # run a single step forward filter
                # prediction step
                
                predicted_state_mean = np.dot(self.transition_matrices, current_state_mean
                                             ) + np.dot(self.control_matrices, current_action)
                predicted_state_cov = np.matmul(np.matmul(self.transition_matrices, current_state_covar),
                                                np.transpose(self.transition_matrices)) + self.transition_covariance
                # observation step
                innovation = current_observed_data - np.dot(self.observation_matrices, predicted_state_mean)
                innovation_covariance = np.matmul(np.matmul(self.observation_matrices, predicted_state_cov),
                                                  np.transpose(self.observation_matrices)) + self.observation_covariance
                # update step
        
     
                kalman_gain = np.matmul(np.matmul(predicted_state_cov, np.transpose(self.observation_matrices)),
                                        np.linalg.inv(innovation_covariance))
                current_state_mean = predicted_state_mean + np.dot(kalman_gain, innovation) 
                current_state_covar = np.matmul((np.eye(current_state_covar.shape[0]) -
                                                 np.matmul(kalman_gain, self.observation_matrices)),
                                                predicted_state_cov)
                # populate holders
                filtered_state_means[i, :] = current_state_mean
                filtered_state_covariances[i, :, :] = current_state_covar
                self.p_n_list[i, :, :] = predicted_state_cov
                # self.p_n_list[i-1, :, :] = predicted_state_cov
                # new
                # self.p_n_list[-1, :, :] = np.matmul(np.matmul(self.transition_matrices, filtered_state_covariances[-1,:,:]),
                #                                    np.linalg.inv(self.transition_matrices)) + self.transition_covariance

#         else:
#             #################################################################################
#             # below: this is an alternative if you do not have an implementation of filtering
#             kf = KalmanFilter(n_dim_state=self.n_dim_state, n_dim_obs=self.n_dim_obs)
#             need_params = ['transition_matrices', 'observation_matrices', 'transition_covariance',
#                            'observation_covariance', 'initial_state_mean', 'initial_state_covariance']
#             for param in need_params:
#                 setattr(kf, param, getattr(self, param))
#             filtered_state_means, filtered_state_covariances = kf.filter(X)
#             #################################################################################
        
        filtered_state_means = np.squeeze(np.array(filtered_state_means))
        filtered_state_covariances = np.squeeze(np.array(filtered_state_covariances))
        latent_state = np.squeeze(np.array(latent_state))
        observed_state = np.squeeze(np.array(observed_state))
        control = np.squeeze(np.array(control))
        
        
        return filtered_state_means, filtered_state_covariances, latent_state, observed_state, control

    def plot_state_vs_time(self, n_timesteps, control_gain, use_myfilter=True):
        filtered_state_means_impl, filtered_state_covariances_impl, latent, measurement, control = self.filter_control(
            n_timesteps, control_gain)

        fig = plt.figure(figsize=(12, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[1, 2]) 

        ax0 = plt.subplot(gs[0])
        ax0.plot(latent,filtered_state_means_impl, 'b.')
        ax0.set_xlabel('latent state')
        ax0.set_ylabel('estimated state')
        ax0.set_aspect('equal')

        ax1 = plt.subplot(gs[1])
        ax1.plot(latent, 'b', label = 'latent state')
        ax1.plot(filtered_state_means_impl, 'r', label = 'estimated state')
        ax1.set_xlabel('time')
        ax1.set_ylabel('state')
        ax1.legend(loc="upper right")
        plt.tight_layout()
        plt.show()
