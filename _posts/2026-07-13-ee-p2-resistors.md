---
layout: post
title: "EE: Resistors"
description: Getting to Know Resistors
tags: [Electrical Engineering, Electricity, Fundamental]
categories: [Learning]
date: 2026-07-13
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

This is the second experiment test on this day. I had resistors with different values: 220 Ohm, 1K Ohm, and 10K Ohm. I wonder what's the difference between the three.

## Hypothesis

{$$ H_0 $$}: There is no difference in light intensity between LEDs with 200 Ohm, 1K Ohm, and 10K Ohm

## Experiment

| LED_loc   | Resistor  |
| :-------- | :-------- |
| 4         | 10K       |
| 11        | 1K        |
| 15        | 200       |

## Result and Discussion

(Insert photo evidence)

It appears that LED on lane 4 (10K Ohm) is dim and LED on lane 15 (200 Ohm) is the brightest. LED on lane 11 (1K Ohm) lit with light intensity between the 10K Ohm and 200 Ohm. 

Delving on the linguistic side of the terminology, the word "resistor" comes from "resist" and suffix "-or". This means that resistor is a module that supress the amount of current flow. If the source current is {$$ X $$} Volt and is connected to a resistor with the amount of {$$ Y $$} Ohm, then the current (V) that already passed the resistor will be less than the original {$$ X $$} Volt. 

In other words, {$$ X_1 < X_0 $$}.

Cross-checking with Physics textbook, Current is expressed as {$$ I $$} with a unit of Ampere, Voltage is expressed as {$$ V $$} with a unit of Volt, and Resistance is expressed as {$$ R $$} with a unit of {$$ \Omega $$} Ohm. Together, to calculate the amount of current flowing is {$$ I = \frac{V}{R} $$}.

To prove this, I tried to do the math using python in Windows Command Prompt. I prefer terminal-style calculator instead of the Calculator App.

```py
>>> 5.5 / 220
0.025
>>> 5.5 / 1000
0.0055
>>> 5.5 / 10000
0.00055
```

## Conclusion

In general terms,

> The higher the resistor value is, the brighter the light intensity will be.

In scientific terms,

> The higher ther resistance is, the lower the current will be, which then resulted in lower output.