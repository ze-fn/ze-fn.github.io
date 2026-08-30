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
  - name: Abstract
  - name: "Chapter 1: Introduction"
    subsections:
    - name: Background of the Study
    - name: Rationale of the Study
    - name: Problems of the Study
    - name: Aims of the Study
    - name: Contributions of the Study
  - name: "Chapter 2: Methodology"
    subsections: 
    - name: Study Design
    - name: Search Strategy
    - name: Study Selection and Eligibility
    - name: Data Extraction and Synthesis
  - name: "Chapter 3: Results and Findings"
    subsections:
    - name: TBA
  - name: "Chapter 4: Conclusions"
    subsections:
    - name: Conclusion
    - name: Limitations and Suggestions
    - name: Declaration of Competing Interest
  - name: Appendix

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

### Background of the Study

This is a personal project aimed to provide insights for researchers and English Language educators in seeing the bigger picture of how English is taught in Indonesia. In nature, one may consider this project as a meta-synthesis research. It collects, analyzes, and interprets articles from all around the internet. 

### Rationale of the Study

Learning and teaching practices is a personalized matter. Each individual has their own preferences. As such, while generalization is a good way to see the characteristics of the majority of the population, individual differences are not to be disregarded. 

Many factors have been believed to be the predictors of students learning outcome. This includes (but not limited only to) economic status, psychological condition, social relationship, age, sex, geography, and so on. With this in mind, this project is set out to capture those variables and plot them into a map. 

### Problems of the Study

To guide the project, I formulated some problems to be solved in this project. That way, I will not stray outside of the scope that I had set.

1. What is the most common teaching methodology to teach English as a Foreign Language in Indonesia over the years?
2. Which English teaching method has the most optimal effect size based on geographical location, age, and sex in each province of Indonesia?

### Aims of the Study

The current project was dedicated to answer the problems stated in the aforementioned section. As such, this project is aimed to:

1. provide a time-series graph that shows the most common teaching methodology to teach English as a Foreign Language in Indonesia, and
2. present a tabular data showing the teaching methods of English as a Foreign Language with the most optimal effect size based on geographical location, age, and sex in each province of Indonesia.

### Contributions of the Study

With the problems and aims at hand, I offered contribution in three dimensions:

* **Empirical contribution:** This project offered a curated list of scientific data from studies all around the internet that resonate with the concern of the current study. Researchers and practitioners may use the data collected in this study as a baseline for more in-depth analysis.
* **Practical contribution:** Teachers/educators and educational policy makers in Indonesia may use both the data and the interpretations from this study to make an informed decision regarding the development in the operational of education including (but not limited to) curriculum development, lesson planning, and policy and regulation making.
* **Theoretical contribution:** This project may add to the literature body of several fields including (but not restricted to) education, economy, urban planning and development, and language policy.

## Chapter 2: Methodology

In this chapter, I mapped out the strategy to achieve the current project's aims.

### Study Design

> **TBA**
>
> Meta-synthesis
{: .block-warning}

### Search Strategy

Manual record: Journal's Archive URL on SINTA 1-5, Scopus Q1-Q4

### Study Selection and Eligibility

#### Inclusion Criteria

* Research field: English Language Teaching
* Research geographical setting: Indonesia
* Research subject/participant: Indonesian
* Research methodology: Quantitative

#### Exclusion Criteria

* Research geographical setting: NOT Indonesia
* Research subject/participant: NOT Indonesian
* Research methodology: NOT Quantitative

### Data Extraction and Synthesis

This study applied concepts and practices from computer science field, specifically data engineering, data analysis, and data science. 

#### Database Design

This study adheres to the Level 1 and 2 of Database Normalization Form (1NF for final data frame and 2NF for data cleaning stage). The 1NF dictates data in each cell of column and row should be representing exactly one data (atomic value). The column (or often referred to as) "variables" or "feature" describes exactly one kind of meaning and data types. This, however, presents a very long list of observation (row number) data but this is intentional for further data processing in the data analysis stage.

The second normal form (2NF) in the data cleaning stage dictates that (1) 1NF must be achieved, and that (2) all non-key column must fully dependent on the entire primary key. This is perfect for multi-stage data collection process because it ensures minimal error in the data scrapping stage.

The following is the relational database diagram that shows the relationship among `staging` and `final data` frame.

> **TBA**
{: .block-warning}

