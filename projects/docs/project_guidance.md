# Daily guide for projects

## Summary

This project plan explicitly encourages the iterative nature of research as a series of questions and answers that gradually refine your hypotheses. You will start with the W1 course content, which teaches you about modeling, the scientific process, and some basics of neural data analysis. You will then apply the steps taught there to a vaguely formed hypothesis or topic of interest to you on W2D1, when half of the day is devoted to developing project proposals. Your proposal will not be perfect, because you still don’t know much about the data or about a phenomenon of interest at that point. Throughout W2, you will develop your knowledge about your topic, and frequently go back to the cheat sheet of research steps taught in W1. On W2D5, you will write a short abstract about your project, which may or may not include results, but it should at least include a testable hypothesis. You'll swap abstracts with other groups and get feedback from your mentors. For the rest of the course, you will focus on getting evidence for/against your hypothesis. Finally, in W3D5 you will meet with other groups in your pod and superpod, and tell them the story of your project. This is a low-key presentation that may include some of the plots you made along the way, but it is not meant as a real research presentation with high “production values”. See some of the [examples](https://compneuro.neuromatch.io/projects/docs/project_2020_highlights.html) from last year to get a sense of what the presentation will look like.

## Submission Links
- W2D5 Abstract Submission [Airtable Link](https://airtable.com/shr0ozNAhXq6K1p8o)
- W3D5 Project Submission [Airtable Link](https://airtable.com/shrvoz2N9UulAVqqU)

## Project templates

[Project templates](https://compneuro.neuromatch.io/projects/docs/project_templates.html) are research ideas developed by the NMA team that can be used in conjunction with the datasets we provided. Project templates can be used in a variety of ways.
* For starters, you can use the project templates just to get familiarized with some of our datasets or one of the provided models. They can provide keywords for you to use in your proposal on D2, or python libraries you can reuse to answer your own questions.
* You should use the project templates extensively if you are new to neuroscience and/or you don’t have a lot of research experience. They have been designed to give you enough structure to get started, and enough options to keep you going if you stick with the template. Or you may start with a template, use it the first week and then in the second week diverge from it as your group develops their own new idea or question to test.
* Templates have a natural flow of questions, but don’t hesitate to skip or completely change some of these. They are meant to be used very flexibly!

## Project TAs

Project TAs are a new role at NMA this year, and they are your friendly dataset experts to consult with on all issues related to datasets. They can also help with other aspects of a project, including brainstorming, literature searches and coding. You will have a one-hour meeting with one of them on your first two project days. During this time, they will help you refine your question and hypothesis into something that can be answered with our datasets. Since they can arrive unannounced at any time (busy schedules!), please stop what you were doing to have the meeting, and then resume your work when the project TA leaves.

In later days, project TAs will be assigned meetings with junior groups, but can also be recruited to senior groups for meetings when you need them. For the assigned meetings, project TAs will generally come only during project times, but sometimes they might need to schedule meetings slightly earlier or later. We encourage you to reach out to them for extra meetings whenever you need them, and to post questions on discord in the #dataset-X channels. All project TAs have time set aside specifically to answer discord questions and to provide additional meetings when necessary.

## Project Mentors

Project mentors are more senior figures in the field, typically senior postdocs, professors, or industry researchers. Each project group will have a mentor to help them refine their hypotheses and navigate the scientific process. They won't be around as often as the TAs, but they are another source of guidance and perspective.

## W1 Project Time

You'll have 2-3 hours each day to work on projects. The goal during the first week is to learn about the research process and start brainstorming ideas. To simplify logistics, we have already broken you into project groups. Moreover, we've organized the pods (and the groups within them) so that everyone is interested in the same type of data (fMRI, Neurons, Behavior, etc.).

### W1D1
Spend the first few sessions getting to know one another and learning about projects.
* Introductions: say a few things about yourself, then about your research area or research interests. What are you really curious about, that you might explore in your NMA project?
* Listen carefully as others talk about their interests. If you are curious about something, ask them.
* Individual reading time: browse the projects booklet which includes dataset details and project template details. Watch some of the videos that are of interest to you.

### W1D2
Brainstorming! Try to come up with one or a few topics of interest, either by yourselves or directly from the booklet (i.e. project templates). Get your hands dirty by running some of the notebooks provided for your dataset. There should be a loading notebook, and there should be some further analysis notebooks interspersed among the project templates. Even if you are not using a project template, they are likely to contain useful code to get you started, especially if you are doing a theory project. If all you do is run the provided notebooks that’s fine! Try to understand what is being plotted and how. Pay attention to the code libraries being used, and the way the data is accessed / binned / aligned. You will reuse some of these code elements to start doing your own analyses in later days.

*Stay tuned for your mentor assignments. Once you receive them, reach out to your mentor to set up a first meeting. Also try to arrange a meeting for W2D1, ideally the second half of the day, when their feedback on your abstract could be useful.*

### W1D3-W1D5
Be on the lookout for interesting hypotheses. You might notice something weird in the data, and if you dig deeper it might lead you directly to a result. For this to work, you must keep an open mind about what your questions are. If you feel like your question is starting to change, go back to Steps1-5 and see if it’s easier to formulate those steps with the new question. A good question/hypothesis makes the 5 steps really easy to think through. Here are some generally useful tips & tricks:

* The hardest part will be wrestling with the data to try to answer your question. You can rely on your TAs, the dedicated project TAs and the Discord channels to make this process easier.
* For theory projects, wrestling with your model can be equally challenging. If your model generates data, for example a neural network simulation, then you can still use some of the tricks below to analyze that data.
* If your model makes a hypothesis that needs to be tested, then your theory project might become a data project. The opposite may also happen: you may find something interesting in the data, and realize that you need a model to understand it better.  
* Always be on the lookout for bugs in your code, or ”bugs” in your analysis plan. If a plot/result looks too good to be true, it might be! Make sure you always split your data train/test, even for simple analyses where you think it might not matter (i.e. for making tuning curves).
* If your question does change, remember to always do a quick literature survey (i.e. google search) to see if others thought about your question in the past. You don’t need to come up with a completely original question! Do however situate your research within the relevant literature, and try to get hints/suggestions from other papers.
* Depending how complex your question is, there could be several data analysis steps:
   * data wrangling: some questions can be answered simply by plotting the right variable from the data! Some generally useful strategies: make PSTHs and tuning curves; try scatter plots of different variables; plot across neurons or across trials; select the most tuned neurons and look just at those; if there are multiple sessions pick a good one and dig deep into that one.
   * simple, linear analyses: most questions can be answered at this stage. This is often needed if you are doing a “population analysis”, i.e. trying to determine if a set of neurons or voxels collectively encode a certain variable. By far, the most used linear analyses are linear regression, PCA and k-means clustering.
   * Linear regression is often a good first step, even if your variables are binary/categorical. Once you have a pipeline, it will be easy to switch to logistic regression or other predictors from the scikit-learn library.
   * For visualizations, you might want to reduce a population of neurons to just a few components using PCA, then go back to the “data wrangling” steps and make the same kinds of plots for PCs that you made for neurons.
   * Another way to reduce the size of data is to cluster neurons (or trials!) into a few subsets, then average within that cluster. The simplest clustering model is k-means, which is a “linear” clustering model.
* complicated, nonlinear analyses: if the simple analyses fail, you might think you have no choice but to try something fancy, like deep learning or ISOMAP. This is often a dead end where projects go to die! You probably will make a lot more progress by slightly (or greatly) changing your question, or refining your hypothesis. The reason complicated analysis are so hard to do and interpret is that they often function as black boxes that are hard to look into. What do the parameters of a deep neural network mean? That is a hard research question in its own right. This is not to say that your hypothesis cannot be a nonlinear model, just that you can often test nonlinear hypotheses with simple, even linear analyses. If you must, however, use complicated analyses, then deep learning “replaces” linear regression, t-SNE / ISOMAP replaces PCA, and hdbscan replaces k-means.
   * deep learning as a prediction tool. This is unlikely to do better than linear/logistic regression, because neural data is noisy, and you need a lot of training data to really train a deep network well. This is because deep networks have a lot of parameters.
   * There are many “nonlinear dimensionality reduction” methods like t-SNE / ISOMAP, but these are often not meant as replacements for PCA, but instead as visualization tools to try to see a clustering structure in your data. They can be useful for making hypotheses based on interesting-looking plots. You still need to validate those hypotheses using simpler methods, like clustering and PCA.
   * There are many nonlinear clustering models like hdbscan and spectral clustering, but those are fickle for high-dimensional data and difficult to interpret. You will have to carefully try different parameters, and think through what the clusters mean.


## W2 Project time

Week 2 is when projects really start to ramp up.

### W2D1: Project Half Day
We have designed tutorials to help launch your projects. Once you're done with them, you will complete your literature review and work on your project proposal.

(2h) Complete the intro/tutorial/outro for this day
* You will need to use your group's project for some of this content. If you don’t have concrete ideas yet, or you haven’t done a research project before, use one of the provided project templates to walk through the four steps.
* If you are using a project template, your goal is to translate the information from the slide and colab notebook into a 4-step format. Some information might not be readily available in the slide or notebook, and you might have to find it in your literature review later this day.
* Try to write down a few sentences for each of the four steps applied to your project. You will re-use these in your proposal later today.  

(1.25h) Literature review: identify interesting papers
The goal of this literature review is to situate your question in context and help you acquire some keywords that you will use in your proposal today.
* (30min) on your own, start doing a literature review using google searches and only look at abstracts to select 2-3 promising ones.  
* (10min) report to the whole group what papers you found and pool them together. Assign one paper per person to read/skim in the next 1h.  
* (1h) on your own, read the paper that was assigned to you. Make notes in a common google doc shared with your group, and especially write down important keywords or concepts which you might use in your proposal later today. If you are not connected to an .edu domain or a VPN, try to find full versions of papers on preprint servers like arXiv / bioRxiv. You could also ask your TA to get it for you (and they might in turn ask someone who has access to a university VPN). There might be other options too…  
* (1h) report back to the group, and try to tell them as much as you understood about the paper. Get into details, but don’t just read to them whole sections from the paper. Ask the other students questions about the papers they are presenting to understand them better.

Project block task:
(3h) Project proposal
* Try to write a proposal for this project based on the way you understand it now. This should re-use some of the text you wrote down for the four steps, and should include keywords and concepts that you identified in your literature review. Don’t worry too much about the structure of this paragraph! The goal is to get as many words (200-300) on paper as possible. You have the entire day 10 to learn how to write a properly structured scientific abstract.
* It is important to include the concepts which you identified as relevant, and the keywords that go with them.
* When you are ready, please submit your proposal [here](https://airtable.com/shrcYuFYMPh4jGIng) so we have it. This is not mandatory and can be submitted at any time.

###  W2D2

You should now have a sense of the data, and you have probably refined your hypothesis a little. You might have a vague idea of what it would take for your project to work, what tools you might use, and what the answer could look like. Let’s make these things explicit, by continuing with steps 6-9 of the modeling practice in this [steps 5-10 notebook](https://compneuro.neuromatch.io/projects/modelingsteps/ModelingSteps_5through10.html).

* (0.5h) Go through the first five steps again with your own refined question. Try to write down what the steps looks like for your data.
* (1-2h) Go through steps 6-10 for the example project in the new notebook and watch the videos.
* (1-2h) The rest of the day, start thinking what these steps would look like for your project, without actually doing the steps. Do you need to select a toolkit and where can you find some options? Do you need to implement a model? Don’t actually implement the model on this day! Try to complete the low-hanging fruit first, because you’ll have the rest of this week and next for the actual full implementation of your project.

### W2D3 and W2D4

You will implement Steps 5-9 in your project. If you are already experienced with research projects, this might just look like a continuation of preceding sessions and you don’t need to stick to the steps too closely. If you are not so experienced, you could benefit from implementing the steps one after the other.

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


With your mentor (timing is not precise!)
* (30-60min) Try to schedule a meeting with your mentor to be about now (or any time in the second half of this day). Show them your abstract. Try to get explicit feedback and edit the abstract together in a google doc.

Last 3h, with the pod.

* (30min / group = 1h) It is always revealing to present your research to someone who has never heard about it. Take turns in your pod to read each other’s abstracts and provide feedback on them. Tell the other group what you understand and what you don’t from their research project. Give detailed writing feedback if you can (use "suggestion mode" in google docs). If there is no other project group in your pod, ask your TA to reach out to other pods to find a group you can workshop your abstract with.

Back in your group
* (1-2h) Has the abstract refined or changed your question? Use the rest of this day to make a concrete plan for the final week of your project. If you already answered your question, then you will need to plan for control analyses, maybe including some simulated data that you need to also generate yourself.

Once you are done, please submit the abstract [here](https://airtable.com/shrITSzD4fgFCGiWI). We won't use this for further matching or anything like that, but we will keep a record of it to help us track the progress of all groups. If you really need/want to, the abstract can also be submitted on Monday (especially for timeslots 2,4 who have had one less project day so far).


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

## W3D5: Final Presentations (Friday tutorial block for everyone)

This is the day where you present your project to other groups. Your mentor and your project TAs can be invited too, but they are busy so they might not make it. The groups will take turns to share their screens. You can use figures and other graphics, but this is meant to be told as a story, and everyone from your group should take a turn telling a part of the story. Tell us about the different hypotheses you’ve had at different points and how you refined them using some of the tools we taught.

At the end of your last project block, you should also submit your slides via this [Airtable link](https://airtable.com/shr9Ge6A94JB7TOPI).   

### Schedule

* 10 minutes of meet & greet. Do a round of introductions (one TA calls out names from the zoom list). Everyone says their name, pod name, position, university and subject of study, as well as one interesting fact about themselves "Hi, I'm Jonny from the wiggly caterpillars and I am a PhD student at University of Notre Dame in Paris. I do neuroscience experiments in flies, and in my free time I like to go on long bike rides".

* 30-40 minutes of presentations, including questions. Each group should speak for approx 5 minutes (depending on group size), and then take questions for 1-2 minutes. The order of presentations should be the one from the email.

* 10-20 minutes of general discussion. Use the following questions to guide the group discussion. Spend a few minutes on each question. It's ok not to use all these questions, especially if you have your own questions to ask!   
  * What was missing in the dataset that you would have really liked to have?
  * Does anyone plan to continue working on this project in the future? Perhaps a few students from the multiple groups would like to continue together?
  * Which one of the 10 steps to modeling/research was hardest and why?
  * Based on your experience with the NMA project, what project would you most like to do next? Make up your own, or pick from the NMA projects (a different dataset or project template which you did not use).
  * What surprised you the most about the process of doing a project? In what way was this project most different from other projects you have done in the past.
  * What technique did you learn at NMA which you think you can immediately apply to your own project (if you are currently doing research)?  


### Logistics:

* You will present to other groups (3-5 groups per room). An email will be sent with the zoom room of one of the pods where everyone goes for one hour corresponding to either:
  * timeslots 1,3,5:   last hour of project time, -1:00 to 0:00 relative to start of your normal tutorial time (check the shared calendars in jupyterbook).
  * timeslots 2,4: after the course feedback session (check the shared calendars in jupyterbook).
  There is a hard cutoff at the one hour mark, so the TAs must ensure everyone gets a turn to present.  

* Use this presentation style ([google slides](https://docs.google.com/presentation/d/1A1uaYarVot9YyCdbAAB4VDvsQfK6emqq-TwIZ9xVNwo/edit?usp=sharing) or [powerpoint](https://osf.io/ky6fj/download)) or create your own style!

* One minute per person and one slide per person only! This is primarily to ensure that everyone in your superpod gets to go before the hard cutoff at the one hour mark.

* Do not do introductions again, just present the material directly.

* When you are done presenting, leave the last slide up (with conclusions), and open the floor for questions.


### Content:

* The 1 minute, 1 slide rule might seem like an impossible limit. However, it is one of the most useful formats you can learn, often referred to as a "one minute elevator pitch". If you can become an expert at giving short pitches about your work, it will help you get the interest of a lot of people, for example when presenting posters at scientific conferences. Or when you accidentally find yourself in an elevator with Mark Zuckerberg: this could be your chance to secure a million dollars in research funds!

* The key to a good presentation is to practice it by yourself many times. It is no different from other performing arts (acting, playing a musical instrument etc), where rehearsals are so crucial to a good performance.

* If something in your presentation doesn't sound good or doesn't make sense, you WILL get annoyed by it when you say it the tenth time, and that will make you want to change it. (Secret: this how professors prepare all of their presentations and it's why they always sound like they know what they are talking about)

* Always have an introduction slide and a conclusion slide. If your group is relatively large (>=5 people), then someone should be assigned to each of the intro and conclusion slides. If your group is small, then the same person can give intro + next slide, or conclusion slide + previous slide.

* Short anecdotes can work like magic for engaging your audience. As a rule, most listeners are passive, bored, not paying attention. You have to grab their attention with that smart elevator pitch, or with a short anecdote about something that happened to your group while working on projects.

* Most groups won’t have a result and this is absolutely normal. However, the main goal anyway is to communicate the logic of your project proposal. Did you design a smart way to test the neural binding hypothesis, but then didn’t find the data to get answers? That can also be very interesting for others to hear about! Furthermore it will make it clear that research never stops. It continues as a series of questions and answers, not just within your own project, but at the level of the entire research field. Tell us what got you excited about this particular project, and try to dream big. One day, models like yours could be used to do what?


### Questions:

* If your presentation was short enough, there can be time for questions from the audience. These are a great way to get feedback on your project!

* Before you ask a question, consider whether others might be interested in that topic too. This usually means asking big picture questions, as opposed to detailed, technical questions, but there are exceptions.

* If you are answering the question, try to be short and concise. Rambling is very clear to the audience, and it can seem like you're avoiding to answer the question. Answering concisely is another very useful skill in "real life". It also means that you can take more questions given our time constraints.
