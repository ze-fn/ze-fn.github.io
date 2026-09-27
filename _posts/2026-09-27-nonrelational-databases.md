---
layout: distill
title: "6. Nonrelational Databases"
description: "Assignment: Soda Profits"
tags: [Data Science, Microsoft, Assignment]
category: [Learning]
date: 2026-09-27
authors:
  - name: Zelvy Fauzan
    url: "https://ze-fn.github.io/"
    affiliations:
      name: Independent
featured: false
mermaid:
  enabled: true
  zoomable: true
code_diff: false
map: false
chart:
  chartjs: false
  echarts: false
  vega_lite: false
tikzjax: false
typograms: false

# bibliography: 
related_publications: false
giscuss_comments: true
---

## Introduction

This is a post about my assignment submission from Microsoft's Data Science for Beginner Repository. This assignment is about performing calculation on a dataset.

## Assignment

1. Calculate the Gross profits of FY '15, '16, '17, and '18
2. Calculate the average of all the gross profits (Sum of gross profits divided by number of fiscal years [10])

## Submission

### Q1

The formula for Gross Profit is `Net operating revenue` - `Cost of goods sold`. First, do for one column using the following formula:

```text
=I4-I5
```

Then, Autofill to the right side.


### Q2

Returning the Mean of Gross profit is straightforward. Sum all up then divide it by the count of numbers. It can be achieved quicker using the following formula:

```text
=AVERAGE(C6:L6)
```