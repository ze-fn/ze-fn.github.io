---
layout: post
title: "Microcontroller 2: Playing with Analog"
description: Exploring the analog and RGB modules
tags: [Arduino, Electrical Engineering, Project, C++]
categories: [Learning]
date: 2026-07-16
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

## Introduction

This is just a recreational project from Robonyx's lesson on Sonar Scanner Project. 

I made an analog controller to make an RGB light lit differently.

## Analog RGB Light Controller

The idea is simple. It's like a volume bar. If the volume bar reaches a certain range, the LED changes in color.

So, as the name suggests, an analog that controls the color of an RGB light.

To be specific ... 

If the "volume" is in range of 0 to 85, then the LED will be red.

If the "volume" is in range of 86 to 170, then the LED will be green.

And if the "volume" is in range of 171 to 255, then the LED will be blue.

Below is the code.

```cpp
// RGB LED
int redRGB = 6;
int greenRGB = 5;
int blueRGB = 3;

// Potentiometer 10K Ohm
int pot = A0;

int value;
int scale;

void setup() {
  // put your setup code here, to run once:
  pinMode(redRGB, OUTPUT);
  pinMode(greenRGB, OUTPUT);
  pinMode(blueRGB, OUTPUT);
  pinMode(pot, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  value = analogRead(pot);
  scale = map(value, 0, 1023, 0, 255);
  if (analogRead(scale) < 85) {
    digitalWrite(redRGB, HIGH);
    digitalWrite(greenRGB, LOW);
    digitalWrite(blueRGB, LOW);
    Serial.println(scale);
  } else if (analogRead(scale) >= 85 && analogRead(scale) <= 170) {
    digitalWrite(redRGB, LOW);
    digitalWrite(greenRGB, HIGH);
    digitalWrite(blueRGB, LOW);
    Serial.println(scale);
  } else {
    digitalWrite(redRGB, LOW);
    digitalWrite(greenRGB, LOW);
    digitalWrite(blueRGB, HIGH);
    Serial.println(scale);
  }
}
```

## Reflection

It worked but with some strange things happened.

As you can see on the video, it seemed like the range is not proportional.

It is as if the intervals are not equal. Green appears to be having the shortest of range, followed by red, and blue is the longest range.

I think I made a mistake, or I missed something to which I'm unaware of. 

If you found the bug, let me know in the comment section.