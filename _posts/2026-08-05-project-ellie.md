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
# data_import Rev.2
# Import specific sheet from given link
journal_list <- read_sheet(
  gsheet_url, 
  sheet = "journals", 
  col_names = TRUE, 
  col_types = "icccccccccl", 
  na = "")
```

##### Stage 2: Testing Connection to Each Journal Archive URL

From my experience in learning cybersecurity, some websites may refuse to connect if the visitor is not human. In other words, since I was using automation tool using R language, websites will know that I was using a tool instead of visiting them myself as a human. Thus, I tested the connection to each URL using a custom configuration of the HTTP Headers. Most of the websites accepted browser user agent while a small portion of them did not. Those inaccessible from custom HTTP Header User-Agent were left for further testing and investigation.

```r
# test_conn Rev.2
archive_statuscode <- vector("integer")
archive_url <- vector("character")


user_agent <- "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0"

for (i in journal_list$archive){
  statuscode1 <- tryCatch({
    i |> 
      httr2::request() |> 
      httr2::req_error(is_error = \(resp) FALSE) |>
      httr2::req_headers(`User-Agent` = user_agent) |> 
      httr2::req_timeout(5) |> 
      httr2::req_perform() |> 
      httr2::resp_status()},
    error = function(e){
      print(glue::glue("Failed to fetch [ {i} ] due to {conditionMessage(e)}"))
      return(NA_integer_)
    })
  print(glue::glue("Testing connection to [ {i} ]: Status code {statuscode1}"))
  archive_statuscode[i] <- statuscode1
  archive_url[i] <- i
}

staging1_df <- tibble(archive_url, archive_statuscode)
```

The code above creates a new table namely `staging1_df`, which contains:

* `archive_url`: The URL to journal's archive webpage
* `archive_statuscode`: Connection test result (uses [HTTP Status Code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) convention)

##### Stage 3: Retrieving Issue URLs for Each Journal

Each journal has volumes and issues. They are usually paired to each other in a hierarchical way. One volume contains at least one issue. The relationship between the two are vertical hierarchy.

To retrieve the list of issue URLs, I fetched the whole webpage instead of targeting the URLs with CSS selector or XPATH. I chose this because the structure of each journals were different from one another, meaning that the structures were heterogeneous. As such, targeting the specific object while the object itself are contained in boxes of different names would impact render the engineering process inefficient. 

```r
# retrieve_issues Rev.2

# URLs as vector
archive_200_ok <- staging1_df %>%
  filter(archive_statuscode == 200) %>%
  select(archive_url) %>%
  pull()

# To store each page from journal archive URLs
staging2_list <- vector("list")

for (i in 1:length(archive_200_ok)) {
  print(glue::glue("Retrieving from: [ {archive_200_ok[i]} ]"))
  target_url <- archive_200_ok[i]
  
  # Parses the URL HTML page
  page <- 
    httr2::request(target_url) %>% 
    httr2::req_user_agent(user_agent) %>% 
    httr2::req_perform() %>% 
    httr2::resp_body_html() 
  
  elements <- page %>% rvest::html_elements("*")
  
  staging2_list[[i]] <- tibble(
    issues = elements %>% rvest::html_text(),
    issue_url = elements %>% rvest::html_attr("href")
  )
}
print(glue::glue("Raw HTML from each Issue URL for all journals has been saved."))
staging2_df <- bind_rows(staging2_list)
```

##### Stage 4: Cleaning The Issue URLs

The data from the retrieval process was unstructured. This calls for further cleaning.

```r
# Only retrieve rows with valid and appropriate text-URL pair
(staging3_df <- staging2_df %>%
    filter(!is.na(issue_url),
           str_detect(issue_url, "ac.id"),
           str_detect(issue_url, "issue/view")) %>%
    mutate(issues = str_remove_all(issues, "\\n")) %>%
    mutate(issues = str_remove_all(issues, "\\t")) %>%
    filter(issues != "")
)
```

##### Stage 5: Testing Connection to Each Issue URL

Since each issue is organized in a different directory (of the journal website), it is safe to assume that for each issue URL retrieved from the previous stage already represents each journal, and that no URL is duplicated both inside the journal and inter-journals.

However, it is considered good practice to investigate on the availability of each URL so that scrapping operation would not halted.

```r
issue_statuscode <- vector("integer")

