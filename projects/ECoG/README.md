# Guide to choosing an EEG/ECoG/LFP dataset

*July 5-23, 2021*

New in 2021, we have ECoG datasets ([youtube](https://youtube.com/watch?v=rAqtrBhwS80)) from Kai Miller! This is a rare dataset from intracranial electrocorticographic recordings in clinical settings. Please watch Kai Miller's TED talk to familiarize yourself with this type of recording.

* The datasets are more or less at the same difficulty level. All datasets are from the same research group, using the same recording methods and standardized protocols.

* Students can choose one dataset based on their particular interest (sensory / motor / memory / BCI).

* For slightly more advanced groups, you should definitely consider the LFPs from the Steinmetz dataset, which are much better suited for exploratory analyses and a wide diversity topics. They are also better for computational projects, because they provide high-dimensional data (lots of neurons) with lots of trials, and they are well supported at NMA, because the Steinmetz dataset has been well curated and annotated in general.  

Credit for data curation: Marius Pachitariu and the project TAs

|   | Run | View |
| - | --- | ---- |
| FacesHouses | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_faceshouses.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_faceshouses.ipynb?flush_cache=true) |
| FingerFlex | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_fingerflex.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_fingerflex.ipynb?flush_cache=true) |
| JoystickTrack | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_joystick_track.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_joystick_track.ipynb?flush_cache=true) |
| MemoryNback | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_memory_nback.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_memory_nback.ipynb?flush_cache=true) |
| MotorImagery | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_motor_imagery.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_motor_imagery.ipynb?flush_cache=true) |


## References:

### Faces/Houses:

- Miller, K. J., Hermes, D., Pestilli, F., Wig, G. S., and Ojemann, J. G. (2017). Face percept formation in human ventral temporal cortex. Journal of neurophysiology 118(5): 2614-2627. doi: [10.1152/jn.00113.2017](https://doi.org/10.1152/jn.00113.2017)

- Miller, K. J., Hermes, D., Witthoft, N., Rao, R. P., and Ojemann, J. G. (2015). The physiology of perception in human temporal lobe is specialized for contextual novelty. Journal of neurophysiology 114(1): 256-263. doi: [10.1152%2Fjn.00131.2015](https://doi.org/10.1152%2Fjn.00131.2015)

- Miller, K. J., Schalk, G., Hermes, D., Ojemann, J. G., and Rao, R. P. (2016). Spontaneous decoding of the timing and content of human object perception from cortical surface recordings reveals complementary information in the event-related potential and broadband spectral change. PLoS computational biology 12(1): e1004660. doi: [10.1371/journal.pcbi.1004660](https://doi.org/10.1371/journal.pcbi.1004660)

### Fingerflex:

- Miller, K. J., Zanos, S., Fetz, E. E., Den Nijs, M., & Ojemann, J. G. (2009). Decoupling the cortical power spectrum reveals real-time representation of individual finger movements in humans. Journal of Neuroscience 29(10): 3132-3137. doi: [10.1523%2FJNEUROSCI.5506-08.2009](https://doi.org/10.1523%2FJNEUROSCI.5506-08.2009)

- Miller, K. J., Hermes, D., Honey, C. J., Hebb, A. O., Ramsey, N. F., Knight, R. T., ... and Fetz, E. E. (2012). Human motor cortical activity is selectively phase-entrained on underlying rhythms. PLoS computational biology: e1002655. doi: [10.1371/journal.pcbi.1002655](https://doi.org/10.1371/journal.pcbi.1002655)

### Joystick track:

- Schalk, G., Kubanek, J., Miller, K. J., Anderson, N. R., Leuthardt, E. C., Ojemann, J. G., ... and Wolpaw, J. R. (2007). Decoding two-dimensional movement trajectories using electrocorticographic signals in humans. Journal of neural engineering 4(3): 264-275. doi: [0.1088/1741-2560/4/3/012](https://doi.org/10.1088/1741-2560/4/3/012)

- Schalk, G., Miller, K. J., Anderson, N. R., Wilson, J. A., Smyth, M. D., Ojemann, J. G., ... and Leuthardt, E. C. (2008). Two-dimensional movement control using electrocorticographic signals in humans. Journal of neural engineering 5(1): 75-84. doi: [10.1088/1741-2560/5/1/008](https://doi.org/10.1088/1741-2560/5/1/008)

### Memory nback (no direct references but see)

- Brouwer, A. M., Hogervorst, M. A., Van Erp, J. B., Heffelaar, T., Zimmerman, P. H., and Oostenveld, R. (2012). Estimating workload using EEG spectral power and ERPs in the n-back task. Journal of neural engineering 9(4): 045008. doi: [10.1088/1741-2560/9/4/045008](https://doi.org/10.1088/1741-2560/9/4/045008)

- Grissmann, S., Faller, J., Scharinger, C., Spüler, M., and Gerjets, P. (2017). Electroencephalography based analysis of working memory load and affective valence in an n-back task with emotional stimuli. Frontiers in human neuroscience 11: 616. doi: [10.3389%2Ffnhum.2017.00616](https://doi.org/10.3389%2Ffnhum.2017.00616)

### Motor imagery:

- Miller, K. J., Schalk, G., Fetz, E. E., Den Nijs, M., Ojemann, J. G., and Rao, R. P. (2010). Cortical activity during motor execution, motor imagery, and imagery-based online feedback. Proceedings of the National Academy of Sciences 107(9):4430-4435. doi: [10.1073/pnas.0913697107](https://doi.org/10.1073/pnas.0913697107)
