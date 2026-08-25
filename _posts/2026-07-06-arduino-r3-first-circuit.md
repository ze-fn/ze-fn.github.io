---
layout: post
title: Traffic Lights in Arduino Uno R3
description: Some of my first circuits
tags: [Arduino, Electrical Engineering, Project]
categories: [Learning]
date: 2026-07-06
featured: false
mermaid:
  enabled: true
  zoomable: true

authors:
  - name: Zelvy Fauzan
    url: https://ze-fn.github.io/
    affiliations:
      name: Independent
      url: https://github.com/ze-fn/

toc:
  sidebar: true

images:
  compare: true
  slider: true

pretty_table: true

giscus_comments: true
---

# 1. Introduction

The day before Monday, 6 July 2026, I saw [Felix Siauw's thumbnail video](https://www.youtube.com/watch?v=fiVFbw2czZc) that says "Selesai Lebih Baik Daripada Sempurna". The text literally translates to "Done is better than perfect". It strucked me! I always filling up my bucket list but I hardly emptied (done) it. One item in my bucket list is to become an Electrical Engineer in Radio Frequency and Microwave using Microcontroller. Long stroy short, I continued my study from Robonyx's free course and below is what I learned and the project that I had done from the first chapter of [Starter Course for Arduino](https://www.skool.com/robonyx/about) course.

# 2. What I Learned

Electricity has been a tough one for me. Last year, I tried to make my own circuit design using breadboard but it didn't go well. I managed to make a blinking LED. But when I stepped up to making a simple traffic light circuit design, the output wasn't expected. Only one of the lights were lit. Below is my old design and the script.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/arduino_projects/proj1-100.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

{% details Script %}
```cpp
const int greenLED = 12;        //the code will flash the LED connected to pin 12
const int yellowLED = 11;       //the yellow LED is connected to digital pin 11
const int redLED = 10;          //the red LED is connected to digital pin 10

void setup() {
  pinMode(greenLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(redLED, OUTPUT);
}

void loop() {
  digitalWrite(redLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(greenLED, HIGH);
  delay(3000);
  digitalWrite(greenLED, LOW);
  digitalWrite(redLED, LOW);
  digitalWrite(yellowLED, HIGH);
  delay(1000);
  digitalWrite(greenLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(redLED, HIGH);
  delay(3000);
}
```
{% enddetails %}

## 2.1. Where to Where: Electric Current Flow

- Electricity moves from Positive to Negative.
- Positive is Anode; Negative is Cathode.
- Anode is (+); Cathode is (-).
- Long pin is Anode; Short pin is Cathode.
- (+) has more lines; (-) has only 1 line.
- Thus, Anode (+) is long pin, Cathode (-) is short pin.

## 2.2. Resistor

From "Resis" with suffix "-or", which means _something that is resisting (something else)_. In this case, if an LED is supplied with unresisted current (e.g., 5 Volts), the LED will burn and then will no longer be used. Resistors keep the LED (or other stuffs) not burn by "resisting" some amount (indicated by Ohm) of the electricity current. Thus, we rescued the LED from burning to crisp! And the LED is happy. Just look at how bright it is.

## 2.3. Ground

Ground is the place where we expel residual electricity. Let's say we want to lit an LED but forgot to connect the cathode of the LED to Ground (GND). The LED won't lit because the electricity is not flowing. To make electricity flow, we must connect the series to the Ground (GND). It has to make a perfect loop. From source (positive), to LED, then to ground (negative). Only by that the current can flow. Else, it won't flow at all and LED won't lit.

# 3. Project from Course

I copied what Hugh (Robonyx) did in the course but with different pin locations.

This is my first attempt, which looked nice! Everything went well.

(circuit design img goes here)

{ % details Script %}
```cpp
void setup() {
    pinMode(8, OUTPUT);
}

void loop() {
    digitalWrite(8, HIGH);
    delay(1000);
    digitalWrite(8, LOW);
    delay(1000);
}
```
{ % enddetails % }

## 3.1. Challenge

So I decided to challenge myself and redo the traffic light circuit design using a new script (see below). Since there were three lights, which means that three sources need to go to the GND, I plugged them all into the negative side of the breadboard and connect a jumper wire from the negative side into the GND on the R3. It didn't go well. Only the red LED went lit. So I tried to collect all of the cathode into one row and then connect the row into the GND on the R3. It went well!

(img with caption: Awesome!)

{ % details Script% }
```cpp
void setup() {
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(6, OUTPUT);
}

void loop() {
  digitalWrite(2, HIGH);
  delay(5000);
  digitalWrite(2, LOW);
  digitalWrite(4, HIGH);
  delay(1000);
  digitalWrite(4, LOW);
  digitalWrite(6, HIGH);
  delay(5000);
  digitalWrite(6, LOW);
}
```
{ % enddetails % }

Really happy with the results!

# 4. What's Next?

I'm continuing my study into Electrical Engineering using Microcontrollers. This is actually a part of my contingency plan for the unpredictable future. Next up is: [Reaction Speed Game](#).