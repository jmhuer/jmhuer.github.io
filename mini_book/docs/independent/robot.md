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

## Robot and Drone Collaboration and Automation

 <sub> <a href="https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html" style="color: red; text-decoration: underline;text-decoration-style: dotted;">← Back to Projects</a> </sub>

<img src="../../../../images/robotautonomy.jpg" align="center"/>

<br>

In this post I share my experience and a few applications of robots and drones for the indoor enviroment. I cover some of the steps required, and provide access to computer vision, and control software. Applications include robot arm and drone with computer vision deliver food to nearby user, robot loads a dishwasher, and robots following humans.
<br>


## A Simple Robot Arm
---

I worked directly on robotics in the
Emerging Technologies and Innovation group at GE. First we designed a few experiences using a simple
robot arm (Robotic xArm 6DOF). We added a camera and computer vision to allow the arm to reach
for food items.

<br>
 <div align="center">   <iframe width="560" height="315"
src="https://www.youtube.com/embed/opX3knb1254"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
></iframe></div>

<br>

The repositories used for this demostration can be found here:
- [Robot-Arm-](https://github.com/srinithish/Robotic-Hand-)
- [Comuter-vision-arm](https://github.com/srinithish/Smarttable)

<br>
<br>

## Add a Drone!
---

In addition, we did a proof of concept with the robot arm collaborating with a drone to
deliver small food items to a nearby user. Below is a demo:

<br>
 <div align="center">   <iframe width="560" height="315"
src="https://www.youtube.com/embed/tN8Z80PSc-M"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
></iframe></div>
<br>

The repositories used for this demostration can be found here:
- [autonomous-drone](https://github.com/jmhuer/DJITelloAutonomy2)

<br>
<br>


## A Better Robot Arm
---

Following the success of this project, the group invested in more sophisticated robot arms, and I
participated in creating experiences including, removing dishes from a dishwasher, making soup and
pizza, and loading a laundry machine with clothes. Below we have a video of our dishwasher example

<br>
 <div align="center">
  <iframe width="560" height="315"
src="https://www.youtube.com/embed/Nqcwmck2szk"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
></iframe></div>

<br>

Unfortunately, this repositary is GE confidential property.

<br>
<br>


## A Robot from Scratch
---

Finally, we worked closely with the [FirstBuild Microfactory](https://firstbuild.com/), to design a robot from scratch including selecting the motors, mounting and wiring batteries, and designing CAD frame with 80/20 t-slot materials that allow the user to attach different mechanisms for various applications. Additionally, a skid steer design allows for 360 turning inside the house in tight spaces and high payload capacity allows the robot to carry heavy weights without stalling torque. We add computer vision and load the drone to allow for collaboration

<br>
 <div align="center">
  <iframe width="560" height="315"
src="https://www.youtube.com/embed/bEvj1QQuPf4"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
></iframe></div>

<br>
<br>

















