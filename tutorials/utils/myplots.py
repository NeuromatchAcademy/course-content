#!/usr/bin/env python
# coding: utf-8

import time                        # import time 
import numpy as np                 # import numpy
import scipy as sp                 # import scipy
import math                        # import basic math functions
import random                      # import basic random number generator functions

import matplotlib.pyplot as plt    # import matplotlib
from IPython import display        


def my_plot_single(x, px):
    """
    Plots normalized Gaussian distribution
    
    Args:
      x (numpy array of floats):         points at which the likelihood has been evaluated
      px (numpy array of floats):    normalized probabilities for prior evaluated at each `x`
             
    Returns:
      Nothing.
    """
    if px is None:
        px = np.zeros_like(x)

    plt.plot(x, px, '-', color='xkcd:green', LineWidth=2, label='Prior')
    plt.legend()
    plt.ylabel('Probability')
    plt.xlabel('Orientation (Degrees)')


def my_plot(x, auditory=None, visual=None, posterior_pointwise=None):
    """
    Plots normalized Gaussian distributions and posterior 
    
    Args:
      x (numpy array of floats):         points at which the likelihood has been evaluated
      auditory (numpy array of floats):  normalized probabilities for auditory likelihood evaluated at each `x`
      visual (numpy array of floats):    normalized probabilities for visual likelihood evaluated at each `x`
      posterior (numpy array of floats): normalized probabilities for the posterior evaluated at each `x`
             
    Returns:
      Nothing.
    """
    if auditory is None:
        auditory = np.zeros_like(x)

    if visual is None:
        visual = np.zeros_like(x)

    if posterior_pointwise is None:
        posterior_pointwise = np.zeros_like(x)

    plt.plot(x, auditory, '-r', LineWidth=2, label='Auditory')
    plt.plot(x, visual, '-b', LineWidth=2, label='Visual')
    plt.plot(x, posterior_pointwise, '-g', LineWidth=2, label='Posterior')
    plt.legend()
    plt.ylabel('Probability')
    plt.xlabel('Orientation (Degrees)')


def plot_visual(mu_visuals, mu_posteriors, max_posteriors):
  """
  Plots the comparison of computing the mean of the posterior analytically and
  the max of the posterior empirically via multiplication.
  
  Args:
    mu_visuals (numpy array of floats): means of the visual likelihood
    mu_posteriors (numpy array of floats):  means of the posterior, calculated analytically
    max_posteriors (numpy array of floats): max of the posteriors, calculated via maxing the max_posteriors.
    posterior (numpy array of floats): normalized probabilities for the posterior evaluated at each `x`
    
  Returns:
    Nothing.
  """
  fig = plt.figure(figsize=(fig_w, 2*fig_h))

  plt.subplot(211)
  plt.plot(mu_visuals, max_posteriors,'-g', label='argmax')
  plt.xlabel('Visual stimulus position')
  plt.ylabel('Multiplied max of position')
  plt.title('Sample output')
  plt.subplot(212)
  plt.plot(mu_visuals, mu_posteriors, '--', color='xkcd:gray', label='argmax')
  plt.xlabel('Visual stimulus position')
  plt.ylabel('Analytical posterior mean')
  plt.tight_layout()
  plt.title('Hurray for math!')
  plt.show()
