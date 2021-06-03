np.random.seed(101)
nstep = 100
switch_prob = 0.1
log10_noise_level = -1

# Build model
model = create_HMM(switch_prob=switch_prob,
                     noise_level=10.**log10_noise_level,
                     startprob=[0.5, 0.5])
observations, states = model.sample(nstep)
# Infer state sequence
predictive_probs, posterior_probs = simulate_forward_inference(model, nstep,
                                                               observations)
states_inferred = posterior_probs <= 0.5

with plt.xkcd():
  plot_forward_inference(model, states, observations, states_inferred)