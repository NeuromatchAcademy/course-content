  # Daily guide for projects

## Summary

This project plan explicitly encourages the iterative nature of research as a series of questions and answers that gradually refine your hypotheses. We have assigned you to pods based on your broad interests (neurons, fMRI, ECoG, theory and behavior). Each pod will split into two groups, with the goal of making well-balanced groups. There is more guidance below.

Once you're in groups, you will start brainstorming and searching the literature for interesting papers, with the goal of forming a project question. For the rest of week 1 you will try preliminary analyses of the datasets with the goal of refining and informing your question. Week 2 day 1 (W2D1) is dedicated to projects and will teach you a general strategy for approaching projects (the "10 steps"). You will apply this strategy to your own question. 

For the rest of the second week you will continue to analyze data / refine your question, with the goal of writing an abstract on W2D5, which is another project day. Your abstract may or may not include results, but it should at least include a testable hypothesis. You'll swap abstracts with another group on W2D5. For the rest of the course, you will focus on getting evidence for/against your hypothesis.

Finally, in W3D5 you will meet with other groups in your pod and megapod (organized by the lead TAs), and tell them the story of your project. This is a low-key presentation that may include some of the plots you made along the way, but it is not meant as a real research presentation with high “production values”. See some of the [examples](https://compneuro.neuromatch.io/projects/docs/project_2020_highlights.html)  to get a sense of what the presentation will look like.


## Submission Links

- W2D5 Abstract Submission [Airtable Link](https://airtable.com/shr0ozNAhXq6K1p8o)
- W3D5 Project Submission [Airtable Link](https://airtable.com/shrvoz2N9UulAVqqU)

## Project templates

[Project templates](https://compneuro.neuromatch.io/projects/docs/project_templates.html) are research ideas developed by the NMA team that can be used in conjunction with the datasets we provided. Project templates can be used in a variety of ways.
* For starters, you can use the project templates just to get familiarized with some of our datasets or one of the provided models. They can provide keywords for you to use in a literature search, or python libraries you can reuse to answer your own questions.
* You should use the project templates extensively if you are new to neuroscience and/or you don’t have a lot of research experience. They have been designed to give you enough structure to get started, and enough options to keep you going if you stick with the template. Or you may start with a template, use it the first week and then in the second week diverge from it as your group develops their own new idea or question to test.
* Templates have a natural flow of questions, but don’t hesitate to skip or completely change some of these. They are meant to be used very flexibly!

## Project TAs

Project TAs are your friendly dataset experts to consult with on all issues related to datasets. They can also help with other aspects of a project, including brainstorming, literature searches and coding. You will have meetings with them approximately every two days. During this time, they will help you refine your question and hypothesis into something that can be answered with our datasets. Since they can arrive unannounced at any time (busy schedules!), please stop what you were doing to have the meeting, and then resume your work when the project TA leaves.

For the assigned meetings, project TAs will generally come only during project times, but sometimes they might need to schedule meetings slightly earlier or later. We encourage you to reach out to them for extra meetings whenever you need them, and to post questions on discord in the #dataset-X channels. 

##  Week 1: Getting started

Depending on your time slot, you may or may not have project time on the first day of the course. Regardless of whether your first project meeting is day 1 or day 2, spend your first session doing the following:

* Split into groups. We recommend intentionally creating groups with diverse skillsets. Groups should have students who are very confident in Python and those who are just learning. Through the project, students can work together to strengthen eachother's skills. We want to make sure that all members of each group get a chance to do all parts of the project. We ask that folks who are good with Python share what they know and handoff tasks to peers who are learning so they can improve their skills. 
* Introductions (30 min = 2 min/student): say a few things about yourself, then about your research area or research interests. What are you really curious about, that you might explore in your NMA project?
* Listen carefully as others talk about their interests.
* Individual reading time (30 min): browse the projects booklet which includes this guide (skim the entire thing) + project templates with slides and code + dataset videos + docs with further ideas and datasets
* Now brainstorm within your group (60 min). Definitely choose a topic and start thinking about concrete questions if you can. Make sure the topic you choose is well suited for answering the broad range of questions you are interested in. Try to come up with one or a few topics of interest, either by yourselves or directly from the booklet (i.e. project templates).

Tips:
* No need to have a very concrete project after this day. You will determine the feasibility of your questions in the next few days, and you will likely change your question completely. That’s how research works!
* The exploratory work you do in week 1 will culminate in a project proposal on the first project day (peek ahead in this guide at W2D1).


### W1D2
Continue brainstorming! Try to come up with one or a few topics of interest, either by yourselves or directly from the project templates. Get your hands dirty by running some of the notebooks provided for your dataset. There should be a loading notebook, and there should be some further analysis notebooks interspersed among the project templates. Even if you are not using a project template, they are likely to contain useful code to get you started, especially if you are doing a theory project. If all you do is run the provided notebooks that’s fine! Try to understand what is being plotted and how. Pay attention to the code libraries being used, and the way the data is accessed / binned / aligned. You will reuse some of these code elements to start doing your own analyses in later days.

### W1D3-W1D5
Be on the lookout for interesting hypotheses. You might notice something unexpected in the data, and if you dig deeper it might lead you directly to a result. For this to work, you must keep an open mind about what your questions are. Here are some generally useful tips & tricks:

* The hardest part will be the technical challenge of wrestling with the data to try to answer your question. You can rely on your TA, the dedicated project TA and the Discord channels to make this process easier.
* For theory projects, wrestling with your model can be equally challenging. If your model generates data, for example a neural network simulation, then you can still use some of the tricks below to analyze that data.
* If your model makes a hypothesis that needs to be tested, then your theory project might become a data project. The opposite may also happen if you find something interesting in the data, and you realize that you need a model to understand it better.  
* Always be on the lookout for bugs in your code, or ”bugs” in your analysis plan. If a result looks too good to be true, it might be! Make sure you always split your data train/test, even for simple analyses where you think it might not matter (i.e. for making tuning curves).
* If your question does change, remember to always do a quick literature survey (i.e. google search) to see if others thought about your question in the past. You don’t need to come up with a completely original question! Do however situate your research within the relevant literature, and try to get hints/suggestions from other papers.
* Depending how complex your question is, there could be several data analysis steps:
   * data wrangling: some questions can be answered simply by plotting the right variable! Some generally useful strategies: make PSTHs and tuning curves; try scatter plots of different variables; plot across neurons or across trials; select the most tuned neurons and look just at those; if there are multiple sessions pick a one of a high quality (more neurons or more trials) and dig deep into that one.
   * simple, linear analyses: most questions can be answered at this stage. This is often needed if you are doing a “population analysis”, i.e. trying to determine if a set of neurons or voxels collectively encode a certain variable. By far, the most used linear analyses are linear regression, PCA and k-means clustering.
   * Linear regression is often a good first step, even if your variables are binary/categorical. Once you have a pipeline, it will be easy to switch to logistic regression or other predictors from the scikit-learn library.
   * For visualizations, you might want to reduce a population of neurons to just a few components using PCA, then go back to the “data wrangling” steps and make the same kinds of plots for PCs that you made for neurons.
   * Another way to reduce the size of data is to cluster neurons into a few clusters, then average within that cluster. The simplest clustering model is k-means.
* More complicated, nonlinear analyses: if the simple analyses fail, you might think you have no choice but to try something fancy, like deep learning or tSNE. This is often a dead end where projects go to die! You probably will make a lot more progress by slightly (or greatly) changing your question, or by refining your hypothesis. The reason complicated analysis are so hard to do and interpret is that they often function as black boxes that are hard to look into. What do the parameters of a deep neural network mean? That is a hard research question in its own right. If you must, however, use complicated analyses, then here's some quick tips:
   * deep learning “replaces” linear regression, t-SNE / UMAP replaces PCA, and Leiden/Louvain replaces k-means.
   * Deep learning can be used as an encoder/decoder tool. This is generally unlikely to do better than linear/logistic regression, because neural data is noisy, and you need a lot of training data to really train a deep network well. This is because deep networks have a lot of parameters.
   * There are many “nonlinear dimensionality reduction” methods like t-SNE / UMAP, but these are often not meant as replacements for PCA, but instead as visualization tools to try to see a clustering structure in your data. They can be useful for making hypotheses based on interesting-looking plots. You still need to validate those hypotheses using simpler methods, like clustering and PCA.
   * There are many complex clustering models like the Leiden/Louvain algorithms, hdbscan and spectral clustering, but those tend to be unstable for high-dimensional data and difficult to interpret. You will have to carefully try different parameters, and think through what the clusters mean.
   * You can still use nonlinear models very well as a *hypothesis* about what the brain is doing. For example, neural networks configured and trained in specific ways can resemble neural activity in the brain. 


## W2 Project time

Week 2 is when projects really start to ramp up.

### W2D1: Project Half Day
We have designed tutorials to help launch your projects. Once you're done with them, you will complete your literature review and work on your project proposal.

(2h) Complete the intro/tutorial/outro for this day
* You will need to use your group's project for some of this content. If you don’t have concrete ideas yet, or you haven’t done a research project before, use one of the provided project templates to walk through the four steps.
* If you are using a project template, your goal is to translate the information from the slide and colab notebook into a 4-step format. Some information might not be readily available in the slide or notebook, and you might have to find it in your literature review later this day.
* Try to write down a few sentences for each of the four steps applied to your project. You will re-use these in your proposal later today.  

(2.5h) Literature review: identify interesting papers
The goal of this literature review is to situate your question in context and help you acquire some keywords that you will use in your proposal today.
* (30min) on your own, start doing a literature review using google searches and only look at abstracts to select 2-3 promising ones.  
* (10min) report to the whole group what papers you found and pool them together. Assign one paper per person to read/skim in the next 1h.  
* (1h) on your own, read the paper that was assigned to you. Make notes in a common google doc shared with your group, and especially write down important keywords or concepts which you might use in your proposal later today. If you are not connected to an .edu domain or a VPN, try to find full versions of papers on preprint servers like arXiv / bioRxiv. You could also ask your TA to get it for you (and they might in turn ask someone who has access to a university VPN). There might be other options too.  
* (1h) report back to the group, and try to tell them as much as you understood about the paper. Get into details, but don’t just read to them whole sections from the paper. Ask the other students questions about the papers they are presenting to understand them better.

Project block task:
(3h) Project proposal
* Try to write a proposal for this project based on the way you understand it now. This should re-use some of the text you wrote down for the four steps, and should include keywords and concepts that you identified in your literature review. Don’t worry too much about the structure of this paragraph! The goal is to get as many words (200-300) on paper as possible. You have the entire day 10 to learn how to write a properly structured scientific abstract.
* It is important to include the concepts which you identified as relevant, and the keywords that go with them.
* When you are ready, please submit your proposal [here](https://airtable.com/shrcYuFYMPh4jGIng). This is not mandatory and can be submitted at any time. We won't evaluate this, but we will use it to keep track of the overall progress of the groups. 

###  W2D2

You should now have a sense of the data, and you have probably refined your hypothesis a little. You might have a vague idea of what it would take for your project to work, what tools you might use, and what the answer could look like. Let’s make these things explicit, by continuing with steps 6-9 of the modeling practice in this [steps 5-10 notebook](https://compneuro.neuromatch.io/projects/modelingsteps/ModelingSteps_5through10.html).

* (1-2h) Go through steps 6-10 for your project and watch the videos.

### W2D5: Abstract Writing Day!

One of the best ways to understand your own research is to try to write about it. You should write early and often, not just at the end when you’re trying to write a paper or your thesis. Science conferences are a great way to present your intermediate work, and they give you a chance to write an abstract. For example, the Neuromatch Conferences are a great venue for this. However, you don’t have to wait so long to write your project abstract, you’ll do it today! If you have preliminary results that’s great, but it’s not required. Most of the components of an abstract do not in fact require results. The goal for this day is to workshop your abstract with your group, and then present this to your entire pod. You can also think of it as a much more refined version of the project proposal you submitted originally.

If you have been using a project template, this is a good time to branch out and pursue your own questions. The template was only meant to get you started on some concrete analyses, so that you become familiar with the data, but now that you have more knowledge, you should be able to come up with your own question. Practice the 4-steps again if necessary, they should be easier once you have a good question.

If you think your abstract is lacking the computational "oomph" to make it sound good, check out the "W2D5 (bonus)" section below. Take the time to find interesting modeling or computational facets to your project, because this will make the abstract writing easier and more enjoyable since you can talk about big, interesting ideas and then gradually focus on the very specific work that you've done.  

Your starting point for workshopping your abstract should be step 10 from the [Modeling steps 5-10](https://compneuro.neuromatch.io/projects/modelingsteps/ModelingSteps_5through10.html) notebook, and especially the example projects ([model project](https://compneuro.neuromatch.io/projects/modelingsteps/TrainIllusionModel.html) and [data project](https://compneuro.neuromatch.io/projects/modelingsteps/TrainIllusionDataProject.html)) which show how you can build an abstract if you have been following the 10 steps.

Note: the timings for this day are just suggestions. You can spend more or less time on different parts depending on how much work you think your abstract needs. Also, take as much time as you need in the beginning of this day to carefully go through the modeling steps notebooks (including the example projects) and/or to explore/think about the big picture topics from the "W2D5 (bonus)" section below.

With your group
* (30 min) use the ABC...G questions from the example model/data projects to write your own answers and build a first version of your abstract.
* (30 min) by yourself, read the [Ten simple rules for structuring papers](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619). Pay close attention to figure 1, and how it specifies the same overall structure for the abstract, for each paragraph in the paper, and for the paper as a whole.  
* (1h) workshop your abstract together as a group. Say what you like and what you don’t like about it. Try to refer back to the principles from the "Ten simple rules" paper in order to find problems with your abstract and follow the recommended solutions from the paper.   

1h break

* (30-60 min) Edit the abstract individually in your own google doc. At this stage, it is also important to control the flow of the abstract, in addition to keeping the structure from the 10 rules-paper. The flow relates to the “writing style”, which is generally no different for scientists than for other writers. Most importantly, make sure each sentence continues from where the previous one left, and do not use jargon without defining it first. Check out this book about writing if you have time ([book](https://sites.duke.edu/niou/files/2014/07/WilliamsJosephM1990StyleTowardClarityandGrace.pdf), especially chapter 3 about "cohesion" and flow.
* (30 min) You should now have as many copies of your abstract as there are students in your group. Put them all into the same google doc, and try to see what you all did the same / differently. What sounds better? Pick and choose different sentences from different abstracts.


* (30-60min) Meet with your Project TA, show them your abstract. Try to get explicit feedback and edit the abstract together in a google doc.

* (30min / group = 1h) With your pod: present your research to the other group in your pod. Take turns in your pod to read each other’s abstracts and provide feedback on them. Tell the other group what you understand and what you don’t from their research project. Give detailed writing feedback if you can (use "suggestion mode" in google docs). If there is no other project group in your pod, ask your TA to reach out to other pods to find a group you can workshop your abstract with.

Back in your group
* (1-2h) Has the abstract refined or changed your question? Use the rest of this day to make a concrete plan for the final week of your project. If you already answered your question, then you will need to plan for control analyses, maybe including some simulated data that you need to also generate yourself.

Once you are done, please submit the abstract [here](https://airtable.com/app1MtChyjyKEDzAt/shr0ozNAhXq6K1p8o). We won't use this for further matching or anything like that, but we will keep a record of it to help us track the progress of all groups. If you really need/want to, the abstract can also be submitted on Monday (especially for timeslots 2,4 who have had one less project day so far).


### W2D5 (bonus)

Writing an abstract is also a good time to reflect on how your work relates to some of the big computational ideas in neuroscience. Relating your work to big ideas is a good way to get lots of people interested in your work! It is also a good way to find inspiration for what to do next. Maybe you have unknowingly proven an important theory? Think through the predictions that theory would make and see if you can steer your analyses towards validating or invalidating those predictions. Here is a list of big ideas the project team put together to think about. Some of them are covered in the course material (potentially next week). Don't be afraid to ask your TA (or project TA) if you are not familiar with some of these ideas, for example "why is sparsity such an important concept in neuroscience?". These kinds of questions usually spark good discussions.

1. Sparsity ([paper](https://www.nature.com/articles/381607a0.pdf?origin=ppub))

2. Mixed selectivity -- having individual neurons respond to multiple elements of a task/context/stimulus can increase the dimensionality of population activity and facilitate learning of arbitrary transformations ()[paper](https://www.nature.com/articles/nature12160)). Modeling idea: make toy model neuron populations based on your data that show either mixed selectivity or are pure labeled lines. How do things like decoder performance (especially for combinations of signals) differ between the two populations?

3. Predictive coding -- rather than encoding sensory input directly, it might be more efficient to encode differences between new and past sensory inputs ([paper]( https://onlinelibrary.wiley.com/doi/full/10.1002/wcs.142))

4. Computing through dynamics ([paper](https://www.annualreviews.org/doi/abs/10.1146/annurev-neuro-092619-094115))

5. Integrate-and-fire Network Models -- See Ch 5 of Dayan and Abbott, Theoretical Neuroscience

6. Generative models of neural activity -- evaluate critically the assumptions made about the generative model which is implied by your analysis method. What does it mean for principles of neural coding/ behavior? E.g. does the linear decoder do as well as a nonlinear decoder - does it suggest that encoding of this variable is likely linear in this brain region?

7. Transfer learning: can the linear (?) combination of basis sets learned from Data A be used to decode Data B? If so, then you might have found a fundamental "dictionary" of neural features (or "ensembles", or "clusters" or "syllables").

8. Generalization across days or individuals -- same as the transfer learning one, but across individuals. If the generalization works, have you found a "universal" set of sufficient features for a certain task?

9. Theories of Band Power (i.e. what is "alpha" band power associated with? what is gamma power associated with? etc.)

10. Labeled Lines -- is information encoded by specific, dedicated neurons, or distributed across a population of cells responding to more than one thing? See for example [10.1146/annurev.neuro.26.041002.131022](https://www.annualreviews.org/doi/abs/10.1146/annurev.neuro.26.041002.131022), [10.1016/j.mcn.2006.08.001](https://doi.org/10.1016/j.mcn.2006.08.001).

## W3 Project Time

Abstract writing day should have helped you narrow down what results (positive or negative) you would actually need to answer your question. You will use the rest of this time to try to get a result, or make progress towards an answer. This might not work out in such a short time, but don’t get discouraged: this part normally takes months if not years of work.

* If you know what analysis you need, but don’t know how to do it, the TAs are there to help you. They can point you to useful toolkits that may be difficult to find otherwise.
* Try not to implement complicated analyses from scratch. Use existing toolkits, and learn how to use them well. This kind of knowledge is very helpful long-term.
* If you find a negative answer to your question, that is absolutely ok! Please do report that. Then go back and think about how this affects your initial hypothesis. Does it rule it out, or could there be limitations in this particular data that lead to the negative result? What other data would you collect that would be better suited for answering this question? Try to design a new experiment in very specific detail and tell us about it. Who knows, somebody might run that experiment someday!
* If you find a positive result (i.e. the data matches your hypothesis), then you should spend the rest of your time validating it to make absolutely sure it is really true. You will need to design controls using the data (shuffling controls), or using simulated data, and you need to check the logic of your pipeline from start to end. Did you accidentally select only neurons that were tuned to a behavior, and then showed that they respond to aspects of that behavior? Did you sort neurons by their peak response time and then found sequences in your data? That is circular reasoning! There are some obvious and some not-so-obvious circular analyses that can catch even experienced researchers off-guard. This is what the controls are especially useful at catching.  

## W3D5: Final Presentations

Please see final day schedule and shared calendars for timing details: [https://compneuro.neuromatch.io/tutorials/Schedule/daily_schedules.html#w3d5-final-day-of-course](https://compneuro.neuromatch.io/tutorials/Schedule/daily_schedules.html#w3d5-final-day-of-course)

This is the day where you present your project to other groups. The groups will take turns to share their screens. You can use figures and other graphics, but this is meant to be told as a story, and everyone from your group should take a turn telling a part of the story. Tell us about the different hypotheses you’ve had at different points and how you refined them using some of the tools we taught.

At the end of your last project block, you should also submit your slides via this [Airtable link](https://airtable.com/shrvoz2N9UulAVqqU).   

### Schedule

* 10 minutes of meet & greet. Do a round of introductions (one TA calls out names from the zoom list). Everyone says their name, pod name, position, university and subject of study, as well as one interesting fact about themselves "Hi, I'm Jonny from the wiggly caterpillars and I am a PhD student at University of Notre Dame in Paris. I do neuroscience experiments in flies, and in my free time I like to go on long bike rides".

* 30-40 minutes of presentations, including questions. Each group should speak for approx 5 minutes (1 minute per person + 2 minutes of intro/discussion), and then take questions for 1-2 minutes. Try not to waste too much time on logistics: join the zoom link and go to the appropriate breakout room quickly. Then the student groups can start presenting in any order. 

* 10-20 minutes of general discussion. Here are some ideas for questions you could ask:
  * What was missing in the dataset that you would have really liked to have?
  * Does anyone plan to continue working on this project in the future? Perhaps a few students from the multiple groups would like to continue together?
  * Which one of the 10 steps to modeling/research was hardest and why?
  * Based on your experience with the NMA project, what project would you most like to do next? Make up your own, or pick from the NMA projects (a different dataset or project template which you did not use).
  * What surprised you the most about the process of doing a project? In what way was this project most different from other projects you have done in the past.
  * What technique did you learn at NMA which you think you can immediately apply to your own project (if you are currently doing research)?  


### Logistics:

* The lead TA for your megapod will make multiple subgroups of 4-5 research teams from across the entire megapod. Each subgroup gets a separate breakout room for their session. If there are too many large pods in the megapod, there may be multiple zoom links in the megapod, so make sure you have the right one for your group. 
  * timeslots 1,3,5:   last hour of project time, -1:00 to 0:00 relative to start of your normal tutorial time (check the shared calendars in jupyterbook).
  * timeslots 2,4: after the course feedback session (check the shared calendars in jupyterbook).
  There is a hard cutoff at the one hour mark, so the TAs must ensure everyone gets a turn to present.  

* Use this presentation style ([google slides](https://docs.google.com/presentation/d/1A1uaYarVot9YyCdbAAB4VDvsQfK6emqq-TwIZ9xVNwo/edit?usp=sharing) or [powerpoint](https://osf.io/ky6fj/download)) or create your own style!

* One minute per person and one slide per person only! This is primarily to ensure that everyone in your superpod gets to go before the hard cutoff at the one hour mark.

* Do not do introductions again, just present the material directly.

* When you are done presenting, leave the last slide up (with conclusions), and open the floor for questions.


### Content:

* The 1 minute, 1 slide rule might seem like an impossible limit. However, it is one of the most useful formats you can learn, often referred to as a "one minute elevator pitch". If you can become an expert at giving short pitches about your work, it will help you get the interest of a lot of people, for example when presenting posters at scientific conferences. Or when you accidentally find yourself in an elevator with Mark Zuckerberg: this could be your chance to secure a million dollars in research funds!

* The key to a good presentation is to practice it by yourself many times. It is not so different from other performing arts (acting, playing a musical instrument etc), where rehearsals are so crucial to a good performance.

* If something in your presentation doesn't sound good or doesn't make sense, you WILL get annoyed by it when you say it the tenth time, and that will make you want to change it. (Secret: this how professors prepare all of their presentations and it's why they always sound like they know what they are talking about)

* Always have an introduction slide and a conclusion slide. If your group is relatively large (>=5 people), then someone should be assigned to each of the intro and conclusion slides. If your group is small, then the same person can give intro + next slide, or conclusion slide + previous slide.

* Short anecdotes can work like magic for engaging your audience. As a general rule, most listeners are passive, bored, not paying attention. You have to grab their attention with that smart elevator pitch, or with a short anecdote about something that happened to your group while working on projects.

* Most groups won’t have a result and this is absolutely normal. However, the main goal anyway is to communicate the logic of your project proposal. Did you design a smart way to test the neural binding hypothesis, but then didn’t find the data to get answers? That can also be very interesting for others to hear about! Furthermore it will make it clear that research never stops. It continues as a series of questions and answers, not just within your own project, but at the level of the entire research field. Tell us what got you excited about this particular project, and try to dream big. One day, models like yours could be used to do what?


### Questions:

* If your presentation was short enough, there can be time for questions from the audience. These are a great way to get feedback on your project!

* Before you ask a question, consider whether others might be interested in that topic too. This usually means asking big picture questions, as opposed to detailed, technical questions, but there are exceptions.

* If you are answering the question, try to be short and concise. Rambling is very clear to the audience, and it can seem like you're avoiding to answer the question. Answering concisely is another very useful skill in "real life". It also means that you can take more questions given our time constraints.
