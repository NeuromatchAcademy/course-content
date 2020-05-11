# Penultimate syllabus
Summer course content for Neuromatch Academy (NMA)
July 13-31, 2020

**Objectives**: Introduce traditional and emerging computational neuroscience tools, their complementarity, and what they can tell us about the brain. A main focus is on modeling choices, model creation, model evaluation and understanding how they relate to biological questions.

**Tutorial microstructure**: ~10min talk, ~20min tutorial (repeated)

**Day structure**: 4h methods, 1h interpretation (what did we learn today, what does it mean, underlying philosophy, 1h professional development/ meta-science, evening group projects for interactive track). There will also be many networking activities!

**Prerequisites**: [See here](https://github.com/NeuromatchAcademy/precourse)

## Week 1
### Mon, July 13: Introduction to Computational Neuroscience and NMA
Introduction of datasets (spikes, EEG, fMRI + behavior), and questions about them. These questions will foreshadow the whole summer school.

**Intro / keynote & tutorial setup** (0:00 - 0:50): NMA organization, expectations, code of conduct, modeling vs. data

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Data intro, preprocessing | Link of neural data to behavior | Tuning (RFs, motor, STA) | What it means to "understand" (signal detection) |

**Recap, Q&A** (4:35 - 5:30): Outlook on school

**Professional development** (5:30 - 6:00): Being a good NMA participant

----

### Tue, July 14: What do models buy us?
Introduce different example model types (Marr 1-3, what/how/why) and the kinds of questions they can answer. MRealize how different models map onto different datasets.

**Intro / keynote & tutorial setup** (0:00 - 0:50): Model classifications 

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Marr 1 | Marr 2-3 | "What" | "How"/"Why" |

**Recap, Q&A** (4:35 - 5:30): The role of models in discovery

**Professional development** (5:30 - 6:00): How-to-model guide 1

----

### Wed, July 15: Model fitting
Fit models to data, quantify uncertainty, compare models

**Intro / keynote & tutorial setup** (0:00 - 0:50): Why and how to fit models

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Fit a model 1 (linear regression) | Get error bars | Compare models, cross-validation, hyperparameters | Fit a model 2 (nonlinear models) |

**Recap, Q&A** (4:35 - 5:30): Critical evaluation of model fitting

**Professional development** (5:30 - 6:00): How-to-model guide 2

----

### Thu, July 16: Machine learning (ML) - decoding
Introduction to machine learning. The commonly used approaches, how to avoid false positives, how to do it well

**Intro / keynote & tutorial setup** (0:00 - 0:50): We want to predict (scikitlearn)...

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| GLMs (temporal filtering models) | Linear classifier (SVM) | Regularization (L1, L2) | Shallow nonlinear classifier (SVM with RBF kernel) |

**Recap, Q&A** (4:35 - 5:30): Promises and pitfalls of ML

**Professional development** (5:30 - 6:00): How-to-model guide 3

---- 

### Fri, July 17: Dimensionality reduction / manifolds
Concept of dimensionality reduction, ways of doing it, what it means

**Intro / keynote & tutorial setup** (0:00 - 0:50): Manifolds to understand

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| PCA 1 | PCA 2 (+CCA/clustering) | Signal vs. noise manifolds | Visualizing high-D nonlinear manifolds (e.g. tSNE) |

**Recap, Q&A** (4:35 - 5:30): The link between high-dimensional brain signals and low-dimensional behavior 

**Professional development** (5:30 - 6:00): Efficient collaborations

----

## Week 2

### Mon, July 20: The Bayesian brain
Bayesian statistics, modeling of behavior, modeling of neural data, quantifying information

**Intro / keynote & tutorial setup** (0:00 - 0:50): Uncertainty

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Bayes rule I (product rule: cue combination) | Bayes rule II (Marginalization and nuisance variables) | Causal inference & structural models (use as example for marginalization) | Bayesian decision theory |

**Recap, Q&A** (4:35 - 5:30): Advanced Bayesian methods

**Professional development** (5:30 - 6:00): Productivity tools for science

---- 

### Tue, July 21: Time series 1 (linear systems)
How to make estimates over time, how the brain does it

**Intro / keynote & tutorial setup** (0:00 - 0:50): World has time

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Linear systems theory I (ND deterministic) | Linear systems theory II (1D stochastic = OU process; ND stocastic = AR(1)) | Markov process | State space model |

**Recap, Q&A** (4:35 - 5:30): Linear systems rule the world

**Professional development** (5:30 - 6:00): Open source ecosystem, data management & sharing

---- 

### Wed, July 22: Time series 2 (decision making)
How we can make decisions when information comes in over time

**Intro / keynote & tutorial setup** (0:00 - 0:50): We need to decide stuff

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Information theory | Sequential Probability Ratio Test (SPRT) | Hidden Markov Model inference (DDM) | Kalman filter |

**Recap, Q&A** (4:35 - 5:30): Decisions, decisions, decisions...

**Professional development** (5:30 - 6:00): Open science (general), replicability & reproducibility

---- 

### Thu, July 23: Optimal control
We need to move gain info and reach goals

**Intro / keynote & tutorial setup** (0:00 - 0:50): We want to control our actions... 

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Expected utility / cost | Markov decision process (MDP) | LQG control (MDP for linear systems) | Motor control (signal-dependent noise, time cost, ...) |

**Recap, Q&A** (4:35 - 5:30): Advanced motor control

**Professional development** (5:30 - 6:00): Networking at Conferences

---- 

### Fri, July 24: Reinforcement learning (RL)
The setting of reinforcement learning and how it approximates the real world, behavior, and potential brain implementations

**Intro / keynote & tutorial setup** (0:00 - 0:50): Problem formulations: actor-critic

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Critic: reward prediction error | Exploration (POMDP) vs exploitation | Model-based vs model-free RL | Multi-arm bandits: foreaging |

**Recap, Q&A** (4:35 - 5:30): RL and the brain

**Professional development** (5:30 - 6:00): Writing Papers & Grants

----

## Week 3

### Mon, July 27: 


**Intro / keynote & tutorial setup** (0:00 - 0:50): Uncertainty

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
|  |  |  |  |

**Recap, Q&A** (4:35 - 5:30): 

**Professional development** (5:30 - 6:00):

---- 

### Tue, July 28: 


**Intro / keynote & tutorial setup** (0:00 - 0:50): Uncertainty

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
|  |  |  |  |

**Recap, Q&A** (4:35 - 5:30): 

**Professional development** (5:30 - 6:00):

---- 

### Wed, July 29: 


**Intro / keynote & tutorial setup** (0:00 - 0:50): Uncertainty

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
|  |  |  |  |

**Recap, Q&A** (4:35 - 5:30): 

**Professional development** (5:30 - 6:00):

---- 

### Thu, July 30: 


**Intro / keynote & tutorial setup** (0:00 - 0:50): Uncertainty

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
|  |  |  |  |

**Recap, Q&A** (4:35 - 5:30): 

**Professional development** (5:30 - 6:00):

---- 

### Fri, July 31:


**Intro / keynote & tutorial setup** (0:00 - 0:50): Uncertainty

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
|  |  |  |  |

**Recap, Q&A** (4:35 - 5:30): 

**Professional development** (5:30 - 6:00):