for (i in 1:length(staging3_df$issue_url)){
  statuscode <- tryCatch({
    staging3_df$issue_url[i] %>%
    httr2::request() %>%
    httr2::req_headers(`User-Agent` = user_agent) %>%
    httr2::req_error(is_error = \(resp) FALSE) %>%
    httr2::req_timeout(5) %>%
    httr2::req_perform() %>%
    httr2::resp_status()
  }, 
  error = function(e){
    print(glue::glue("Network error on {staging3_df$issue_url[i]}: {conditionMessage(e)}"))
    return(NA_integer_)
  })
  # Logging progress
  print(glue::glue("Testing connection to URL [ {staging3_df$issue_url[i]} ] Status Code: {statuscode}"))
  # Append statuscode to vector
  issue_statuscode[i] <- statuscode
}
# Add the issue_statuscode vector into staging data frame for next stage
staging3_df$issue_statuscode <- issue_statuscode
```

##### Stage 7: Retrieving Article URLs from Each Issue URL

This stage has the same logic with the previous retrieval stage, the difference being the source URL. Looking at the resulting status code for each issue URL, there are some unreachable URLs. I have tried to access it manually, using Virtual Private Network (VPN), and the combination between the two, but to no avail. Therefore, I excluded the URLs with `NA` status code.

```r
# retrieve_article

# URLs as vector
issue_200_ok <- staging3_df %>%
  filter(issue_statuscode == 200) %>%
  select(issue_url) %>%
  pull()

# To store each page from journal issue URLs
staging4_list <- vector("list")

for (i in 1:length(issue_200_ok)) {
  print(glue::glue("Retrieving from: [ {issue_200_ok[i]} ]"))
  target_url <- issue_200_ok[i]
  
  # Parses the URL HTML page
  page <- 
    httr2::request(target_url) %>% 
    httr2::req_user_agent(user_agent) %>% 
    httr2::req_perform() %>% 
    httr2::resp_body_html() 
  
  elements <- page %>% rvest::html_elements("*")
  
  staging4_list[[i]] <- tibble(
    article_title = elements %>% rvest::html_text(),
    article_url = elements %>% rvest::html_attr("href")
  )
}
print(glue::glue("Raw HTML containing all articles from each issue URL for all journals has been saved."))
staging4_df <- bind_rows(staging4_list)
```

##### Stage 8: Cleaning the List of Article URLs

```r
staging5_df <- staging4_df %>%
  # Cleaning Regex and Whitespaces
  mutate(
    article_title = str_replace(article_title, "[\n\t]", ""),
    article_url = str_replace(article_url, "[\n\t]", "")) %>%
  mutate(
    article_title = str_squish(article_title),
    article_url = str_squish(article_url)) %>%
  
  # Adding a new column to count the n of char in article_title
  group_by(article_title) %>%
  mutate(article_title_strlen = str_length(article_title)) %>%
  ungroup() %>%
  
  # Exclude NULL from article_url and `0` from article_title_strlen
  filter(!is.na(article_url),
         article_title_strlen != 0)
```

```r
staging6_df <- staging5_df %>%
  #filter(!article_title %in% exc_not_article_explicit) %>%
  filter(str_detect(article_url, "article")) %>%
  filter(!str_detect(article_title, "^\\d")) %>%
  filter(!str_detect(article_title, regex("pdf|epub|html|front matter|back matter", ignore_case = TRUE)))
```

```r
# Preview
(staging6_df %>%
  group_by(article_url) %>%
  mutate(count_url = n()) %>%
  ungroup() %>%
  group_by(article_title) %>%
  mutate(count_title = n()) %>%
  ungroup() %>%
  arrange(desc(count_url)) %>%
  filter(count_url == 1) -> staging7_df)
View(staging7_df)
```

##### Stage X: Testing Connection to Each Article URLs

```r
article_statuscode <- vector("integer")

