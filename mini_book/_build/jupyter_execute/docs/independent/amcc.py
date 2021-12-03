#!/usr/bin/env python
# coding: utf-8

# ## Automatic Music Composition and Completion
# 
#  <sub> <a href="https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html" style="color: red; text-decoration: underline;text-decoration-style: dotted;">← Back to Porfolio</a> </sub>
# 
# <img src="../../../../images/amcc.png" align="center"/>
# 
# <br>
# 
#  In this blog post I will explain what an SDP is and one application: how to find optimal bridge points using Python libraries: scikit, numpy, pytorch. explain what an SDP is and one application: how to find optimal bridge points using Python libraries: scikit, numpy, pytorch.
# 
# <br>
# 
# 
# ## Introduction
# ---
# 
# An SDP (Semidefinite Programming) is a superclass of LP (linear programming). Its called an SDP because the programs can
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
# ## Formal Defenition
# 
# > **Semidefinite Programming (SDP)** has the form
# >
# >```{math}
# >\begin{array}{ll}
# >\operatorname{minimize} & C \bullet X \\
# >\text { s.t. } & A_{i} \bullet X=b_{i} \quad i=1, \ldots, m \\
# >& X \succeq 0
# >\end{array}
# >```
# >```{math}
# >C \bullet X:=\sum_{i=1}^{n} \sum_{j=1}^{n} C_{i j} X_{i j}
# >```
# 
# 
# 
# 
# ## Method
# 
# A linear program LP is a special instance of an SDP.
# This means the LP can be written as an SDP
# 
# <img src="../../../../images/snn.png" align="center"/>
