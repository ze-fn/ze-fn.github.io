---
layout: post
title: "EE: Electricity"
description: Getting to Know Electricity
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

Few days ago, I tried to light up some LEDs but sometimes it lit up and sometimes it didn't. I got stuck. So, today, I tried some experiments. I wanted to understand how electricity flows.

## Before

I thought that all LEDs will light up as long as every LEDs are channeled to GND.

(insert image here)

## Experiment

I installed additional LEDs on the breadboard. Three were previously installed and 5 new ones.

Below is my circuit design for this experiments.

(insert illustation)

To understand how electricity flow, I tried to isolate different connections.

### First Experiment

LEDs: 25, 27, 29, 50
Positive: 50
Negative: 60
**Lit up: 50*

LEDs: 25, 27, 29, 50
Positive: 20
Negative: 60
**Lit up: None*

LEDs: 25, 27, 29, 50
Positive: 50
Negative: 20
**Lit up: None*

LEDs: 25, 27, 29, 50
Positive: 20
Negative: 20
**Lit up: 25, 27, 29*

> Temporary Conclusion:
> *Current flows from right to left?*

### Second Experiments

LEDs: 25, 27, 29, 50, 57
Positive: 50
Negative: 60
**Lit up: 50, 57*

LEDs: 25, 27, 29, 50, 57
Positive: 20
Negative: 60
**Lit up: None*

LEDs: 25, 27, 29, 50, 57
Positive: 50
Negative: 45
**Lit up: 50, 57*

LEDs: 25, 27, 29, 50, 57
Positive: 20
Negative: 45
**Lit up: None*

LEDs: 25, 27, 29, 50, 57
Positive: 57
Negative: 20
**Lit up: None*

LEDs: 25, 27, 29, 50, 57
Positive: 50
Negative: 20
**Lit up: None*

LEDs: 25, 27, 29, 50, 57
Positive: 45
Negative: 20
**Lit up: None*

LEDs: 25, 27, 29, 50, 57
Positive: 20
Negative: 20
**Lit up: 25, 27, 29*

### Third Experiments

LEDs: 25, 27, 29, 37, 50, 57
Positive: 57
Negative: 60
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 50
Negative: 60
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 37
Negative: 60
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 20
Negative: 60
**Lit up: None*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 50
Negative: 55
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 50
Negative: 45
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 50
Negative: 35
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 50
Negative: 26
**Lit up: None*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 50
Negative: 20
**Lit up: None*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 45
Negative: 60
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 45
Negative: 55
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 45
Negative: 45
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 45
Negative: 35
**Lit up: 37, 50, 57*

LEDs: 25, 27, 29, 37, 50, 57
Positive: 45
Negative: 26
**Lit up: None*

> Temporary Conclusion:
> Direction is not right to left, nor left to right.

### Fourth Experiments

When I was about to place moreLEDs, I saw that there is a gap on the rails' positive line.

(insert photo)

Just like that I realized that the gap is an indicator of separation. In other words, the breadboard is one but the current flow is divided into two parts. The two different current flows are separated by that gap.

So I tried connecting between the two separate rails with a jumper to see if all six LEDs will lit up.

LEDs: 25, 27, 29, 37, 50, 57
Positive: 60
Positive_Connection: 20, 35
Negative_Connection: 20, 35
Negative: 60
**Lit up: 25, 27, 29, 37, 50, 57*

## Conclusion

All LEDs will light up if every LEDs are connected to ground.

(insert two illustrations side by side)