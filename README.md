[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/coiled/data-science-at-scale/master?urlpath=lab)

**Note:** This repository is currently a work in progress. If you are joining for any given tutorial, please make sure to clone // pull the repository 2 hours before the tutorial begins.


# Data Science At Scale

This tutorial's purpose is to introduce Pythonistas to methods for scaling their data science and machine learning work to larger datasets and larger models, using the tools and APIs they know and love from the PyData stack (such as `numpy`, `pandas`, and `scikit-learn`).


## Prerequisites

Not a lot. It would help if you knew

* programming fundamentals and the basics of the Python programming language (e.g., variables, for loops);
* a bit about `pandas`, `numpy`, and `scikit-learn` (although not strictly necessary);
* a bit about Jupyter Notebooks;
* your way around the terminal/shell.


**However, I have always found that the most important and beneficial prerequisite is a will to learn new things so if you have this quality, you'll definitely get something out of this code-along session.**

Also, if you'd like to watch and **not** code along, you'll also have a great time and these notebooks will be downloadable afterwards also.

If you are going to code along and use the [Anaconda distribution](https://www.anaconda.com/download/) of Python 3 (see below), I ask that you install it before the session.


## Getting set up computationally
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/coiled/data-science-at-scale/master?urlpath=lab)

The first option is to click on the [Binder](https://mybinder.readthedocs.io/en/latest/) badge above. This will spin up the necessary computational environment for you so you can write and execute Python code from the comfort of your browser. Binder is a free service. Due to this, the resources  are not guaranteed, though they usually work well. If you want as close to a guarantee as possible, follow the instructions below to set up your computational environment locally (that is, on your own computer). Note that Binder will not work for all of the notebooks, particularly when we spin up Coiled Cloud. For these, you can follow along or set up your local environment as detailed below.


### 1. Clone the repository

To get set up for this live coding session, clone this repository. You can do so by executing the following in your terminal:

```
git clone https://github.com/coiled/data-science-at-scale
```

Alternatively, you can download the zip file of the repository at the top of the main page of the repository. If you prefer not to use git or don't have experience with it, this a good option.

### 2. Download Anaconda (if you haven't already)

If you do not already have the [Anaconda distribution](https://www.anaconda.com/download/) of Python 3, go get it (n.b., you can also do this w/out Anaconda using `pip` to install the required packages, however Anaconda is great for Data Science and I encourage you to use it).

### 3. Create your conda environment for this session

Navigate to the relevant directory `data-science-at-scale` and install required packages in a new conda environment:

```
conda env create -f binder/environment.yml
```

This will create a new environment called data-science-at-scale. To activate the environment on OSX/Linux, execute

```
source activate data-science-at-scale
```
On Windows, execute

```
activate data-science-at-scale
```


### 4. Open your Jupyter Lab

In the terminal, execute `jupyter lab`.

Then open the notebook `0-overview.ipynb` and we're ready to get coding. Enjoy.
