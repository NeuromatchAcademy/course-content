# Hidden Dynamics


Today you will learn about Hidden Markov Models (HMMs), which allow us to infer things in the world from a stream of data. Tutorials will continue our two running examples that help provide intuition: fishing (for a binary latent state) and tracking astrocat (for a gaussian latent state). In both examples, we've set up interactive visualizations to provide intuition, and then students will recreate the key inferences step by step. For the binary case, we start with a simple version where the latent state doesn't change, then we'll allow the latent state to change over time. There's plenty of bonus material, but your core learning objective is to understand and implement an algorithm to infer a changing hidden state from observations.

The HMM combines ideas from the linear dynamics lessons (which used Markov models) with inferences described in the Bayes day (which used Hidden variables). It also connects directly to later lessons in Optimal Control and Reinforcement Learning, which often use the HMM to guide actions.

The HMM is a pervasive model in neuroscience. It is used for data analysis, like inferring neural activity from fluorescence images. It is also a foundational model for what the brain should compute, as it interprets the physical world that is observed only through its senses.
