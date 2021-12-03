---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

## Automate Data Labeling using Temperature Differential

 <sub> <a href="https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html" style="color: red; text-decoration: underline;text-decoration-style: dotted;">← Back to Porfolio</a> </sub>

<img src="../../../../images/thermal.png" align="center" />

<br>

Data labeling for object detection/segmentation is expensive to acquire.  In this blog post we show we can sped up this proesses of labeling data for certain objects using a thermal camera, and standard computer vision techniques.We can create mask or ROI annotations depending on annotations of interest.

<br>


## Introduction
---

There are various popular dataset but for costume objects one has to take images and manually label the example as shown in the image below

<img src="../../../../images/labelex.gif" width="80%" align="center"/>

<br>

This technique can be applied two ways:
- To speed up data collection process to train supervised computer vision models
- To be used for object localization in combination with a classification model, to achieve segmentation or object detection task


This technique can only be used in specific use cases where objects of interest have a noticeable temperature difference. Such as:
- Living things
- Stove top cooking, ovens, or cooking in general
- Items that can be cooled before collecting data


##  Method
---

The method consists of the following steps.

Step 1: Find placement for thermal/RGB camera
- In the following slides we show two examples: handheld & above stovetop

Step 2: Specify expected temperature of item of interest
- For example: 10C < temp > 30C  or temp > 30C) and classes name

Step 3: Run
- Apply thermal image postprocessing to obtain localization of objects
- Store RGB image and annotated data

Our postprocessing is as follows: Bucket fill ->  K-means -> Find contour



##  Stove top examples
---

Here we have a example of living

<img src="../../../../images/thermalfood.png" align="center"/>

<br>

##  Regular objects heated up
---

Here we have a example of living

<img src="../../../../images/thermalwarm.png" align="center"/>

<br>


##  Humans or animals
---

Here we have a example of living

<img src="../../../../images/thermal.png" align="center" />

<br>
