#### Data Wrangling

This section covers both data scrapping and cleaning because the process is rather cyclical rather than a linear one.

##### Stage 0: Environment Preparation

The script I used was mainly in R language, and I used the libraries/packages in the `tidyverse` collection.

```r
req_packs <- c(
  "tidyverse", 
  "googlesheets4")

for (pack in req_packs) {
  if (!requireNamespace(pack, quietly = FALSE)) {
    install.packages(pack, dependencies = TRUE)
  }
  library(pack, character.only = TRUE)
}
```

Once the packages are installed, I imported the data of eligible journals. The link is open for public review.

```r
gsheet_url <- "https://docs.google.com/spreadsheets/d/1ReHFwLLCVOFLmOSEyyxD60DCepdVPC5jvuBJCbryDLM/edit?usp=sharing"
```

##### Stage 1: Getting The URLs for Eligible Journals

```r
# data_import Rev.1
# Import specific sheet from given link
journal_list <- read_sheet(
  gsheet_url, 
  sheet = "journals", 
  col_names = TRUE, 
  col_types = "icccccccccl", 
  na = "")
```

##### Stage 2: Testing Connection to Each Journal Archive URL

From my experience in learning cybersecurity, some websites my refuse to connect if the visitor is not human. In other words, since I was using automation tool using R language, websites will know that I was using a tool instead of visiting it myself as a human. Thus, I tested the connection to each URL.

```r
# test_conn Rev.1
j <- 0
for (i in journal_list$archive){
  j <- j + 1
  print(glue::glue("Iteration: {j}"))
  print(glue::glue("Testing connection to URL: {i}"))
  print(httr2::request(i) |> 
          #httr2::req_headers(`Host` = "google.com") |> 
          #httr2::req_headers(`Referrer` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded-For` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded` = "google.com") |> 
          #httr2::req_headers(`X-Original-URL` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded-For` = "google.com", `X-Forwarded` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded-For` = "google.com", `X-Forwarded` = "google.com", `Referrer` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded-For` = "google.com", `Referrer` = i) |>
          httr2::req_headers(`User-Agent` = c("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:134.0) Gecko/20100101 Firefox/134.0")) |> 
          httr2::req_perform() |> 
          httr2::resp_status())
}
```

As expected, two URLs refused to connect. Since I lack deep level of proficiency in computer networking and website infrastructure, I decided to exclude the ones refused to connect by creating a new column in the Google Sheet. If connection to website is NOT 200 OK, then bot_ok is populated with boolean values represented with `1` for `TRUE` and `0` for `FALSE`.

| bot_ok |
| :----: |
| TRUE   |
| TRUE   |
| FALSE  |
| ...    |

This presents a change in the initial database and revision as well as re-execution of the whole code is necessary.

##### Stage 3: Update Database Excluding URLs with 403 Code

```r
# data_import Rev.2
# Import specific sheet from given link
journal_list <- read_sheet(
  gsheet_url, 
  sheet = "journals", 
  col_names = TRUE, 
  col_types = "icccccccccll",   # Added `l` at the end representing the new col
  na = "")

# test_conn Rev.2
j <- 0
for (i in journal_list$archive[journal_list$bot_ok != FALSE]){
  j <- j + 1
  print(glue::glue("Iteration: {j}"))
  print(glue::glue("Testing connection to URL: {i}"))
  print(httr2::request(i) |> 
          #httr2::req_headers(`Host` = "google.com") |> 
          #httr2::req_headers(`Referrer` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded-For` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded` = "google.com") |> 
          #httr2::req_headers(`X-Original-URL` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded-For` = "google.com", `X-Forwarded` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded-For` = "google.com", `X-Forwarded` = "google.com", `Referrer` = "google.com") |> 
          #httr2::req_headers(`X-Forwarded-For` = "google.com", `Referrer` = i) |>
          httr2::req_headers(`User-Agent` = c("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:134.0) Gecko/20100101 Firefox/134.0")) |> 
          httr2::req_perform() |> 
          httr2::resp_status())
}
```

##### Stage 4: Retrieving Issue URLs for Each Journal

Each journal has volume and issue. They are usually paired to each other. 

I used a global coverage parsing of the fields that I needed. This was done because each journal structured their webpage differently despite using the same website template. As an illustration, journal X defines the issue links under the `<a>` HTML tag but journal Y and Z define the issue links under the `<div>` element of the month separator. This heterogeneity posed problem in the automation process. Therefore, I decided to cover the whole page instead, and cleaning them at a later stage.

```r
# Researcher's Note: Test SUCCESS. Production SUCCESS
ok_status_journals <- journal_list |> 
  filter(bot_ok != FALSE) |> 
  pull(archive)