for (i in 1:length(staging7_df$article_url)){
  statuscode <- tryCatch({
    staging7_df$article_url[i] %>%
    httr2::request() %>%
    httr2::req_headers(`User-Agent` = user_agent) %>%
    httr2::req_error(is_error = \(resp) FALSE) %>%
    httr2::req_timeout(5) %>%
    httr2::req_perform() %>%
    httr2::resp_status()
  }, 
  error = function(e){
    print(glue::glue("Network error on {staging7_df$article_url[i]}: {conditionMessage(e)}"))
    return(NA_integer_)
  })
  # Logging progress
  print(glue::glue("Testing connection to URL [ {staging7_df$article_url[i]} ] Status Code: {statuscode}"))
  # Append statuscode to vector
  article_statuscode[i] <- statuscode
}
# Add the issue_statuscode vector into staging data frame for next stage
staging7_df$article_statuscode <- article_statuscode
```

##### Stage X1: Scrapping the Article Surface Metadata

```r
# Find nodes whose class contains `pattern` (case-insensitive).
# Drops nodes nested inside another matching node to avoid duplicate text.
class_nodes_outermost <- function(html, pattern) {
  cls <- "translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"
  xpath <- paste0(
    "//*[contains(", cls, ", '", pattern, "') and ",
    "not(ancestor::*[contains(", cls, ", '", pattern, "')])]"
  )
  rvest::html_nodes(html, xpath = xpath)
}

# Combine texts and child HTML from a node set into single strings.
combine_nodes <- function(nodes) {
  if (length(nodes) == 0) {
    return(list(text = NA_character_, html = NA_character_))
  }
  texts <- stringr::str_squish(iconv(
    rvest::html_text(nodes, trim = TRUE),
    from = "UTF-8", to = "UTF-8", sub = ""
  ))
  texts <- unique(texts[!is.na(texts) & nchar(texts) > 0])
  text <- if (length(texts) > 0) paste(texts, collapse = "\n") else NA_character_

  html_bits <- unlist(lapply(nodes, function(n) as.character(rvest::html_children(n))))
  html_combined <- if (length(html_bits) > 0) paste(html_bits, collapse = "\n") else NA_character_

  list(text = text, html = html_combined)
}


