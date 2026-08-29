---
layout: post
title: "Project ELLIE: Pseudocode for Retrieving Volume, Issue, and Issue URL"
description: One of the parts of project ELLIE
tags: [Web Scrapping, R, rvest package]
categories: [Portfolio]
date: 2026-08-28
featured: false
mermaid:
  enabled: true
  zoomable: true
tabs: true
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

This article focuses on designing the logic behind _"harvesting"_ the data for Project ELLIE. 

Project ELLIE is an open-source meta-analysis research project specific to scientific articles discussing English Language Education. The main goal is to provide an "at a glance" insight of current developments in English teaching. As of the time of this writing, the current geographical scope is limited to studies in Indonesia. Development of this project may expand to a global coverage.

## Methodology

Instead of looking and recording data from articles all around the internet (which would take a lifetime), why not use automation instead? They are way faster and programmable. That was what I was thinking. This is achievable with the power of coding.

In this project, I use R programming language to _"harvest"_ the articles' metadata.

The underlying principles are:

* HTML (Hypertext Markup Language) structure,
* CSS (Cascading Style Sheet) class selector,
* XML (Extensible Markup Language) Path (usually referred as: XPATH),
* HTTP Requests (GET request), and
* Database Normalization (N1)

## Algorithm

Below is the procedure (or IT practitioners usually address it as: algorithm) for scrapping the data, served in pseudocode. Pseudocode is a human-friendly and -redable format to explain computing processes.

1. Search for journals of interest.
2. Store the link of each journal in a column `journal_url`.
3. Add a new column `journal_name` beside the `journal_url`.
4. In each journal's website, look for the "Archive" menu and take the link (URL).
5. Store the Archive URL into its respective journal in a column named `j_archive_url`.
6. For each link in `j_archive_url`, retrieve the HTML element that contains the word: `"Vol%"` (percent sign represents a wildcard, meaning look for words that starts with "Vol." and whatever comes after it).
    6.1. For each detected HTML element, take the entire text of the HTML element that starts with "Vol." and store it into a column called `vol-issue`.
    6.2. For each detected HTML element, take the href attribute of the HTML element that has its text starts with "Vol." and store it into a column called `issue_url`.
7. For each link in `issue_url`, set scrapping boundaries to `article` HTML tag.
8. Inside each link in `issue_url` with boundaries set to `article`, take the CSS element having class name resembles "title" and store the text content as `article_title`.
9. Inside each link in `issue_url` with boundaries set to `article`, take the CSS element having class name resembles "author" and store the text content as `article_authors`.
10. Inside each link in `issue_url` with boundaries set to `article`, take the CSS element having class name resembles "doi" and store the text content as `article_doi`.
11. Inside each link in `issue_url` with boundaries set to `article`, take the CSS element having class name resembles "pdf" and store the text content as `article_link`.
12. Inside each link in `issue_url` with boundaries set to `article`, take the CSS element having class name resembles "page" and store the text content as `article_pages`.
13. For each link in `article_link`, take the CSS element having class name resembles "abstract" and store the text content as `article_abstract`.
14. For each link in `article_link`, take the CSS element having class name resembles "keywords" and store the text content as `article_keywords`.
15. For each link in `article_link`, take the CSS element having class name resembles "reference" and store the text content as `article_references`.

## 

## Script Prototyping

This section presents the script (code/program) in R language to execute the algorithm. For development purposes, I took a sample of journal at random. Then, I wrote the script and ran it. If the result of this web scrape is good, proceed to the next stage of data analysis (data wrangling).

{% tabs scripts %}

{% tab scripts R %}

```r
# Library/package requirement
req_packs <- c("tidyverse", "googlesheets4")

for (pack in req_packs) {
  if (!requireNamespace(pack, quietly = FALSE)) {
    install.packages(pack, dependencies = TRUE)
  }
  library(pack, character.only = TRUE)
}

# Import data from Google Sheets
sheet_url <- "https://docs.google.com/spreadsheets/d/1ReHFwLLCVOFLmOSEyyxD60DCepdVPC5jvuBJCbryDLM/edit?usp=sharing"
```

{% endtab %}

{% tab scripts Python %}

Coming Soon...

{% endtab %}

{% endtabs %}