# Binds the text and URL
prev_df <- tibble()
next_df <- tibble()
staging1_df <- tibble()

for (i in 1:length(ok_status_journals)){
  print(glue::glue("Retrieving from: ", ok_status_journals[i]))
  next_df <- bind_cols(
    issues = (
      # Take the text having "Vol"
      ok_status_journals[i] |> 
        rvest::read_html() |> 
        rvest::html_elements("*") |>
        rvest::html_text()
      ),
    # Take the URL having "Vol" in text
    issue_url = (
      ok_status_journals[i] |> 
        rvest::read_html() |> 
        rvest::html_elements("*") |> 
        rvest::html_attr('href'))
    )
  staging1_df <- bind_rows(staging1_df, next_df)
  prev_df <- next_df
}
print(glue::glue("All issue URL from journals saved.
                 Number of total HTML elements from all journal: {nrow(staging1_df)}"))
```

##### Stage 5: Cleaning The Issue URLs

The data from the retrieval process was unstructured. This calls for further cleaning.

```r
# Only retrieve rows with valid and appropriate text-URL pair
staging2_df <-
  staging1_df %>%
    filter(!is.na(issue_url),
           str_detect(issue_url, "ac.id"),
           str_detect(issue_url, "issue/view")
    ) %>%
    mutate(issues = str_remove_all(issues, "\\n")) %>%
    mutate(issues = str_remove_all(issues, "\\t")) %>%
    filter(issues != "")
```

##### Stage 6: Testing Connection to Each Issue URL

Since each issue is organized in a different directory (of the journal website), it is safe to assume that for each issue URL retrieved from the previous stage already represents each journal, and that no URL is duplicated both inside the journal and inter-journals.

However, it is considered good practice to investigate on the availability of each URL so that scrapping operation would not halted.

```r
issue_statuscode <- vector("integer", length(staging2_df$issue_url))

for (i in 1:length(staging2_df$issue_url)){
  statuscode <- tryCatch({
    staging2_df$issue_url[i] %>%
    httr2::request() %>%
    httr2::req_error(is_error = \(resp) FALSE) %>%
    httr2::req_perform() %>%
    httr2::resp_status()
  }, 
  error = function(e){
    print(glue::glue("Network error on {staging2_df$issue_url[i]}: {conditionMessage(e)}"))
    return(NA_integer_)
  })
  # Logging progress
  print(glue::glue("Testing URL [ ", staging2_df$issue_url[i], " ] Status Code: ", statuscode))
  # Append statuscode to vector
  issue_statuscode[i] <- statuscode
}
# Add the issue_statuscode vector into staging data frame for next stage
staging2_df$issue_statuscode <- issue_statuscode
```

##### Stage 7: Retrieving Article URLs from Each Issue URL

This stage has the same logic with the previous retrieval stage, the difference being the source URL. Looking at the resulting status code for each issue URL, there are some unreachable URLs. I have tried to access it manually, using Virtual Private Network (VPN), and the combination between the two, but to no avail. Therefore, I excluded the URLs with `NA` status code.

```r

```

> **TBA**
{: .block-warning}

#### Data Cleaning

Since the scrapping process was divided into several processes, each process produces separate related tables. As such, the tables are joined using one-to-many table join procedure.

> **TBA**
{: .block-warning}

### Chapter 3: Results and Findings

This chapter encloses the aggregation of the data frame. Each subsection is elaborated with data analysis and interpretation from the author.

> **TBA**
{: .block-warning}

### Chapter 4: Conclusions

#### Conclusion

> **TBA**
{: .block-warning}

#### Limitations and Suggestions

> **TBA**
{: .block-warning}

### Declaration of Competing Interest

None.

## Appendix

[Link to the source code of the web scrapping script]()

[Link to the list of journals' archive URLs](https://docs.google.com/spreadsheets/d/1ReHFwLLCVOFLmOSEyyxD60DCepdVPC5jvuBJCbryDLM/edit?usp=sharing)