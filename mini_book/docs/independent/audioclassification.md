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

# Sound Activity Recognition and Annomaly detection

 <sub> <a href="https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html" style="color: red; text-decoration: underline;text-decoration-style: dotted;">← Back to Projects</a> </sub>

<img src="../../../../images/audio.png" align="center"/>

<br>

 In this post I will explore a few approaches and applications of sound classification. We use both a standard appraoch using spectrograms + CNNs and a more sophisticated approach using transformers on spectrogram patches. We are testing two different methods:
 - Spectogram + CNN (pre-trained AlexNet). Here is the repository: https://github.com/jmhuer/specCNN_sound_classification
 - Spectogram + Transformer (16x16 image patches). Here is the repository: https://github.com/jmhuer/spectogram_transformer

<br>

## Activity Recognition with Spectrogram Transformer
---

In addition, we did a proof of concept of a system that can detect what kind of activities are going on in a room and change color of a light automatically

<br>
 <div align="center">   <iframe width="560" height="315"
src="https://www.youtube.com/embed/snkbodqne9o"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
></iframe></div>

<br>
<br>

## Laugh Detection + Philips Hue Bulb
---

Using AudioSet data we train a laugh detection sound classification and interpret the output for the laugh class as an intensity measure [0,1] to control the intensity of a philips hue bulb

<br>
 <div align="center">   <iframe width="560" height="315"
src="https://www.youtube.com/embed/bOG9VGZbTj8"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
></iframe></div>

<br>
<br>

## Service Diagnostics Running iOS CoreML
---

In addition, we did a proof of concept with the robot arm collaborating with a drone to
deliver small food items to a nearby user
There are many applications such as:

<br>
 <div align="center">   <iframe width="560" height="315"
src="https://www.youtube.com/embed/eoMQt4muwW4"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
></iframe></div>



<br>
<br>


