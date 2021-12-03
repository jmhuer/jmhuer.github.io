#!/usr/bin/env python
# coding: utf-8

# ## Automatic Music Composition and Completion
# 
#  <sub> <a href="https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html" style="color: red; text-decoration: underline;text-decoration-style: dotted;">← Back to Projects</a> </sub>
# 
# <img src="../../../../images/amcc.png" align="center"/>
# 
# <br>
# 
# We present a new symbolic approach to auto- matic music generation. First we create a dataset of 62 hours of Mozart music represented by binary piano roll arrays. The dataset is used to train a 1-hidden layer neural network to predict a section of music given the surrounding music. After training we will use our model to continu- ously predict and replace random sections of existing music completely altering the original into what we consider new music.
# <br>
# 
# 
# ## Introduction
# ---
# 
# In this paper we are attempting to generate music that utilizes the clarity and low com- putational cost of a symbolic representation while maintaining a good variation and global structure. However unlike the usual approach to generate music we will not use any form of sequence modeling mechanism. Instead we will attempt to create a new sequence of music by altering an existing sequence of music. To accomplish this, we will train a neural network to predict a missing section of music given the surrounding music. After trining, we will use our model to predict and replace sections of existing music.
# 
# 
# 
# ## Method
# ---
# 
# 
# A linear program LP is a special instance of an SDP.
# This means the LP can be written as an SDP
# 
# <img src="../../../../images/amcc.png" align="center"/>
# 
# 
# 
# ## Results
# ---
# 
# Below we show a few results
# 
# 
# <img src="../../../../images/(1).png" align="center"/>
# 
# 
# **Orginal**
# 
# <audio controls>
#   <source src="../../../../audio/a.wav" type="audio/wav">
# Your browser does not support the audio element.
# </audio><br>
# <br>
# 
# **Generated**
# 
# <audio controls>
#   <source src="../../../../audio/a.wav" type="audio/wav">
# Your browser does not support the audio element.
# </audio><br>
# <br>
