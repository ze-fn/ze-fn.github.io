---
layout: post
title: "Python: Basic Conditional Statements"
description: A Simple Travel Weather Planner but with Diagrams
tags: [Software Engineering, Project, Python]
categories: [Learning]
date: 2026-07-17
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

Friday is the time for me to learn Data Science. Actually, I should be learning more about data science specifically.

I have some experiences with R for Data Science, but I faced some troubles when learning the machine learning part. My main source of learning was hard to follow so I decided to learn Python for Data Science instead, hoping to get a better explanation.

Python and R are different. I had to learn from scratch again. But even then, my main source of learning was also hard to follow despite the fact that I was just started.

I changed my learning source to [freeCodeCamp](https://freecodecamp.org/). The learning format was different but the materials were easy to follow. 

Then, I reached the "Lab" part. It is a part where I apply what I have learned and make a simple program.

There were many projects but this one is about conditional statements.

## Project: Travel Weather Planner

### Overview

The task was simple:

Write a simple program to decide whether commuting is possible based on the weather, distance to travel, and vehicle availability.

### Planning

At first, I jumped right into the terminal and wrote my program. But I found it difficult to wrote the program. There were too many to consider. My head got overheated.

Not long, I remembered that I had seen someone made a flowchart diagram for this kind of task.

So, I decided to draw a flowchart diagram di organize the conditions.

Once the diagram was done, I started writing the code.

Writing the program while looking at the flowchart was shockingly easier than jumping right to the text editor!

I spent excessive amount of time drawing the diagram, though, but it was worth it. See the diagram below.

(Insert dagram in svg)

As for the code, you can review it below.

```py
distance_mi = 54
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

if distance_mi == False:
    print('False')
elif distance_mi > 0 and distance_mi <= 1:
    if is_raining == True:
        print('False')
    else:
        print('True')
elif distance_mi > 1 and distance_mi <= 6:
    if is_raining == True:
        print('False')
    elif has_bike == True:
        print('True')
    else:
        print('False')
elif distance_mi > 6:
    if has_ride_share_app == True:
        print('True')
    elif has_car == True:
        print('True')
    else:
        print('False')
```

## Reflections

I found my workflow for writing a simple program:

> Diagram -> Code

And **not** straight to code.

This is subjective, I admit. But everyone has their own way of doing things, no?

Leave a comment if you find my experience entertaining! XD