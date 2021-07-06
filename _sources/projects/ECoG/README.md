# Guide to choosing an EEG/ECoG/LFP dataset

*July 5-23, 2021*

New in 2021, we have ECoG datasets ([youtube](https://youtube.com/watch?v=rAqtrBhwS80)) from Kai Miller! This is a rare dataset from intracranial electrocorticographic recordings in clinical settings. Please watch Kai Miller's TED talk to familiarize yourself with this type of recording.

* The datasets are more or less at the same difficulty level. All datasets are from the same research group, using the same recording methods and standardized protocols.

* Students can choose one dataset based on their particular interest (sensory / motor / memory / BCI).

* For slightly more advanced groups, you should definitely consider the LFPs from the Steinmetz dataset, which are much better suited for exploratory analyses and a wide diversity topics. They are also better for computational projects, because they provide high-dimensional data (lots of neurons) with lots of trials, and they are well supported at NMA, because the Steinmetz dataset has been well curated and annotated in general.  

Credit for data curation: Marius Pachitariu and the project TAs

|   | Run | View |
| - | --- | ---- |
| FacesHouses | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_faceshouses.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_faceshouses.ipynb?flush_cache=true) |
| FingerFlex | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_fingerflex.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_fingerflex.ipynb?flush_cache=true) |
| JoystickTrack | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_joystick_track.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_joystick_track.ipynb?flush_cache=true) |
| MemoryNback | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_memory_nback.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_memory_nback.ipynb?flush_cache=true) |
| MotorImagery | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_motor_imagery.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/ECoG/load_ECoG_motor_imagery.ipynb?flush_cache=true) |


References:

faces/houses:

Miller, Kai J., et al. "Face percept formation in human ventral temporal cortex." Journal of neurophysiology 118.5 (2017): 2614-2627.

Miller, Kai J., et al. "The physiology of perception in human temporal lobe is specialized for contextual novelty." Journal of neurophysiology 114.1 (2015): 256-263.

Miller, Kai J., et al. "Spontaneous decoding of the timing and content of human object perception from cortical surface recordings reveals complementary information in the event-related potential and broadband spectral change." PLoS computational biology 12.1 (2016): e1004660.

fingerflex:

Miller, Kai J., et al. "Decoupling the cortical power spectrum reveals real-time representation of individual finger movements in humans." Journal of Neuroscience 29.10 (2009): 3132-3137.

Miller, Kai J., et al. "Human motor cortical activity is selectively phase-entrained on underlying rhythms." (2012): e1002655.

joystick track:

Schalk, G., et al. "Decoding two-dimensional movement trajectories using electrocorticographic signals in humans." Journal of neural engineering 4.3 (2007): 264.

Schalk, Gerwin, et al. "Two-dimensional movement control using electrocorticographic signals in humans." Journal of neural engineering 5.1 (2008): 75.

memory nback: no direct references but see

Brouwer, Anne-Marie, et al. "Estimating workload using EEG spectral power and ERPs in the n-back task." Journal of neural engineering 9.4 (2012): 045008.

Grissmann, Sebastian, et al. "Electroencephalography based analysis of working memory load and affective valence in an n-back task with emotional stimuli." Frontiers in human neuroscience 11 (2017): 616.

 motor imagery:

 Miller, Kai J., Gerwin Schalk, Eberhard E. Fetz, Marcel Den Nijs, Jeffrey G. Ojemann, and Rajesh PN Rao. "Cortical activity during motor execution, motor imagery, and imagery-based online feedback." Proceedings of the National Academy of Sciences (2010): 200913697.
