---
layout: distill
title: "Project: ELLIE"
description: "A Meta-Synthesis of papers about English Language Education in Indonesia"
tags: [Teaching Methodology, English as a Foreign Language, Indonesia]
category: [Research]
date: 2026-08-05
authors:
  - name: Zelvy Fauzan
    url: "https://ze-fn.github.io/"
    affiliations:
      name: Independent
toc:
  - name: "Abstract"
  - name: "Chapter 1: Introduction"
    subsections:
    - name: "1.1. Background of the Study"
    - name: "1.2. Rationale of the Study"
    - name: "1.3. Problems of the Study"
    - name: "1.4. Aims of the Study"
    - name: "1.5. Contributions of the Study"
  - name: "Chapter 2: Methodology"
    subsections: 
    - name: "2.1. Study Design"
    - name: "2.2. Search Strategy"
    - name: "2.3. Study Selection and Eligibility"
    - name: "2.4. Data Extraction and Synthesis"
  - name: "Chapter 3: Results and Findings"
    subsections:
    - name: "TBA"
  - name: "Chapter 4: Conclusions"
    subsections:
    - name: "4.1. Conclusion"
    - name: "4.2. Limitations and Suggestions"
    - name: "4.3. Declaration of Competing Interest"
  - name: "Appendix"

featured: true
mermaid:
  enabled: true
  zoomable: true
code_diff: false
map: false
chart:
  chartjs: true
  echarts: true
  vega_lite: false
tikzjax: false
typograms: false

# bibliography: 
related_publications: false
giscuss_comments: true
---

{% details Development Progress %}

0. 
0. 2026-08-29: Some links returned 403 Forbidden. (User-Agent tested, err persisted)
0. 2026-08-28: [Pseudocode for web scrapping](https://ze-fn.github.io/blog/2026/pseudocode-to-retrieve-vol-and-issue/)
0. 2026-08-27: Initial draft of research report

{% enddetails %}

## Abstract

_To be added_

## Chapter 1: Introduction

This chapter elaborates on the foundations, the motivations, the direction, and the contributions of the study.

### 1.1. Background of the Study

This is a personal project aimed to provide insights for researchers and English Language educators in seeing the bigger picture of how English is taught in Indonesia. In nature, one may consider this project as a meta-synthesis research. It collects, analyzes, and interprets articles from all around the internet. 

### 1.2. Rationale of the Study

Learning and teaching practices is a personalized matter. Each individual has their own preferences. As such, while generalization is a good way to see the characteristics of the majority of the population, individual differences are not to be disregarded. 

Many factors have been believed to be the predictors of students learning outcome. This includes (but not limited only to) economic status, psychological condition, social relationship, age, sex, geography, and so on. With this in mind, this project is set out to capture those variables and plot them into a map. 

### 1.3. Problems of the Study

To guide the project, I formulated some problems to be solved in this project. That way, I will not stray outside of the scope that I had set.

1. What is the most common teaching methodology to teach English as a Foreign Language in Indonesia over the years?
2. Which English teaching method has the most optimal effect size based on geographical location, age, and sex in each province of Indonesia?

### 1.4. Aims of the Study

The current project was dedicated to answer the problems stated in the aforementioned section. As such, this project is aimed to:

1. provide a time-series graph that shows the most common teaching methodology to teach English as a Foreign Language in Indonesia, and
2. present a tabular data showing the teaching methods of English as a Foreign Language with the most optimal effect size based on geographical location, age, and sex in each province of Indonesia.

### 1.5. Contributions of the Study

With the problems and aims at hand, I offered contribution in three dimensions:

* **Empirical contribution:** This project offered a curated list of scientific data from studies all around the internet that resonate with the concern of the current study. Researchers and practitioners may use the data collected in this study as a baseline for more in-depth analysis.
* **Practical contribution:** Teachers/educators and educational policy makers in Indonesia may use both the data and the interpretations from this study to make an informed decision regarding the development in the operational of education including (but not limited to) curriculum development, lesson planning, and policy and regulation making.
* **Theoretical contribution:** This project may add to the literature body of several fields including (but not restricted to) education, economy, urban planning and development, and language policy.

## Chapter 2: Methodology

In this chapter, I mapped out the strategy to achieve the current project's aims.

### 2.1. Study Design

> **TBA**
>
> Meta-synthesis
{: .block-warning}

### 2.2. Search Strategy

Manual record: Journal's Archive URL on SINTA 1-5, Scopus Q1-Q4

### 2.3. Study Selection and Eligibility

#### Inclusion Criteria

* Research field: English Language Teaching
* Research geographical setting: Indonesia
* Research subject/participant: Indonesian
* Research methodology: Quantitative

#### Exclusion Criteria

* Research geographical setting: NOT Indonesia
* Research subject/participant: NOT Indonesian
* Research methodology: NOT Quantitative

### 2.4. Data Extraction and Synthesis

This study applied concepts and practices from computer science field, specifically data engineering, data analysis, and data science. 

#### Database Design

This study adheres to the Level 1 and 2 of Database Normalization Form (1NF for final data frame and 2NF for data cleaning stage). The 1NF dictates data in each cell of column and row should be representing exactly one data (atomic value). The column (or often referred to as) "variables" or "feature" describes exactly one kind of meaning and data types. This, however, presents a very long list of observation (row number) data but this is intentional for further data processing in the data analysis stage.

The second normal form (2NF) in the data cleaning stage dictates that (1) 1NF must be achieved, and that (2) all non-key column must fully dependent on the entire primary key. This is perfect for multi-stage data collection process because it ensures minimal error in the data scrapping stage.

The following is the relational database diagram that shows the relationship among `staging` and `final data` frame.

> **TBA**
{: .block-warning}

#### Script

> **TBA**
{: .block-warning}

#### Data Cleaning

Since the scrapping process was divided into several processes, each process produces separate related tables. As such, the tables are joined using one-to-many table join procedure.

> **TBA**
{: .block-warning}

### 3. Chapter 3: Results and Findings

This chapter encloses the aggregation of the data frame. Each subsection is elaborated with data analysis and interpretation from the author.

> **TBA**
{: .block-warning}

### 4. Chapter 4: Conclusions

#### 4.1. Conclusion

> **TBA**
{: .block-warning}

#### 4.2. Limitations and Suggestions

> **TBA**
{: .block-warning}

### 4.3. Declaration of Competing Interest

None.

## Appendix

[Link to the source code of the web scrapping script]()

[Link to the list of journals' archive URLs](https://docs.google.com/spreadsheets/d/1ReHFwLLCVOFLmOSEyyxD60DCepdVPC5jvuBJCbryDLM/edit?usp=sharing)