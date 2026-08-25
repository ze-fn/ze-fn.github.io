---
layout: distill
title: "Conducting Logistic Regression pt1"
description: "Learning from DataCamp's Car Insurance Claim Outcomes"
tags: [Statistics, Generalized Linear Regression, R, Data Science, English]
categories: [Portfolio]
date: 2026-06-16
authors:
  - name: Zelvy Fauzan
    affiliations:
     name: Independent Scientist
featured: false
mermaid:
  enabled: true
  zoomable: true
toc:
  - name: Introduction
  - name: The Dataset
  - name: How I Started
  - name: How I Ended up
giscus_comments: true
pretty_table: true
---

# Introduction

I have been learning "Introduction to Linear Regression" on DataCamp for a few days and today was the day I applied what I have learned. More specifically, I learned Simple Linear Regression and Simple Logistic Regression in R, and the project I was tasked was predicting Car Insurance Claim Outcomes. During the learning session, I have little concern about implementing what was taught; but it took a turn when it comes to applying to a project. 

The question for the project was simple:

> Using Logistic Regression models, what single feature has the best predictive performance for a car insurance claim ("outcome")?

# The Dataset

The table below shows the structure of the dataset that I was working with. I adapted it as is from the project's webpage.

| Column | Description |
|--------|-------------|
| `id` | Unique client identifier |
| `age` | Client's age: <br> <ul><li>`0`: 16-25</li><li>`1`: 26-39</li><li>`2`: 40-64</li><li>`3`: 65+</li></ul> |
| `driving_experience` | Years the client has been driving: <br> <ul><li>`0`: 0-9</li><li>`1`: 10-19</li><li>`2`: 20-29</li><li>`3`: 30+</li></ul> |
| `education` | Client's level of education: <br> <ul><li>`0`: No education</li><li>`1`: High school</li><li>`2`: University</li></ul> |
| `income` | Client's income level: <br> <ul><li>`0`: Poverty</li><li>`1`: Working class</li><li>`2`: Middle class</li><li>`3`: Upper class</li></ul> |
| `credit_score` | Client's credit score (between zero and one) |
| `vehicle_ownership` | Client's vehicle ownership status: <br><ul><li>`0`: Does not own their vehilce (paying off finance)</li><li>`1`: Owns their vehicle</li></ul> |
| `vehicle_year` | Year of vehicle registration: <br><ul><li>`0`: Before 2015</li><li>`1`: 2015 or later</li></ul> |
| `married` | Client's marital status: <br><ul><li>`0`: Not married</li><li>`1`: Married</li></ul> |
| `children` | Client's number of children |
| `postal_code` | Client's postal code | 
| `annual_mileage` | Number of miles driven by the client each year |
| `vehicle_type` | Type of car: <br> <ul><li>`0`: Sedan</li><li>`1`: Sports car</li></ul> |
| `speeding_violations` | Total number of speeding violations received by the client | 
| `duis` | Number of times the client has been caught driving under the influence of alcohol |
| `past_accidents` | Total number of previous accidents the client has been involved in |
| `outcome` | Whether the client made a claim on their car insurance (response variable): <br><ul><li>`0`: No claim</li><li>`1`: Made a claim</li></ul> |

# How I Started

My initial thought was to perform logistic regression on one variable, to see whether my code work well, and then creating a function which then looped in a for-loop operation. 

1. I started with performing `glm()` to model age vs outcome from the dataset while specifying binomial as the distribution.
2. Then, I created a tibble for the explanatory variabel (i.e., age).
3. I performed prediction on `outcome` given `age` based on the model I generated in the first step.
4. The prediction result on step 3 was stored in a variable `pred`.
5. Then, I tried to `mutate` a proportion (pred / (1-pred)) and store it in a new column.

However, I stucked at step 5.

After trying for quite some time, I gave up and looked on the solution instead. I decided to retrace the solution to get more insights.

# How I Ended up

As a disclaimer, I didn't follow the solution blindly or copy-pasted it as is. Instead, I tried to analyze and reason every line of code to understand the workflow to performing logistic regression. The following is the code I wrote (or rather, _imitated_).

```r
# Import library
library(readr)
library(dplyr)

# Import data
car_insurance <- read_csv("/car_insurance.csv")
```

```r
# Inspecting for NA values
car_insurance %>% 
  filter(if_any(everything(), is.na))
```

```r
# # Get all column name except `outcome` and `id`
features_chr <- car_insurance %>% 
  select(-id, -outcome) %>% 
  colnames()
# Store the features into a dataframe
features_df <- data.frame(features = features_chr)
```

In the retracing of the _solution_, I wrote a "For Loop logic" to evaluate and clarify how far I understood the workflow.

```markdown
### For Loop logic

1. Get `features` from dataset.
2. Store `features` into a dataframe variable.
3. Get `features` in a vector format to be used in the for-loop operation.

=== start loop from here ===

4. Generate GLM for each feature to `outcome`.
5. Run prediction and Store it in a vector.
6. Get proportion of prediction to actual and Store it to `accuracy` vector variable.
7. Update the respective feature (in `features_df`) with the value of `accuracy` variable.

=== end loop ===

8. See the final **features** dataframe.
9. Arrange descendingly on `accuracy` to see which feature best predict the `outcome`.
```


```r
# Load the glue package
library(glue)

# Initiate the for-loop operation
for (f in features_df$features){
	model <- glm(glue("outcome ~ {f}"), data = car_insurance, family = "binomial")
	pred <- round(fitted(model))
	accuracy <- length(which(pred == car_insurance$outcome)) / length(car_insurance$outcome)
	features_df[which(features_df$features == f), "accuracy"] = accuracy
}
```

This is where I question my basic skill in data wrangling in R. 

- I didn't know `glue()` can be used inside a for-loop.
- I haven't grasped what `fitted()` function do.
- I haven't undestood what and how `which()` function.
- I haven't revisited to what extent the `length()` function can be applied.
- I haven't accustomed to updating an existing dataframe using base R functions.

If I had to guess how each of the functions work, I would say:

The `glue()` function concatenates all the supplied arguments and engrave it into the code as if the concatenation was the user's input. In this case, the `glue("outcome ~ {f}")` takes whatever is in the for statement and then concatenates it into the code. So, if the first element of `f` inside the `features_df$features` (that is encased inside a for-loop statement) is `age`, it will appear to the machine: `glm(outcome ~ age, data = car_insurance, family = "binomial")`. And if the first iteration is complete, it loops the second element, and so on and so forth until the very last element in the list.

The `fitted()` function, I assume that this function simplifies the longer version of performing logistic regression for predictive statistics. So, in the `model` variable, we can access both the resulting model or the data that is being used to model the relationship. The `fitted()` function takes the explanatory variable inside the raw data and applies the resulted model into the existing response variable. We still have our raw data inside the `model` variable but we have our prediction result inside the `pred` variable. Nothing was lost. The `round()` function uses the _banker's rounding_ algorithm. So, inside the `pred` variable, we have our raw explanatory column and a predicted response column. It's the simplified procedure from the longer, manual one.

The `which()` function, I suspect, takes a conditional argument and returns the rows that satisfy the condition(s).

The `length()` function is different from that of `len()` in which case the former counts the number of existing rows while the latter counts the number of character in a string value. Nesting `which()` inside `length()` will returns the number of rows that satisfy the specified condition(s).

```r
# Print the dataframe
features_df
# Return the feature with highest accuracy
features_df %>% 
  arrange(desc(accuracy)) %>% 
  slice(1)
```