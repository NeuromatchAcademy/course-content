# Guide to choosing a Neurons dataset

*July 5-23, 2021*

### Steinmetz

The Steinmetz dataset ([youtube](https://www.youtube.com/watch?v=WXn4-FpVaOo)) contains 39 Neuropixels recordings of 400-700 neurons each from across the mouse brain during a visual behavior task. This dataset was used by the most groups last year, as it is great for exploratory analyses and is relatively well supported with code and many included experimental and behavioral variables. You should still try to ask specific questions, i.e.: "does the superior colliculus offer a parallel or complementary visual processing pathway to visual cortex?"

Credit for data curation: Marius Pachitariu, Scott Linderman

|   | Run | View |
| - | --- | ---- |
| Main notebook | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_steinmetz_decisions.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_steinmetz_decisions.ipynb?flush_cache=true) |
| LFP and waveform notebook | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_steinmetz_extra.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_steinmetz_extra.ipynb?flush_cache=true) |

References:

Steinmetz, Nicholas A., et al. "Distributed coding of choice, action and engagement across the mouse brain." Nature 576.7786 (2019): 266-273.

https://neurostars.org/t/steinmetz-et-al-2019-dataset-questions/14539/72

### Stringer

The Stringer datasets ([youtube](https://www.youtube.com/watch?v=78GSgf6Dkkk)) contain simultaneous recordings of 10,000 or 20,000 neurons from mouse visual cortex either during the presentation of gratings or during spontaneous behaviors like running, whisking and sniffing. These datasets are a little more advanced because you have to work with many neurons simultaneously. They are exciting, because they give a taste of what's to come in neuroscience.

Credit for data curation: Marius Pachitariu

|   | Run | View |
| - | --- | ---- |
| Orientation stimuli + running | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_stringer_orientations.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_stringer_orientations.ipynb?flush_cache=true) |
| High-dimensional spontaneous behaviors | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_stringer_spontaneous.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_stringer_spontaneous.ipynb?flush_cache=true) |

References:

Stringer, Carsen, et al. "Spontaneous behaviors drive multidimensional, brainwide activity." Science 364.6437 (2019).

Stringer, Carsen, et al. "High-precision coding in visual cortex." Cell 184.10 (2021): 2767-2778.

### Allen Institute

The Allen Institute dataset ([youtube](https://www.youtube.com/watch?v=3YP-GYvYnuA)) is new this year, and it was designed to be very friendly for beginners. The mice do a visual adaptation task using either familiar or novel images. The recordings are from specific neuron populations (VIP, SST etc) in multiple visual cortical brain areas. This dataset is well supported with code and a dedicated project template. This would provide a more focused experience for beginner groups than the Steinmetz dataset, with the caveat that the data is unpublished so it is harder to find supporting information for it. For more advanced groups, a separate dataloader is available using the Allen Institute SDK, which gives access to the entire dataset for more exploratory analyses.

Credit for data curation: Marina Garret, Iryna Yavorska, Doug Ollerenshaw

|   | Run | View |
| - | --- | ---- |
| Analyze one dataset | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_Allen_Visual_Behavior_from_pre_processed_file.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_Allen_Visual_Behavior_from_pre_processed_file.ipynb?flush_cache=true) |
| Access to all data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_Allen_Visual_Behavior_from_SDK.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/neurons/load_Allen_Visual_Behavior_from_SDK.ipynb?flush_cache=true) |

References: none yet for this dataset, but see:

de Vries, Saskia EJ, et al. "A large-scale standardized physiological survey reveals functional organization of the mouse visual cortex." Nature Neuroscience 23.1 (2020): 138-151.

Siegle, Joshua H., et al. "Survey of spiking in the mouse visual system reveals functional hierarchy." Nature 592.7852 (2021): 86-92.
