# Guide to choosing a Neurons dataset

Scroll down for project templates associated to these datasets. 

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

The Allen Institute dataset ([youtube](https://www.youtube.com/watch?v=3YP-GYvYnuA)) is new this year, and it was designed to be very friendly for beginners. The mice do a visual change detection task using either familiar or novel images. The recordings are from specific neuron populations (Excitatory, VIP, and SST) in multiple visual cortical brain areas (V1 and LM). This dataset is well supported with code and a dedicated project template. This would provide a more focused experience for beginner groups than the Steinmetz dataset. For more advanced groups, a separate dataloader is available using the Allen Institute SDK, which gives access to the entire dataset for more exploratory analyses. You can learn more about the dataset and find additional description and helpful tools on [Allen Brain Atlas](https://allensdk.readthedocs.io/en/latest/visual_behavior_optical_physiology.html) and [SWDB databook](https://allenswdb.github.io/physiology/ophys/visual-behavior/VB-Ophys.html).

Credit for data curation: Marina Garret, Iryna Yavorska, Doug Ollerenshaw

|   | Run | View |
| - | --- | ---- |
| Analyze one dataset | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_pre_processed_file.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_pre_processed_file.ipynb?flush_cache=true) |
| Access to all data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_SDK.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_SDK.ipynb?flush_cache=true) |

### You can read more about scientific discoveries related to this dataset in our preprint:

- Garrett, M. et. al. (2023) Stimulus novelty uncovers coding diversity in visual cortical circuits. bioRxiv doi: [https://www.biorxiv.org/content/10.1101/2023.02.14.528085v2]


## International Brain Laboratory

The International Brain Laboratory (IBL) brain-wide map dataset ([YouTube tutorial – TODO link]) includes data from 699 Neuropixels probe insertions across 281 brain regions, recorded during a standardized visual decision-making task. To help users get started, a dedicated project and step-by-step tutorial are available. For more advanced users, the IBL ONE tutorial demonstrates how to access the full range of IBL data using the Open Neurophysiology Environment (ONE) API, enabling deeper exploration and custom analyses across the entire dataset.

Credit for data curation: Mayo Faulkner

|                       | Run | View |
|-----------------------| --- | ---- |
| Analyze prepared data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WEhmZF4hnxkuGCcqJn1tl5oGFgO85Qai) | 
| IBL ONE tutorial      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1y3sRI1wC7qbWqN6skvulzPOp6xw8tLm7) | 

### References

- International Brain Laboratory et al. (2023) A Brain-Wide Map of Neural Activity during Complex Behaviour doi: [10.1101/2023.07.04.547681]([https://doi.org/10.1101/2023.07.04.547681])
- Findling et al. (2023) Brain-wide representations of prior information in mouse decision-making doi: [10.1101/2023.07.04.547684](https://doi.org/10.1101/2023.07.04.547684)


# Project Templates

Click on each image below to see a full browser version!

## Effect of stimulus context and behavior state on visual representations

<img src="template_images/StimulusContextBehaviorState.svg" width="100%">

## Behavior representations in mouse visual cortex

<img src="template_images/MouseOrofacialBehaviors.svg" width="100%">

## Brain-wide map of neural activity during complex behaviour

<img src="template_images/BrainwideMapIBL.svg" width="100%">