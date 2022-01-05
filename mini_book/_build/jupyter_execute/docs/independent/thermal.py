## Automate Data Labeling using Temperature Differential

 <sub> <a href="https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html" style="color: red; text-decoration: underline;text-decoration-style: dotted;">← Back to Projects</a> </sub>

<img src="../../../../images/thermal.png" align="center" />

<br>

Data labeling for object detection/segmentation is expensive to acquire.  In this blog post we show we can sped up this proesses of labeling data for certain objects using a thermal camera, and standard computer vision techniques. We can create mask or ROI annotations depending on annotations of interest.

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

Here is the code used: [Auto-label](https://github.com/jmhuer/mask_from_thermal_image)


You will need a Flir camera specifically since it is crucial to be able to take an image with both RGB and Thermal sensors and calibrate overlay between the two images.


##  Method
---

The method consists of the following steps.

**Step 1**: Find placement for thermal/RGB camera
- In the following slides we show two examples: handheld & above stovetop

**Step 2**: Specify expected temperature of item of interest
- For example: 10C < temp > 30C  or temp > 30C) and classes name

**Step 3**: Run
- Apply thermal image postprocessing to obtain localization of objects
- Store RGB image and annotated data

Our postprocessing is as follows: Bucket fill -> 
K-means -> Find contour



##  Stove Top Examples
---

Here we have an example applying our proposed method on food being cooked. This setting provides us a very natural temperature differential since the pan is almost always hotter than the food. Of course there are exceptions but this method is not meant to sutable for all settings, otherwise we wouldnt need ai :D

<img src="../../../../images/thermalfood.png" align="center"/>

<br>

##  Regular Objects Heated up
---

Here we have an example applying our proposed method on items that were left in the fridge for a few min. This creates the necessary temperature differential:

<img src="../../../../images/thermalwarm.png" align="center"/>

<br>


##  Humans or Animals
---

Finally mammals usually have a body temperature higher than the surroundings. In these settings our method can be applied naturally

<img src="../../../../images/thermal.png" align="center" />

<br>