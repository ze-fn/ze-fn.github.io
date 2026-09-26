---
layout: distill
title: "5. Relational Databases"
description: "Assignment: Displaying Airport Data"
tags: [Data Science, Microsoft, Assignment]
category: [Learning]
date: 2026-09-26
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

This post is my assignment submission from Microsoft's Data Science for Beginners Repository. The assignment is about "Displaying Airport Data" using SQLite. As instructed, I'm using SQLite extension that is installed inside VSCode.

## Assignment

1. all city names in the Cities table
2. all cities in Ireland in the Cities table
3. all airport names with their city and country
4. all airports in London, United Kingdom

### Q1

```sql
SELECT city
FROM Cities;
```

### Q2

```sql
SELECT city
FROM Cities
WHERE country = 'Ireland'
```

### Q3

```sql
SELECT Airports.name, Cities.city, Cities.country
FROM Cities
RIGHT JOIN Airports
  ON Airports.city_id = Cities.city;
```

### Q4

```sql
SELECT name
FROM Airports
WHERE city_id = (SELECT id FROM Cities WHERE city = 'London');
```