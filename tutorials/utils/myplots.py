#!/usr/bin/env python
# coding: utf-8

import time                        # import time 
import numpy as np                 # import numpy
import scipy as sp                 # import scipy
import math                        # import basic math functions
import random                      # import basic random number generator functions

import matplotlib.pyplot as plt    # import matplotlib
from IPython import display        


def my_plot(x, auditory=None, visual=None, posterior_pointwise=None):
    """
    Plots normalized Gaussian distributions and posterior 

    DO NOT EDIT THIS FUNCTION !!!
    
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


def my_dynamic_plot(x, auditory, visual, posterior_pointwise):
    """
    DO NOT EDIT THIS FUNCTION !!!

    Plots the auditory, visual and posterior distributions and update the figure every .2 seconds
    
    Args: 
      x (numpy array of floats):         points at which the likelihood has been evaluated
      auditory (numpy array of floats):  normalized probabilities for auditory likelihood evaluated at each `x`
      visual (numpy array of floats):    normalized probabilities for visual likelihood evaluated at each `x`
      posterior (numpy array of floats): normalized probabilities for the posterior evaluated at each `x`
             
    Returns:
      Nothing
    """
    
    plt.clf()
    plt.plot(x, auditory, '-r', LineWidth=2, label='Auditory')
    plt.plot(x, visual, '-b', LineWidth=2, label='Visual')
    plt.plot(x, posterior_pointwise, '-g', LineWidth=2, label='Posterior')
    plt.ylabel('Probability')
    plt.xlabel('Orientation (Degrees)')
    plt.legend()
    display.clear_output(wait=True)
    display.display(plt.gcf())
    time.sleep(0.2)
