# Introduction to Programming using Python
This is meant to be a short course that helps you to start programming in Python, especially if you have little to no background in programming. There is no need for yet another course on how to learn Python, instead I will select a subset of topics that are likely to be interesting for researchers, give a short introduction and point towards resources where you can learn more. First we will cover the basics of how to program in Python and get everyone up and running. After having mastered the very basics, each student will design a small programming project, e.g. downloading data from the internet, reorganizing a dataset, statistical analysis of some data... In general many repetitive tasks can be automated in a python script and we'll learn how to do that in the next few weeks. Over time you will appreciate the versatility and simplicity of Python!

Some Links:
* [Python Getting Started](https://www.python.org/about/gettingstarted/)
* [Python Wiki in other languages](https://wiki.python.org/moin/Languages)
* [Curated list of links related to Python](https://github.com/vinta/awesome-python)
* [Data Science related Notebooks](https://github.com/donnemartin/data-science-ipython-notebooks)

## Class 0 - Git and installing python

[Slides - Class 0](https://gitpitch.com/chrished/intro_prog_py/master?p=class0)

1. Before we start with Python, you should make yourself familiar with [Git](https://git-scm.com/) and [Github](https://github.com/). Git is a distributed version control system, mainly used for code.  To get familiar with git follow this [tutorial](https://try.github.io)

2. Install Python. I suggest the [Anaconda Distribution](https://www.anaconda.com/download). It comes with many packages preinstalled and an IDE similar to RStudio. Please install python 3.*


#### How to Install Packages with conda
1. check for the right link by searching for it: e.g. search for `conda install unidecode`
2. you will find [this](https://anaconda.org/anaconda/unidecode)
3. using conda you run: `conda install -c anaconda unidecode` (This is NOT a python command!)
  * open the "Anaconda prompt" on Windows, or the "terminal" on Mac/Linux
  * type `conda install -c anaconda unidecode` and press enter, say yes if conda asks you to install packages

### Excercises Class 0
0.1. As an exercise you should create a private repository on github (sign up as an academic account if possible so you get unlimited private repositories).  Clone the repository to your computer and add a txt file. Commit your work and then push it to the github server.

0.2. Open Spyder and run the "Hello World!" program.

## Class 1 - First Introduction to Python

[Slides - Class 1](https://gitpitch.com/chrished/intro_prog_py/master?p=class1)

* Basic introduction: Define variables, lists and dictionaries
* Operators on numbers/strings
* Data types
* Booleans
* if-else, for-, while-loops

## Class 2 - Programming Essentials

[Slides - Class 2](https://gitpitch.com/chrished/intro_prog_py/master?p=class2)

After this class you know the most important programming concepts, based on which you can write almost any program.

* Revisit basics
* Functions
* import a package
* numpy/scipy/pandas


## Class 3 - Interacting with the web, File IO
[Slides - Class 3](https://gitpitch.com/chrished/intro_prog_py/master?p=class3)

* urllib
* File IO using pandas and open/csv
* Beautiful Soup


## Class 4 - Student Projects
[Slides - Class 4](https://gitpitch.com/chrished/intro_prog_py/master?p=class4)


From now on, classes will be more like a QA session. You can only learn programming by doing, therefore it's important to get started on your projects and along the way I can help with issues that come up.

* Plan your own project using python, what concepts do you need to learn? What packages do you need?

Don't know where to start/what to do? Checkout these links:

1. [edX Course on Python for Research](https://courses.edx.org/courses/course-v1:HarvardX+PH526x+1T2018/course/)
2. Andy Halterman for stuff on creating/analyzing event data: https://andrewhalterman.com/2017/05/08/making-event-data-from-scratch-a-step-by-step-guide/ or his [Github page](https://github.com/ahalterman?tab=repositories)
3. Natural Language Processing: e.g. [Spacy](https://spacy.io/)
4. Face Recognition (as a service) by [Face++](https://www.faceplusplus.com/)
5. Extract text from PDFs: [pdfminer](https://github.com/euske/pdfminer)

For some tips on best practices for your own code see the top answer [here](https://stackoverflow.com/questions/356161/python-coding-standards-best-practices).

## Class 5 and 6: Support and Presentation of projects
* Work on personal project
* Help with issues and setup of project.
* students should present their use case
