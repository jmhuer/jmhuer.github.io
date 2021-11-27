#!/usr/bin/env python
# coding: utf-8

# ## VaryCHarm: A Method to Automatically Vary the Complexity of Harmonies in Music
# 
#  <sub> [← Back to Porfolio](https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html)</sub>
# 
# <img src="../../../../images/aelstm.png" align="center"/>
# 
# <br>
# 
#  **In this post we formulate the problem of varying music complexity mathematically and propose a method to preserve general harmonic structure and melody while vary-ing the number of notes. To do this, we find a compressed representationof pitch while simultaneously training on symbolic chord predictions. Wetest different pitch Autoencoders with various sparsity constraints, and evaluate our results by plotting chord recognition accuracy with increas-ing and decreasing  number  of  notes, observations  in relation  to  music theory, and by analysing absolute and relative musical features with a probabilistic framework.**
# 
# <br>
# 
# 
# ## Introduction
# ---
# 
# There are many applications such as:
# 
# -   Machine learning and data science
# -   Astronomy
# -   Artificial intelligence
# -   Chemistry
# -   Computational biology
# 
# 
# 
# 
# ## Problem Defenition
# 
# It is clear automatically varying the complexity of music has valuable applications. But how do we approach this problem without supervision? In words, we want to add or remove notes without diverging too much from the original "feeling" of music. In math we write:
# > **The Problem of Varying Harmonic Information**:
# >
# >We denote Symbolic music information as piano rools where the input is information with a fixed history length $H$ as a matrix $X_t \triangleq x_{t-H:t} \in \{0,1\}^{P \times H}$. For simplicity, we denote $\mathcal{X} = \{0,1\}^{P \times H}$ as the input space.
# >
# >Then the goal is to learn a mapping $f_\theta(X_t; \eta) \rightarrow \hat{X}_t \in \mathcal{X}$ parameterized by $\theta$ such that $\hat{X}_t$ summarizes (or further ornament) the original piece of music $X_t$, given a hyper-parameter $\eta \in [0,1]$ that controls the sparsity level of $\hat{X}_t$. More specifically, we consider the following optimization:
# >
# >$$  \min_{\theta} \mathcal{D}\bigg(f_\theta(X_t; \eta),~X_t\bigg) ~~\text{s.t.}~~||f_\theta(X_t; \eta)||_0 \leq \eta HP.$$
# >
# 
# 
# 
# 
# 
# 
# ## How do we solve this problem?
# 
# In order to reconstruct pitch vectors with the extra criteria of maintaining theoriginal chord/harmonic functionality, we propose a combined loss of MSE onpitch vector reconstruction and Cross Entropy on symbolic chord targets. Thereconstruction should be such that we do not lose the ability to map the originalchords but the information bottleneck serves to generalize pitch functionality
# 
# 
# 
# 
# 
# ## Numerical Example
# 
# Below we have some randomly selected examples using a validation set:
