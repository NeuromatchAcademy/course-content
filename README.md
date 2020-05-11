# NeuroMatch Academy (NMA) penultimate syllabus

*July 13-31, 2020*

**Objectives**: Introduce traditional and emerging computational neuroscience tools, their complementarity, and what they can tell us about the brain. A main focus is on modeling choices, model creation, model evaluation and understanding how they relate to biological questions.

**Tutorial microstructure**: ~10min talk, ~20min tutorial (repeated)

**Day structure**: Opening keynote, 3h lecture/tutorial modules, 1h interpretation (what did we learn today, what does it mean, underlying philosophy, 1h professional development/ meta-science, evening group projects (for interactive track). There will also be many networking activities!

**Prerequisites**: [See here](https://github.com/NeuromatchAcademy/precourse)

# Course outline

* [Week 1](#week-1)
    * [Mon, July 13: Introduction to Computational Neuroscience and NMA](#mon-july-13-introduction-to-computational-neuroscience-and-nma)
    * [Tue, July 14: What do models buy us?](#tue-july-14-what-do-models-buy-us)
    * [Wed, July 15: Model fitting](#wed-july-15-model-fitting)
    * [Thu, July 16: Machine learning (ML) - decoding](#thu-july-16-machine-learning-ml---decoding)
    * [Fri, July 17: Dimensionality reduction / manifolds](#fri-july-17-dimensionality-reduction--manifolds)
* [Week 2](#week-2)
    * [Mon, July 20: The Bayesian brain](#mon-july-20-the-bayesian-brain)
    * [Tue, July 21: Time series 1 (linear systems)](#tue-july-21-time-series-1-linear-systems)
    * [Wed, July 22: Time series 2 (decision making)](#wed-july-22-time-series-2-decision-making)
    * [Thu, July 23: Optimal control](#thu-july-23-optimal-control)
    * [Fri, July 24: Reinforcement learning (RL)](#fri-july-24-reinforcement-learning-rl)
* [Week 3](#week-3)
    * [Mon, July 27: Real neurons](#mon-july-27-real-neurons)
    * [Tue, July 28: What happens in dynamic networks?](#tue-july-28-what-happens-in-dynamic-networks)
    * [Wed, July 29: Causality &amp; networks](#wed-july-29-causality--networks)
    * [Thu, July 30: Deep learning (DL) 1](#thu-july-30-deep-learning-dl-1)
    * [Fri, July 31: Deep learning (DL) 2](#fri-july-31-deep-learning-dl-2)

----

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
----

## Week 3

### Mon, July 27: Real neurons
The things neurons are made of, channels, morphologies, neuromodulators, and plasticity

**Intro / keynote & tutorial setup** (0:00 - 0:50): Real neurons ftw

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Channels, HH | LIF neuron | LNP (loses fine timing info) | Hebbian plasticity & STDP |

**Recap, Q&A** (4:35 - 5:30): A variety of neuron models

**Professional development** (5:30 - 6:00): How to find a postdoc

---- 

### Tue, July 28: What happens in dynamic networks?
How single neurons create population dynamics

**Intro / keynote & tutorial setup** (0:00 - 0:50): Mechanistic models of different types of brain actvivity

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Spikes to rates | Wilson-Cowen model (coarse-grained), oscillations & synchrony | Attractors & local linearization around fixed points | Chaos in rate networks (stimulus dependent chaotic attractor) |

**Recap, Q&A** (4:35 - 5:30): A theory of the whole brain

**Professional development** (5:30 - 6:00): Early career panel - academia (how to advance through career steps)

---- 

### Wed, July 29: Causality & networks
Ways of discovering causal relations, ways of estimating networks, what we can do with networks

**Intro / keynote & tutorial setup** (0:00 - 0:50): Causality - different views

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Pitfalls of Granger | Centrality | Instrumental variables | Interventions |

**Recap, Q&A** (4:35 - 5:30): Latters of causality

**Professional development** (5:30 - 6:00): Computational neuroscience in industry - career panel

---- 

### Thu, July 30: Deep learning (DL) 1
The concept of ANNs, how to train them,what they are made out of, convnets, and how to fit them to brains

**Intro / keynote & tutorial setup** (0:00 - 0:50): DL = crucial tool

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Pytorch intro & model components | Training it & inductive bias | ConvNets | Fit to brain (RSA - represenatational similarity analysis) |

**Recap, Q&A** (4:35 - 5:30): Digging deep

**Professional development** (5:30 - 6:00): Job fair (FRL)

---- 

### Fri, July 31: Deep learning (DL) 2
Deep learning in more advanced settings. Autoencoders for structure discovery, RNNs, and fitting them to brains

**Intro / keynote & tutorial setup** (0:00 - 0:50): DL for structure

| Lecture & tutorial 1 | Lecture & tutorial 2 | Lecture & tutorial 3 | Lecture & tutorial 4 |
| :---: | :---: | :---: | :---: |
| 0:50 - 1:25 | 1:30 - 2:05 | 2:10 - 2:45 | 3:30 - 4:05 |
| Autoencoders | RNN | Transfer learning / generalization | Causality |

**Recap, Q&A** (4:35 - 5:30): Digging deeper

**Professional development** (5:30 - 6:00): NMA wrap-up

----


## Networking (throughout) - interactive track only
* Meet a prof about your group's project
* Meet a prof about your career
* Meet a prof about your own project
* Meet other participants interested in similar topics
* Meet a group of likeminded people
* Meet people that are local to you (same city, country)

----


## Group projects (throughout) - interactive track only
TBA
