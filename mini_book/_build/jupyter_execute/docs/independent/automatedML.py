#!/usr/bin/env python
# coding: utf-8

# ##  Automated Machine Learning with SkLearn
# 
#  <sub> <a href="https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html" style="color: red; text-decoration: underline;text-decoration-style: dotted;">← Back to Projects</a> </sub>
# 
# <img src="../../../../images/automatedml.png" align="center"/>
# 
# <br>
# 
#  In this post Ill explain automated machine learning (AutoML); and provide an example for a simple classificatino tasks using various common algorithms in a frequentist and bayesian setting
# 
# <br>
# 
# 
# ## What is AutoML?
# ---
# 
# Automated Machine Learning (AutoML) is tied in with producing Machine Learning solutions for the data scientist without doing unlimited inquiries on data preparation, model selection, model hyperparameters, and model compression parameters.
# On top of that AutoML frameworks help the data scientist in:
# - Data visualization
# - Model intelligibility
# - Model deployment
# 
# AutoML is viewed as about algorithm selection, hyperparameter tuning of models, iterative modeling, and model evaluation. It is about making Machine Learning tasks easier to use less code and avoid hyper tuning manually.
# 
# <img src="../../../../images/automl.png" align="center" />
# 
# <br>
# <br>
# 
# ## Random Search
# ---
# 
# The simplest way to think about hyper parameter optimization is to randomly try different combinations and pick the best setting
# 
# <br>
# 
# ## Grid Search
# ---
# 
# Another approach is to iterate through a list of possible configurations. This is know as grid search
# 
# ### Sklearn tools
# 
# ```
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import make_pipeline
# from sklearn.model_selection import GridSearchCV
# from sklearn.svm import SVR
# 
# # Instantiate a SVR model with standard scaler
# # Create pipeline 
# svr = make_pipeline(StandardScaler(), SVR(kernel='linear'))
# 
# #Define parameter grid
# parameters = {'svr__kernel':['linear', 'rbf'], 'svr__epsilon':[0.1, 0.2, 0.3,0.6], 'svr__C': [0.1,0.5,1,2,3]}
# 
# # Grid cross-validation object is ready
# svr = GridSearchCV(svr, parameters)
# 
# 
# ```
