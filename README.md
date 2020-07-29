# NeuroMatch Academy (NMA) syllabus

*July 13-31, 2020*

**Objectives**: Introduce traditional and emerging computational neuroscience tools, their complementarity, and what they can tell us about the brain. A main focus is on modeling choices, model creation, model evaluation and understanding how they relate to biological questions.

**Tutorial microstructure**: ~5min talk, ~15min hands-on (repeated)

**Day structure**: Opening keynote, 3h15min lecture/live Q&A/tutorial modules, 40min group discussion, 55min interpretation lecture (Outro) + live Q&As (what did we learn today, what does it mean, underlying philosophy). There will also be many networking activities (professional development sessions, yoga, social hangouts etc)! Details below.

**Note for visitors from China**: This repository contains many links to YouTube and Google Colab. We have a version of the repository with those same videos posted on bilibili, and the Google Colab links replaced with links to Aliyun. Please visit the [China Accessible Neuromatch Course-Content](https://github.com/erlichlab/course-content/)

**Prerequisites**: [See here](https://github.com/NeuromatchAcademy/precourse)

# Course materials

- [Welcome Video](https://youtu.be/s4kBB1OMs0Q)
- [**Tutorials**: videos, notebooks, and slides](./tutorials/README.md)
- [**Projects**: videos, notebooks, and slides](./projects/README.md)

Group projects are offered for the *interactive track* only and will be running during all 3 weeks of NMA!

# Course outline

* [Week 0](#week-0)
    * [Thu, July 9: Python for NMA Part 1](#python-for-nma-workshop)
    * [Fri, July 10: Python for NMA Part 2](#python-for-nma-workshop) 
* [Week 1](#week-1)
    * [Mon, July 13: Model Types](#mon-july-13-model-types)
    * [Tue, July 14: Modeling Practice](#tue-july-14-modeling-practice)
    * [Wed, July 15: Model Fitting](#wed-july-15-model-fitting)
    * [Thu, July 16: Machine Learning: GLM](#thu-july-16-machine-learning)
    * [Fri, July 17: Dimensionality Reduction](#fri-july-17-dimensionality-reduction)
    
 * [Professional Development](#weekend-1-july-18--19)
    
* [Week 2](#week-2)
    * [Mon, July 20: Bayesian Statistics](#mon-july-20-bayesian-statistics)
    * [Tue, July 21: Linear Systems](#tue-july-21-linear-systems)
    * [Wed, July 22: Decision Making](#wed-july-22-decision-making)
    * [Thu, July 23: Optimal Control](#thu-july-23-optimal-control)
    * [Fri, July 24: Reinforcement Learning](#fri-july-24-reinforcement-learning)
    
 * [Professional Development](#weekend-2-july-25--26)
 
* [Week 3](#week-3)
    * [Mon, July 27: Real Neurons](#mon-july-27-real-neurons)
    * [Tue, July 28: Dynamic Networks](#tue-july-28-dynamic-networks)
    * [Wed, July 29: Network Causality](#wed-july-29-network-causality)    
    * [Thu, July 30: Deep Learning 1](#thu-july-30-deep-learning-1)
    * [Fri, July 31: Deep Learning 2](#fri-july-31-deep-learning-2)

----

## Week 0

### Python for NMA workshop

**Description** Two-day workshop for absolute Python beginners. Learn essential Python skills for course tutorials and practice by coding a neuronal simulation.


----

## Week 1

### Mon, July 13: Model Types

**Description** Introduce different example model types (Marr 1-3, what/how/why) and the kinds of questions they can answer. Realize how different models map onto different datasets.

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    Model classifications                                              |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    "What"/"How" models                                                |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break + Physical Activity      |    BREAK incl. 20min yoga session                                     |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    "Why" model & discussion                                           |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, The role of models in discovery                     |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session

----

### Tue, July 14: Modeling Practice

**Description** Introduction to the process of building models.

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    How to approach modeling                                          |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Framing the question                                               |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break                          |    BREAK                                                              |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Model implementation and testing                                   |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, the modeling process                                |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


----

### Wed, July 15: Model Fitting

**Description** Fit models to data, quantify uncertainty, compare models

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    Why and how to fit models                                          |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Fit a model 1 (linear regression), Get error bars                  |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break + Physical Activity      |    BREAK incl. 20min yoga session                                     |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Compare models, cross-validation, hyperparameters, Fit a model 2  (nonlinear models) |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, Critical evaluation of model fitting                |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


----

### Thu, July 16: Machine Learning: GLM

**Description** Introduction to machine learning. The commonly used approaches, how to avoid false positives, how to do it well

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    We want to predict ([scikit learn](https://scikit-learn.org/))    |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Introduction to GLMs and predicting neural responses               |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break + Physical Activity      |    BREAK incl. 20min yoga session                                     |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Logistic regression, regularization, and decoding neural activity      |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, Promises and pitfalls of ML for Neuroscience        |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Fri, July 17: Dimensionality Reduction

**Description** Concept of dimensionality reduction, ways of doing it, what it means

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    Manifolds to understand                                           |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    PCA 1 (orthonormal basis), PCA 2 (eigenvalues)                     |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break                          |    BREAK                                                              |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    MNIST with PCA, MNIST with t-SNE                                   |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, The link between high-dimensional brain signals and low-dimensional behavior    |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Weekend 1: [Professional Development & Social](https://github.com/NeuromatchAcademy/course-content#professional-development-sessions) 

**Description** Professional development sessions and social activities will be offered on the weekend. More information, including exact times are available on the Neurostars Calendar

----
----

## Week 2

### Mon, July 20: Bayesian Statistics

**Description** Bayesian statistics, modeling of behavior, modeling of neural data, quantifying information

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    Uncertainty                                                        |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Bayes rule: cue combination and marginalization                    |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break + Physical Activity      |    BREAK incl. 20min yoga session                                     |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Bayesian Decision Theory & Causal inference                        |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, Advanced Bayesian methods                           |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Tue, July 21: Linear Systems

**Description** How to make estimates over time, how the brain does it

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    World has time                                                     |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Linear systems theory I (ND deterministic) and Markov process      |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break                          |    BREAK                                                              |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Linear systems theory II (1D stochastic = OU process; ND stocastic = AR(1)) and State space model |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, Linear systems rule the world                       |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Wed, July 22: Decision Making

**Description** How we can make decisions when information comes in over time

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    We need to decide stuff                                            |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Information theory, Sequential Probability Ratio Test (SPRT)       |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break + Physical Activity      |    BREAK incl. 20min yoga session                                     |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Hidden Markov Model inference (DDM), Kalman filter                 |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, Decisions, decisions, decisions ...                 |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Thu, July 23: Optimal Control

**Description** We need to move gain info and reach goals

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    We want to control our actions...                                  |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Expected utility / Cost, Markov decision process (MDP)             |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break + Physical Activity      |    BREAK incl. 20min yoga session                                     |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    LQG control (MDP for linear systems), Motor control (signal-dependent noise, time cost, ...) |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, Advanced motor control                              |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Fri, July 24: Reinforcement Learning

**Description** The setting of reinforcement learning and how it approximates the real world, behavior, and potential brain implementations

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    We want reward now and in the future...                           |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Predicting rewards, learning to act in one-step tasks, Exploration vs exploitation |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break                          |    BREAK                                                              |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Learning to act in multi-step tasks, on-policy vs. off-policy control, Model-based vs model-free RL          |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, RL and the brain                                    |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


----

### Weekend 2: [Professional Development & Social](https://github.com/NeuromatchAcademy/course-content#weekend-2-july-25--26) 

**Description** Professional development sessions and social activities will be offered on the weekend. More information, including exact times are available on the Neurostars Calendar

----
----

## Week 3

### Mon, July 27: Real Neurons

**Description** The things neurons are made of, channels, morphologies, neuromodulators, and plasticity

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    Real neurons ftw                                                   |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Reduced neuron models and transfer of synchrony                    |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break + Physical Activity      |    BREAK incl. 20min yoga session                                     |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Short-term plasticity of synapses and Hebbian plasticity & STDP    |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, A variety of neuron models                          |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:05-7:05     |    Social hour                        |    Social hour                                                        |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Tue, July 28: Dynamic Networks

**Description** How single neurons create population dynamics

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    Mechanistic models of different types of brain actvivity           |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    2D dynamical systems, Wilson-Cowen model (coarse-grained), oscillations & synchrony |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break                          |    BREAK                                                              |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Attractors & local linearization around fixed points, Balanced Amplification & Inhibition-stabilized network |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, A theory of the whole brain                         |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:05-7:05     |    Social hour                        |    Social hour                                                        |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Wed, July 29: Network Causality

**Description** Ways of discovering causal relations, ways of estimating networks, what we can do with networks

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    Causality - different views                                        |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Pittfalls of Granger and Centrality                                |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break + Physical Activity      |    BREAK incl. 20min yoga session                                     |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Instrumental Variables and interventions                           |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, Ladders of causality                                |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Thu, July 30: Deep Learning 1

**Description** The concept of ANNs, how to train them,what they are made out of, convnets, and how to fit them to brains

|    Time (Hour)   |    Lecture                            |    Details                                                            |
|------------------|---------------------------------------|-----------------------------------------------------------------------|
|    -0:30-0:00\*   |    Intro / keynote & tutorial setup   |    DL = crucial tool                                                  |
|    0:00-0:15     |    Pod Discussion I                   |    Lecture discussion with pod TA                                     |
|    0:20-1:35     |    Tutorials + nano-lectures I        |    Pytorch intro & model components, Training it & inductive bias     |
|    1:35-1:55     |    Pod Discussion II                  |    Discussion with pod TA                                             |
|    1:55-2:55     |    Big break + Physical Activity      |    BREAK incl. 20min yoga session                                     |
|    2:55-4:10     |    Tutorials + nano-lectures II       |    Convolutional Neural Network, Fit to brain (RSA - represenatational similarity analysis) |
|    4:10-4:30     |    Pod Discussion III                 |    Discussion with pod TA                                             |
|    4:35-5:05**     |    Outro                              |    Recap session, Digging deep                                        |
|    5:05-6:05     |    Q&A                                |    Q&A with lecturers/Mentors                                         |
|    6:00-7:00     |    Social Activity                    |    Hangout in Mozilla Hubs                                            |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


---- 

### Fri, July 31: Deep Learning 2

**Description** Deep learning and autoencoders for structure discovery + end-of-course celebration

|    Time (Hour)   |    Lecture                            |    Details                                                            |
--------------------|--------------------------------------|------------------------------------------------------------------------|
|-0:30-0:00\*		| Intro					| DL for structure |
|0:00-0:15		| Pod Discussion I		| Lecture discussion with pod TA |
|0:20-1:40		|Tutorial 				| Variational autoencorders and uses in Neuroscience |
|1:45-1:55		| Pod Discussion II		| Discussion with pod TA |
|1:55-2:55		| Big Break				|                                             |
|3:00-3:30**		| Outro					| Application of DL autoencoders |
|3:35-4:05		| Faculty QA				| Shortened QA |
|4:05-4:30		| Evals					| Fill in our end of term evaluation survey |
|4:30-5:15		| Project presentations	| Presentation and discussion of projects in small groups in your superpod |
|5:15-5:30		| Pod farewell			| Closing discussion of NMA with your pod |
|5:40-6:10		| NMA project highlights	| Highlights and discussion of the project experience |
|6:15-7:00		| NMA closing 			| Celebration, shared experience, credits, memories, call to action and the future! |

\* the Intro / keynote will be watched asynchronously, which means that you can watch this lecture before the start of the day
\** please watch the Outro on your own after having completed the tutorials and before the Q&A session


----


## Networking (throughout) - interactive track only

* Meet a prof about your group's project
* Meet a prof about your career
* Meet a prof about your own project
* Meet other participants interested in similar topics
* Meet a group of likeminded people
* Meet people that are local to you (same city, country)

----
# Professional Development Sessions
These are hour-long live-streamed events with a panel of speakers that will discuss a topic and answer audience questions.  For times in the relevant time-zones, see the [Neurostars Calendar](https://neurostars.org/t/professional-development-and-social-calendar/10496). These sessions will be recorded for later replay. Some sessions are duplicated to ensure coverage for students in different time-zones. 

## Weekend 1: July 18 & 19
|   Session   |  Date |   Description                                                         |
|-------------------|--------------------|----------------------------------------------------------------------|
|   **2.1: Data Sharing and Management**| July 18, 13:00 UTC | Dimitri Yatsenko (DataJoint), Edgar Walker (DataJoint), Ben Dichter (NWB) <br>Software tools for efficient management, analysis, and sharing of experimental data.<br>[https://www.crowdcast.io/e/nma/18](https://www.crowdcast.io/e/nma/18)
|    **2.2: Data Sharing and Management**| July 18, 23:00 UTC |  Russ Poldrack (Stanford)<br> Efficient data management and sharing strategies focusing on fMRI data. <br>[https://www.crowdcast.io/e/nma/20](https://www.crowdcast.io/e/nma/20)                                             
|   **3.1 Open Science**  | July 19, 0:00 UTC | Nici Pfeiffer (COS), Mark Musen (CEDAR, Stanford)<br> The Center for Open Science develops tools for project management, collaboration, preregistration, and data sharing. CEDAR enables investigators to author metadata, annotating experimental datasets to make data more findable, accessible, interoperable, and reusable (FAIR). <br>[https://www.crowdcast.io/e/nma/21](https://www.crowdcast.io/e/nma/21)  
|   **4.1 Visualization**  |July 18 16:00 UTC |  Colin Prahl (Artist), Amy Robinson Sterling (Eyewire), Helena Ledmyr (INCF)<br> Data Visualization and communication. Neuroscience-inspired art. <br>[https://www.crowdcast.io/e/nma/19](https://www.crowdcast.io/e/nma/19)      
|    **5.1 Publishing**  |  July 19, 18:00 UTC|Brett Mensh (Optimize Science)<br>   Maximizing the impact of your paper and the journal it gets into.<br>[https://www.crowdcast.io/e/nma/24](https://www.crowdcast.io/e/nma/24) 
|    **6.1 Philosophy**  |  July 19, 1:00 UTC|Lisa Miracchi (U Penn)<br>  What is the difference between “what a cognitive agent does” and “what processes happen inside an agent”? Lisa Miracchi, philosophy professor at UPenn, talks about how this distinction relates to selecting models.<br>[https://www.crowdcast.io/e/nma/22](https://www.crowdcast.io/e/nma/22) 
|    **6.2 Philosophy**  | July 19, 15:00 UTC|  Lisa Miracchi (U Penn)<br> What is the difference between “the content of representations” and “the content of perceptions and thoughts”? Lisa Miracchi, philosophy professor at UPenn, talks about Marr’s Computational Level and how these questions relate to what robots might internally represent.<br>[https://www.crowdcast.io/e/nma/23](https://www.crowdcast.io/e/nma/23) 


## Weekend 2: July 25 & 26
|    Session   |   Date|    Description                                                            |
|-------------------|--------------------|-----------------------------------------------------------------------|
|  **1.1 Inclusive Neuroscience**  |  July 25, 16:00 UTC|  NMA Staff <br> A goal of the NMA is to lower the barriers for learning about neuroscience.  These barriers take many forms and this session will feature organizers discussing what we have done to make our platform more inclusive. We will wrap up with suggestions from students about how we can improve for next year. Bring your suggestions please!<br>[http://neuromatchacademy.org/stream](http://neuromatchacademy.org/stream)   
|  **3.1 Open Science**  |  July 25, 15:00 UTC|  Nici Pfeiffer (COS), Mark Musen (CEDAR, Stanford) <br> The Center for Open Science develops tools for project management, collaboration, preregistration, and data sharing. CEDAR enables investigators to author metadata, annotating experimental datasets to make data more findable, accessible, interoperable, and reusable (FAIR).<br>[http://neuromatchacademy.org/stream](http://neuromatchacademy.org/stream)       
|   **7.1 FRL Career Forum**  | July 26 01:00 UTC | Facebook Reality Labs (FRL) researchers, developers, and engineers are building the future of connection within AR/VR. Join our ‘FRL Career Forum’ to hear from our scientists about how we use computational neuroscience & machine learning – and from our recruiters about job opportunities. Excited to meet the many diverse talents from NMA! <br>[http://neuromatchacademy.org/stream](http://neuromatchacademy.org/stream)  
|   **7.2 FRL Career Forum**  | July 26 14:00 UTC | Facebook Reality Labs (FRL) researchers, developers, and engineers are building the future of connection within AR/VR. Join our ‘FRL Career Forum’ to hear from our scientists about how we use computational neuroscience & machine learning – and from our recruiters about job opportunities. Excited to meet the many diverse talents from NMA! <br>[http://neuromatchacademy.org/stream](http://neuromatchacademy.org/stream)   
|   **8.1 Careers in Industry** | July 25 20:00 UTC| Becky Clarkson (Apple), Kyle Frankovich (Insight Data Science), Kachi Odoememe (APL)<br> Research careers in industry. <br>[http://neuromatchacademy.org/stream](http://neuromatchacademy.org/stream)  
|   **8.2 Careers in Industry**  | July 25 18:00 UTC| Feryal Behbahani (DeepMind), Sophie Kenny (Vpixx), Graeme Moffat (System2 Neurotechnology) <br>Research careers in industry.<br>[http://neuromatchacademy.org/stream](http://neuromatchacademy.org/stream)  
|   **9.1 Careers in Academia**  | July 26 05:00 UTC | S.P. Arun (IISc), Minhae Kwon (Soongsil University), Taro Toyoizumi (RIKEN) <br> Research careers in academia.<br>[http://neuromatchacademy.org/stream](http://neuromatchacademy.org/stream)   
|   **9.3 Careers in Academia**  | July 26 16:00 UTC  | Russ Poldrack (Stanford), Xiao-Jing Wang (NYU) <br> Research careers in academia.<br>[http://neuromatchacademy.org/stream](http://neuromatchacademy.org/stream)  
|   **10.1 How We Built This**  | July 26 20:00 UTC | Ella Batty, Patrick Mineault, Madineh Sarvestani, Tara van Viegen, Michael Waskom, <br>2000 students, 200 TAs, 200 volunteers, 20 days of content, 20 hours of video - how we built and launched NMA in 2 months.<br>[http://neuromatchacademy.org/stream](http://neuromatchacademy.org/stream) 




----

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work and everything in this repo is licensed under a [Creative Commons Attribution 4.0 International
License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
