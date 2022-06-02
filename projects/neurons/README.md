# Guide to choosing a Neurons dataset

*July 5-23, 2021*

## Steinmetz

The Steinmetz dataset ([youtube](https://www.youtube.com/watch?v=WXn4-FpVaOo)) contains 39 Neuropixels recordings of 400-700 neurons each from across the mouse brain during a visual behavior task. This dataset was used by the most groups last year, as it is great for exploratory analyses and is relatively well supported with code and many included experimental and behavioral variables. You should still try to ask specific questions, i.e.: "does the superior colliculus offer a parallel or complementary visual processing pathway to visual cortex?"

Credit for data curation: Marius Pachitariu, Scott Linderman

|   | Run | View |
| - | --- | ---- |
| Main notebook | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_steinmetz_decisions.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_steinmetz_decisions.ipynb?flush_cache=true) |
| LFP and waveform notebook | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_steinmetz_extra.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_steinmetz_extra.ipynb?flush_cache=true) |

### References:

- Steinmetz, N. A., Zatka-Haas, P., Carandini, M., and Harris, K. D. (2019). Distributed coding of choice, action and engagement across the mouse brain. Nature, 576(7786): 266-273. doi: [10.1038/s41586-019-1787-x](https://doi.org/10.1038/s41586-019-1787-x)

- url: [neurostars.org/t/steinmetz-et-al-2019-dataset-questions/14539/72](https://neurostars.org/t/steinmetz-et-al-2019-dataset-questions/14539/72)

## Stringer

The Stringer datasets ([youtube](https://www.youtube.com/watch?v=78GSgf6Dkkk)) contain simultaneous recordings of 10,000 or 20,000 neurons from mouse visual cortex either during the presentation of gratings or during spontaneous behaviors like running, whisking and sniffing. These datasets are a little more advanced because you have to work with many neurons simultaneously. They are exciting, because they give a taste of what's to come in neuroscience.

Credit for data curation: Marius Pachitariu

|   | Run | View |
| - | --- | ---- |
| Orientation stimuli + running | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_stringer_orientations.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_stringer_orientations.ipynb?flush_cache=true) |
| High-dimensional spontaneous behaviors | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_stringer_spontaneous.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_stringer_spontaneous.ipynb?flush_cache=true) |

### References:

- Stringer, C., Pachitariu, M., Steinmetz, N., Reddy, C. B., Carandini, M., and Harris, K. D. (2019). Spontaneous behaviors drive multidimensional, brainwide activity. Science, 364(6437): eaav7893. doi: [10.1126/science.aav7893](https://doi.org/10.1126/science.aav7893)

- Stringer, C., Michaelos, M., Tsyboulski, D., Lindo, S. E., and Pachitariu, M. (2021). High-precision coding in visual cortex. Cell, 184(10): 2767-2778. doi: [10.1016/j.cell.2021.03.042](https://doi.org/10.1016/j.cell.2021.03.042)

## Allen Institute

The Allen Institute dataset ([youtube](https://www.youtube.com/watch?v=3YP-GYvYnuA)) is new this year, and it was designed to be very friendly for beginners. The mice do a visual adaptation task using either familiar or novel images. The recordings are from specific neuron populations (VIP, SST etc) in multiple visual cortical brain areas. This dataset is well supported with code and a dedicated project template. This would provide a more focused experience for beginner groups than the Steinmetz dataset, with the caveat that the data is unpublished so it is harder to find supporting information for it. For more advanced groups, a separate dataloader is available using the Allen Institute SDK, which gives access to the entire dataset for more exploratory analyses.

Credit for data curation: Marina Garret, Iryna Yavorska, Doug Ollerenshaw

|   | Run | View |
| - | --- | ---- |
| Analyze one dataset | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_pre_processed_file.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_pre_processed_file.ipynb?flush_cache=true) |
| Access to all data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_SDK.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_SDK.ipynb?flush_cache=true) |

### References: none yet for this dataset, but see:

- de Vries, S. E., Lecoq, J. A., Buice, M. A., Groblewski, P. A., Ocker, G. K., Oliver, M., ... and Koch, C. (2020). A large-scale standardized physiological survey reveals functional organization of the mouse visual cortex. Nature neuroscience, 23(1): 138-151. doi: [10.1038/s41593-019-0550-9](https://doi.org/10.1038/s41593-019-0550-9)

- Siegle, J. H., Jia, X., Durand, S., Gale, S., Bennett, C., Graddis, N., ... and Koch, C. (2021). Survey of spiking in the mouse visual system reveals functional hierarchy. Nature, 592(7852): 86-92. doi: [10.1038/s41586-020-03171-x](https://doi.org/10.1038/s41586-020-03171-x)
