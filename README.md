# NeuroMatch Academy (NMA) syllabus

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
    * [Mon, July 20: Bayes](#mon-july-20-bayes)
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

**Description** Introduction of datasets (spikes, EEG, fMRI + behavior), and questions about them. These questions will foreshadow the whole summer school.

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | NMA organization, expectations, code of conduct, modeling vs. data |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Data intro, preprocessing                                          |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Link of neural data to behavior                                    |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Tuning (RFs, motor, STA)	                                        |
| 3:30 - 4:05 | Lecture & Tutorial 4             | What it means to "understand" (signal detection)                   |
| 4:35 - 5:30 | Recap, Q&A                       | Outlook on school                                                  |
| 5:30 - 6:00 | Professional development         | Being a good NMA participant                                       |


----

### Tue, July 14: What do models buy us?

**Description** Introduce different example model types (Marr 1-3, what/how/why) and the kinds of questions they can answer. MRealize how different models map onto different datasets.

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | Model classifications                                              |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Marr 1                                                             |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Marr 2-3                                                           |
| 2:10 - 2:45 | Lecture & Tutorial 3             | "What"                                                             |
| 3:30 - 4:05 | Lecture & Tutorial 4             | "How"/"Why"                                                        |
| 4:35 - 5:30 | Recap, Q & A                     | The role of models in discovery                                    |
| 5:30 - 6:00 | Professional development         | How-to-model guide 1                                               |

----

### Wed, July 15: Model fitting

**Description** Fit models to data, quantify uncertainty, compare models

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | Why and how to fit models                                          |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Fit a model 1 (linear regression)                                  |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Get error bars                                                     |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Compare models, cross-validation, hyperparameters                  |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Fit a model 2 (nonlinear models)                                   |
| 4:35 - 5:30 | Recap, Q & A                     | Critical evaluation of model fitting                               |
| 5:30 - 6:00 | Professional development         | How-to-model guide 2                                               |

----

### Thu, July 16: Machine learning (ML) - decoding

**Description** Introduction to machine learning. The commonly used approaches, how to avoid false positives, how to do it well

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | We want to predict ([scikit learn](https://scikit-learn.org/))     |
| 0:50 - 1:25 | Lecture & Tutorial 1             | GLMs (temporal filtering models)                                   |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Linear classifier (SVM)                                            |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Regularization (L1, L2)                                            |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Shallow nonlinear classifier (SVM with RBF kernel)                 |
| 4:35 - 5:30 | Recap, Q & A                     | Promises and pitfalls of ML                                        |
| 5:30 - 6:00 | Professional development         | How-to-model guide 3                                               |

---- 

### Fri, July 17: Dimensionality reduction / manifolds

**Description** Concept of dimensionality reduction, ways of doing it, what it means

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | Manifolds to understand                                            |
| 0:50 - 1:25 | Lecture & Tutorial 1             | PCA 1                                                              |
| 1:30 - 2:05 | Lecture & Tutorial 2             | PCA 2 (+CCA/clustering)                                            |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Signal vs. Noise Manifolds                                         |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Visualizing high-D nonlinear manifolds (e.g. t-SNE)                |
| 4:35 - 5:30 | Recap, Q & A                     | The link between high-dimensional brain signals and low-dimensional behavior |
| 5:30 - 6:00 | Professional development         | Efficient collaborations                                           |

----
----

## Week 2

### Mon, July 20: Bayes

**Description** Bayesian statistics, modeling of behavior, modeling of neural data, quantifying information

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | Uncertainty                                                        |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Bayes rule I (product rule: cue combination)                       |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Bayes rule II (Marginalization and nuisance variables)             |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Causal inference & structural models (use as example for marginalization) |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Bayesian decision theory                                           |
| 4:35 - 5:30 | Recap, Q & A                     | Advanced Bayesian methods                                          |
| 5:30 - 6:00 | Professional development         | Productivity tools for science                                     |

---- 

### Tue, July 21: Time series 1 (linear systems)

**Description** How to make estimates over time, how the brain does it

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | World has time                                                     |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Linear systems theory I (ND deterministic)                         |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Linear systems theory II (1D stochastic = OU process; ND stocastic = AR(1)) |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Markov process                                                     |
| 3:30 - 4:05 | Lecture & Tutorial 4             | State space model                                                  |
| 4:35 - 5:30 | Recap, Q & A                     | Linear systems rule the world                                      |
| 5:30 - 6:00 | Professional development         | Open source ecosystem, data management & sharing                   |


---- 

### Wed, July 22: Time series 2 (decision making)

**Description** How we can make decisions when information comes in over time

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | We need to decide stuff                                            |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Information theory                                                 |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Sequential Probability Ratio Test (SPRT)                           |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Hidden Markov Model inference (DDM)                                |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Kalman filter                                                      |
| 4:35 - 5:30 | Recap, Q & A                     | Decisions, decisions, decisions ...                                |
| 5:30 - 6:00 | Professional development         | Open science (general), replicability & reproducibility            |

---- 

### Thu, July 23: Optimal control

**Description** We need to move gain info and reach goals

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | We want to control our actions...                                  |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Expected utility / Cost                                            |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Markov decision process (MDP)                                      |
| 2:10 - 2:45 | Lecture & Tutorial 3             | LQG control (MDP for linear systems)                               |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Motor control (signal-dependent noise, time cost, ...)             |
| 4:35 - 5:30 | Recap, Q & A                     | Advanced motor control                                             |
| 5:30 - 6:00 | Professional development         | Networking at Conferences                                          |

---- 

### Fri, July 24: Reinforcement learning (RL)

**Description** The setting of reinforcement learning and how it approximates the real world, behavior, and potential brain implementations

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | Problem formulations: actor-critic                                 |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Critic: reward prediction error                                    |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Exploration (POMDP) vs Exploitation                                |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Model-based vs model-free RL                                       |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Multi-arm bandits: foraging                                        |
| 4:35 - 5:30 | Recap, Q & A                     | RL and the brain                                                   |
| 5:30 - 6:00 | Professional development         | Writing Papers & Grants                                            |

----
----

## Week 3

### Mon, July 27: Real neurons

**Description** The things neurons are made of, channels, morphologies, neuromodulators, and plasticity

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | Real neurons ftw                                                   |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Channels, HH                                                       |
| 1:30 - 2:05 | Lecture & Tutorial 2             | LIF neuron                                                         |
| 2:10 - 2:45 | Lecture & Tutorial 3             | LNP (loses fine timing info)                                       |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Hebbian plasticity & STDP                                          |
| 4:35 - 5:30 | Recap, Q & A                     | A variety of neuron models                                         |
| 5:30 - 6:00 | Professional development         | How to find a postdoc                                              |

---- 

### Tue, July 28: What happens in dynamic networks?

**Description** How single neurons create population dynamics

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | Mechanistic models of different types of brain actvivity.          |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Spikes to rates.                                                   |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Wilson-Cowen model (coarse-grained), oscillations & synchrony      |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Attractors & local linearization around fixed points               |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Chaos in rate networks (stimulus dependent chaotic attractor)      |
| 4:35 - 5:30 | Recap, Q & A                     | A theory of the whole brain                                        |
| 5:30 - 6:00 | Professional development         | Early career panel - academia (how to advance through career steps)|

---- 

### Wed, July 29: Causality & networks

**Description** Ways of discovering causal relations, ways of estimating networks, what we can do with networks

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | Causality - different views                                        |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Pitfalls of Granger Caausality                                     |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Centrality                                                         |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Instrumental variables                                             |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Interventions                                                      |
| 4:35 - 5:30 | Recap, Q & A                     | Latters of causality                                               |
| 5:30 - 6:00 | Professional development         | Computational neuroscience in industry - career panel              |

---- 

### Thu, July 30: Deep learning (DL) 1

**Description** The concept of ANNs, how to train them,what they are made out of, convnets, and how to fit them to brains

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | DL = crucial tool                                                  |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Pytorch intro & model components                                   |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Training it & inductive bias                                       |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Convolutional Neural Network                                       |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Fit to brain (RSA - represenatational similarity analysis)         |
| 4:35 - 5:30 | Recap, Q & A                     | Digging deep                                                       |
| 5:30 - 6:00 | Professional development         | Job fair (FRL)                                                     |

---- 

### Fri, July 31: Deep learning (DL) 2

**Description** Deep learning in more advanced settings. Autoencoders for structure discovery, RNNs, and fitting them to brains

| Time (Hour) | Lecture                          | Details                                                            |
|-------------|----------------------------------|--------------------------------------------------------------------|
| 0:00 - 0:50 | Intro / keynote & tutorial setup | DL for structure                                                   |
| 0:50 - 1:25 | Lecture & Tutorial 1             | Autoencoders                                                       |
| 1:30 - 2:05 | Lecture & Tutorial 2             | Recurrent Neural Network                                           |
| 2:10 - 2:45 | Lecture & Tutorial 3             | Transfer learning / generalization                                 |
| 3:30 - 4:05 | Lecture & Tutorial 4             | Causality                                                          |
| 4:35 - 5:30 | Recap, Q & A                     | Digging deeper                                                     |
| 5:30 - 6:00 | Professional development         | NMA wrap-up                                                        |

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