scrape_article_segmented <- function(url) {
  response <- tryCatch({
    httr::GET(
      url,
      httr::add_headers(`User-Agent` = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"),
      httr::timeout(10)
    )
  }, error = function(e) return(NULL))

  empty_payload <- list(
    title = tibble::tibble(url = as.character(url), title = NA_character_),
    authors = tibble::tibble(url = as.character(url), author = NA_character_),
    abstract = tibble::tibble(url = as.character(url), abstract_text = NA_character_, nested_html = NA_character_),
    keywords = tibble::tibble(url = as.character(url), keyword_text = NA_character_, nested_html = NA_character_),
    references = tibble::tibble(url = as.character(url), reference_list = NA_character_)
  )

  if (is.null(response) || httr::status_code(response) != 200) {
    return(empty_payload)
  }

  content_type <- httr::headers(response)[["content-type"]]
  if (!is.null(content_type) && grepl("application/pdf", content_type, ignore.case = TRUE)) {
    return(empty_payload)
  }

  html <- tryCatch(rvest::read_html(response), error = function(e) return(NULL))
  if (is.null(html)) return(empty_payload)

  # --- helpers -------------------------------------------------------------

  class_nodes_outermost <- function(doc, pattern) {
    cls <- "translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"
    xpath <- paste0(
      "//*[contains(", cls, ", '", pattern, "') and ",
      "not(ancestor::*[contains(", cls, ", '", pattern, "')])]"
    )
    rvest::html_nodes(doc, xpath = xpath)
  }

  safe_text <- function(nodes) {
    if (length(nodes) == 0 || inherits(nodes, "xml_missing")) return(NA_character_)
    txt <- tryCatch(rvest::html_text(nodes, trim = TRUE), error = function(e) NA_character_)
    txt <- iconv(txt, from = "UTF-8", to = "UTF-8", sub = "")
    txt <- stringr::str_squish(txt)
    txt <- unique(txt[!is.na(txt) & nchar(txt) > 0])
    if (length(txt) == 0) NA_character_ else paste(txt, collapse = "\n")
  }

  safe_html <- function(nodes) {
    if (length(nodes) == 0 || inherits(nodes, "xml_missing")) return(NA_character_)
    bits <- unlist(lapply(nodes, function(n) {
      if (inherits(n, "xml_missing")) return(character(0))
      kids <- tryCatch(rvest::html_children(n), error = function(e) NULL)
      if (is.null(kids) || length(kids) == 0) return(character(0))
      tryCatch(as.character(kids), error = function(e) character(0))
    }))
    if (length(bits) == 0) NA_character_ else paste(bits, collapse = "\n")
  }

  # --- 1. TITLE -----------------------------------------------------------
  title_node <- rvest::html_node(html, "head title")
  raw_title <- if (!inherits(title_node, "xml_missing") && length(title_node) > 0) {
    rvest::html_text(title_node, trim = TRUE)
  } else {
    NA_character_
  }
  clean_title <- if (!is.na(raw_title)) stringr::str_squish(iconv(raw_title, from = "UTF-8", to = "UTF-8", sub = "")) else NA_character_
  df_title <- tibble::tibble(
    url = as.character(url),
    title = if (!is.na(clean_title) && nchar(clean_title) > 0) clean_title else NA_character_
  )

  # --- 2. AUTHORS ---------------------------------------------------------
  author_nodes <- rvest::html_nodes(html, xpath = "//*[contains(translate(@class, 'AUTHOR', 'author'), 'author')]")
  raw_authors <- tryCatch(rvest::html_text(author_nodes, trim = TRUE), error = function(e) character(0))
  clean_authors <- iconv(raw_authors, from = "UTF-8", to = "UTF-8", sub = "")
  clean_authors <- stringr::str_squish(clean_authors)
  keep <- !is.na(clean_authors) & nchar(clean_authors) > 0
  clean_authors <- clean_authors[keep]

  df_authors <- if (length(clean_authors) > 0) {
    tibble::tibble(url = as.character(url), author = clean_authors)
  } else {
    tibble::tibble(url = as.character(url), author = NA_character_)
  }

  # --- 3. ABSTRACT (class contains "abstract") ----------------------------
  abstract_nodes <- class_nodes_outermost(html, "abstract")
  df_abstract <- tibble::tibble(
    url = as.character(url),
    abstract_text = safe_text(abstract_nodes),
    nested_html = safe_html(abstract_nodes)
  )

  # --- 4. KEYWORDS (class contains "keyword") -----------------------------
  keyword_nodes <- class_nodes_outermost(html, "keyword")
  df_keywords <- tibble::tibble(
    url = as.character(url),
    keyword_text = safe_text(keyword_nodes),
    nested_html = safe_html(keyword_nodes)
  )

  # --- 5. REFERENCES (class contains "reference" OR ul/ol with "reference") -
  ref_nodes <- class_nodes_outermost(html, "reference")

  lowtxt <- "translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"
  cls    <- "translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"

  ref_ul <- tryCatch(
    rvest::html_nodes(html, xpath = paste0("//ul[contains(", lowtxt, ", 'reference') and not(ancestor::*[contains(", cls, ", 'reference')])]")),
    error = function(e) rvest::html_nodes(html, xpath = "//none")
  )
  ref_ol <- tryCatch(
    rvest::html_nodes(html, xpath = paste0("//ol[contains(", lowtxt, ", 'reference') and not(ancestor::*[contains(", cls, ", 'reference')])]")),
    error = function(e) rvest::html_nodes(html, xpath = "//none")
  )

  ref_texts <- c(safe_text(ref_nodes), safe_text(ref_ul), safe_text(ref_ol))
  ref_texts <- ref_texts[!is.na(ref_texts)]
  ref_combined <- if (length(ref_texts) > 0) paste(ref_texts, collapse = "\n") else NA_character_

  df_references <- tibble::tibble(
    url = as.character(url),
    reference_list = ref_combined
  )

  return(list(
    title = df_title,
    authors = df_authors,
    abstract = df_abstract,
    keywords = df_keywords,
    references = df_references
  ))
}

urls <- staging7_df %>%
  select(article_url) %>%
  pull()

article_list <- scrape_urls_to_list(urls)
```

##### Stage X2: Scrapping Result

```r
article_list$titles %>%
  left_join(article_list$authors, by = "url") %>%
  left_join(article_list$abstracts, by = "url") %>%
  left_join(article_list$keywords, by = "url") %>%
  left_join(article_list$reference_lists, by = "url") %>%
  group_by(url) %>%
  mutate(count_url = n()) %>%
  ungroup() %>%
  arrange(desc(count_url)) -> dirty_articles

(missing_keywords <- sum(is.na(dirty_articles$keyword_text)))
(n_keywords <- length(dirty_articles$keyword_text))

dirty_articles %>%
  visdat::vis_miss() +
  ggthemes::theme_fivethirtyeight() +
  labs(title = "Missing data", subtitle = glue::glue("{missing_keywords} of {n_keywords} articles need further investigation")) +
  theme(axis.text.x = element_text(angle = 15, vjust = 1))
```

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