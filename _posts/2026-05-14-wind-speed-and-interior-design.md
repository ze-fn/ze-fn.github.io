---
layout: distill
title: "Comparative Anemometric Analysis of Room Ventilation"
description: "My legs were constantly sweating because there is little to no wind flowing underneath my desk, so I tried to scientifically prove it"
tags: [Wind Speed, Interior Design, Data Science, English]
categories: [Portfolio]
date: 2026-05-14
authors:
  - name: Zelvy Fauzan
    affiliations:
     name: Independent
featured: false
mermaid:
  enabled: true
  zoomable: true
toc:
  - name: Introduction
    subsections:
    - name: Hypothesis
  - name: Methodology
    subsections:
    - name: Measurement Tools
    - name: Data Collection
    - name: Script for Data Extraction
    - name: Database Design
    - name: Data Analysis
    - name: Research Timeline
  - name: Result and Discussion
    subsections:
    - name: Wind Speed at AN1
    - name: Wind Speed at AN2
  - name: Conclusion
    subsections:
    - name: Implication
    - name: Limitations
    - name: Suggestions
---

> ## **NOTICE**
> 
> This study is ongoing.
>
> last updated: 2026-05-14
{: .block-warning}

# Introduction

It has been some weeks since this dry season arrived. Just by sitting still in my room made me sweaty all over my body. Three windows were opened but no air were flowing through below my desk. 

Frustrated by this, I wanted to prove that there is a difference of average wind speed underneath my desk and the other area inside my room.

## Hypothesis

**Null Hypothesis:** There is no difference in average wind speed among two locations (AN1: undeneath desk; AN2: another location inside the room). 

$$H_0: \mu_{AN1} = \mu_{AN2}$$

**Alternative Hypothesis:** Average wind speed at location AN2 (another location inside the room) is higher than the average wind speed at AN1 (underneath the desk) 

$$H_A: \mu_{AN2} > \mu_{AN1}$$

# Methodology

In this section, I map out the measurement tools, data collection method, data extraction, database design, data analysis method, and timeline of the observation.

## Measurement Tools

At first, I used a rather primitive measurement tools to observe the wind speed that flow through underneath my desk and the other area of my room. They were: ruler, a thread, and a $3 \space cm \times 14 \space cm$ paper. But when I set out to observe the change in wind speed, the observation was highly subjective. Therefore, I used a more robust methods to measurement and data collection. Enclosed below is the measurement tools I usde.

| Tool | Quantity |
| :--- | :------: |
| Anemometer | 2 |
| Tripod | 2 |
| Smartphone (as video recording) | 1 |

## Data Collection

The data were collected from two anemometers located at two different coordinates (see figure below). The observation duration was set to 1 hour with an interval of 1 hour rest. Both anemometers were video recorded for later documentation. Once the observation period was over, each video recording was further recorded using a python script to automate data entry process.

## Script for Data Extraction

As the time of writing this report, the research was still in its infancy stage. Therefore, the script for data extraction process was also still in development stage. Below is a flowchart that illustrates how the data extraction would run.


(Present as flowchart diagram)
_Video -> stacked rect: frames -> random sampling: frame (n = 1) -> define limit for scan -> identify numbers (return point) -> store numbers in temp variable (n = 30 fps = 1 sec) -> aggregate temp var (mean) -> store aggregated value in persistent variable as vector -> back to "return point"_

```python
# This space is reserved for python script: Video to CSV Data Extraction
```

## Database Design

The anemometer was treated as groups. Therefore, there are two groups: AN1 and AN2. Alongside the two groups was wind speed data, stored in a variable/column called `wspeed`. In addition, date time variable was also added to the database (1 second interval) to which it was stored in a POSIXct format.

| Variable              | Description                                               | Data Type       |
| :-------------------- | :-------------------------------------------------------- | :-------------- |
| `group`               | Anemometer (AN1, AN2).                                    | `nominal`       |
| `wspeed`              | Wind speed value from observation.                        | `continuous`    |
| `datetime`            | Date and time of the recorded `wspeed` (format: POSIXct). | `datetime`      |

## Data Analysis

The initial aim of this mini study was to see whether there is a difference in average wind speed at two different locations inside my room. Prior to performing a hypothesis test whether there is any difference in central measure of the wind speed among two groups, assumption checks for variable `group` and `wspeed`were conducted to determine the appropriate formal statistical inference test.

## Research Timeline

(Insert gantt chart using Mermaid.js)

# Result and Discussion

This part narrates the results of the data analysis, sectioned by each group in the `group` variable.

## Wind Speed at AN1

_(Content: TBA)_

## Wind Speed at AN2

_(Content: TBA)_

# Conclusion
 
_(Content: TBA)_

## Implication

_(Content: TBA)_

## Limitations

_(Content: TBA)_

## Suggestions

_(Content: TBA)_
