
# Guide to choosing an FMRI dataset

*July 5-23, 2021*

### HCP task datasets

The HCP task datasets ([youtube-2021](https://youtube.com/watch?v=nssSiCmbjxw), [youtube-2020](https://youtube.com/watch?v=iOCcY0QFMS4)) are a great overall choice, because many of the behaviors are interesting (gambling, emotion, language, social, working memory etc), and the data is already preprocessed and averaged across voxels to make brain regions. This dataset is appropriate for all levels.  

Credit for data curation: John Murray, Saad Jbabdi

|   | Run | View |
| - | --- | ---- |
| HCP 2021 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_hcp_task.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_hcp_task.ipynb?flush_cache=true) |
| HCP 2020 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_hcp.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_hcp.ipynb?flush_cache=true) |

### FSL course task

The FSL course task dataset ([youtube](https://youtube.com/watch?v=ZI-xFYubENw)) complements the HCP one, with two additional language tasks. These data are brainwide and at the voxel level.

Credit for data curation: Saad Jbabdi

|   | Run | View |
| - | --- | ---- |
| FSL course task | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_fslcourse.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_fslcourse.ipynb?flush_cache=true) |

### HCP retinotopy

HCP retinotopy ([youtube](https://youtube.com/watch?v=nssSiCmbjxw)) is a specific kind of project that can be used to do population receptive field modelling. This might be interesting to ML-savy groups because it doesn’t require a lot of neuroscience or FMRI background, and one can visualize the hierarchy of brain areas and their responses.

Credit for data curation: Saad Jbabdi

|   | Run | View |
| - | --- | ---- |
| HCP retinotopy | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_hcp_retino.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_hcp_retino.ipynb?flush_cache=true) |

### Kay natural images

Credit for data curation: Michael Waskom, Marius Pachitariu

The Kay dataset ([youtube](https://youtube.com/watch?v=LdJkLyw4yzg)) of visual responses to natural images is intermediate, as it has many voxels in V1/V2/V3/V4 and many images annotated with object label information.

|   | Run | View |
| - | --- | ---- |
| Kay natural images | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_kay_images.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_kay_images.ipynb?flush_cache=true) |

### Bonner/Algonauts/Cichy

Bonner ([youtube](https://youtube.com/watch?v=7NggvUlobQQ)) / Cichy ([youtube](https://youtube.com/watch?v=I3_nA_6mq1g)) / Algonauts ([youtube](https://youtube.com/watch?v=TID48cMcneo)) are the most advanced datasets which can be used to do representational (di)similarity analyses on visual response data (static images, videos, or navigation-related images). Specifically designed to go with the two project templates comparing FMRI responses to deep neural networks.

Credit for data curation: Kshitij Dwivedi

|   | Run | View |
| - | --- | ---- |
| Bonner navigation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_bonner_navigational_affordances.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_bonner_navigational_affordances.ipynb?flush_cache=true) |
| Cichy objects/animals | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_cichy_fMRI_MEG.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_cichy_fMRI_MEG.ipynb?flush_cache=true) |
| Algonauts video clips | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_algonauts_videos.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/NeuromatchAcademy/course-content/blob/master/projects/fMRI/load_algonauts_videos.ipynb?flush_cache=true) |
