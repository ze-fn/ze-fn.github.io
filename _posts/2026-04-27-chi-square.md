---
layout: post
title: Chi-square
description: How we calculate categorical data is different to that of numerical data
tags: [Statistics, Hypotheis Testing, English]
categories: [Diary, Journal]
date: 2026-04-27
featured: false
mermaid:
  enabled: true
toc: 
  sidebar: false
authors:
  - name: Zelvy Fauzan
    url: https://ze-fn.github.io/
    affiliations:
      name: Independent
      url: https://github.com/ze-fn/
pretty_table: true
---

Monday, 27 April 2026. I have no teaching schedule on Monday. Longer weekend, yay!

I just finished my network engineering project yesterday so I want to keep progressing on my projects. I see that building a home server and home security would need some materials (second hand laptop, additional storage, CCTV, etc.) so I decided to continue my learning on Hypothesis Testing.

I continued my learning on Hypothesis Testing, specifically on the categorical data. I focused my study on Chi-square $ (\chi^2) $ test and so does this diary about. First off, I thought the Chi-square got its name from the fact that it usually investigates two variables of two distinct data. So, for example, the variable `gender` (which only has either male or female) and whether someone `joined club` or not (boolean: TRUE or FALSE, which can also be translated as either 1 or 0 of categoric: nominal data type) are cross-multiplied. If I had to illustrate it into a table. it would look like the following:

|            | Joined | Not Joined |
| :--------- | :----: | :--------: |
| Male       | 40     | 10         |
| Female     | 30     | 20         |

There would be `Male-Joined`, `Male-Not Joined`, `Female-Joined`, and `Female-Not Joined` pairs.

Now, one might wonder:

> _"Why don't we use T-Test for categorical data?"_

Good question! We simply cannot do arithmatics with categorical data. Let me explain it here. Suppose we want to find the _Average/Mean_ of a categorical data, say, of `smartphone brands`. One does not simply perform "mean" on those value. Can you find the "middle value" between these data (please, disregard their attributes such as aftersales quality, processor capability, or other attributes): Samsung, Apple, Xiaomi, Oppo, Tecno, and Motorola? No, you can't, can you? We cannot find the "middle grounds" between each smartphone brands. As such, we cannot use T-Tests on categorical data because T-Tests use calculations for numerical data types. It's just not compatible.

Back to the Chi-square, let's just see the formula for calculating the Chi-square. 

$$
\chi^2 = \sum \frac{(O - E)^2}{E}
$$

where:

$\chi^2$ : Chi-square

$O$ : Observed value

$E$ : Expected value

And that:

$$
E = \frac{(Row \space Total \times Column \space Total)}{Grand \space Total}
$$



So... let's plug it into the table, shall we?

|            | Joined | Not Joined |
| :--------- | :----: | :--------: |
| Male       | $ \frac{(O - E)^2}{E} $ | $ \frac{(O - E)^2}{E} $ |
| Female     | $ \frac{(O - E)^2}{E} $ | $ \frac{(O - E)^2}{E} $ |


And now for the $ E $ part, into the equation:


|            | Joined | Not Joined |
| :--------- | :----: | :--------: |
| Male       | $ \frac{\left(40 - \frac{(50 \times 70)}{100} \right)^2}{\frac{50 \times 70}{100}} $ | $ \frac{\left(10 - \frac{(50 \times 30)}{100} \right)^2}{\frac{50 \times 30}{100}} $ |
| Female     | $ \frac{\left(30 - \frac{(50 \times 70)}{100} \right)^2}{\frac{50 \times 70}{100}} $ | $ \frac{\left(20 - \frac{(50 \times 30)}{100} \right)^2}{\frac{50 \times 30}{100}} $ |


Let's do the calculation so that we can see what's happening clearly.


|            | Joined | Not Joined |
| :--------- | :----: | :--------: |
| Male       | $ \frac{(40 - 35)^2}{35} $ | $ \frac{(10 - 15)^2}{15} $ |
| Female     | $ \frac{(30 - 35)^2}{35} $ | $ \frac{(20 - 15)^2}{15} $ |


Now, we sum all of the cells up like the following:

$$
\chi^2 = \left(\frac{(40 - 35)^2}{35}\right) + \left(\frac{(10 - 15)^2}{15} \right) + \left(\frac{(30 - 35)^2}{35} \right) + \left(\frac{(20 - 15)^2}{15} \right)
$$

This will give us the Chi-square ($ \chi^2 $) statistic value.

There is also another important value, and yes you guessed it right, the $ p $-value.

> Insert explanation of where and how to get the p-value from the Chi-square formula

# Exercise

> CSV file pending upload. I will upload it ASAP.

As an effor to understand the Chi-square ($ \chi^2 $), I made my own exercise from the dataset that I collected myself. I have a dataset from my students. In short, this dataset of mine consist of 180 observations:

1. `local_id`: Student's ID from the school (this is different from the National Student ID)
2. `pres_num`: Student's index number relative to the class they are in; ordered by another unique ID from "DAPODIK"
3. `gender`: Student's sex
4. `class`: Student's class
5. `ad_dt1`: Student's answer for number 1 from exercise _"Data Analysis: Data Type I"_. Answer = {`k`, `d`, `n`, `o`, `NULL`}

I only exported the answer for question number 1 (out of 15) because what I was trying to prove is whether:

> Female students are more likely to turn-in their exercise than male students ($ H_A $)

So, I started my exercise on R and got the following result:

```r
library(tidyverse)
library(glue)

# Import the data
data_ad_dt1 <- read_delim("<file location>",    # Change this
                        delim = ';',
                        col_types = "cicffc")

# Assumption Check: Independency
data_ad_dt1 %>% 
  group_by(local_id) %>% 
  select(local_id) %>% 
  mutate(cnt = n()) %>% 
  filter(cnt != 1)
# Verdict on Independency assumption check: CLEAR

# Assumption Check: Simpson's Paradox
n_gender_per_class <- data_ad_dt1 %>% 
  group_by(class, gender) %>% 
  summarize(cnt = n())

n_student_per_class <- data_ad_dt1 %>% 
  group_by(class) %>% 
  summarize(nt_student = n())

n_gender_per_class %>% 
  left_join(n_student_per_class, by = "class") %>% 
  mutate(prop = cnt/nt_student)
# Verdict on Simpson's Paradox assumption check: CLEAR

# Data Transform: Add new col `status` to describe "turned-in" (1) and "not turned-in" (NA)
transform1 <- data_ad_dt1 %>% 
  mutate(status = if_else(is.na(ad_dt1), NA, 1)) %>% 
  mutate(status = factor(status)) %>% 
  select(gender, class, status)

# Data Transform: Contingency Table
transform2 <- transform1 %>%
  group_by(gender) %>%
  summarize(turned_in = sum(!is.na(status)),
            not_turned_in = sum(is.na(status)))

# Save as matrix with `gender` as rownames
h_test_matrix <- as.matrix(transform2[,2:3])
rownames(h_test_matrix) <- transform2$gender
h_test_matrix

# Run the Chi-square test
result_chisq <- chisq.test(h_test_matrix, correct = FALSE)
result_chisq

# Variables for each gender
female_submit_prop <- h_test_matrix[2,1]/sum(h_test_matrix[2,1:2])*100
male_submit_prop <- h_test_matrix[1,1]/sum(h_test_matrix[1,1:2])*100

# Chi-square value and p-value
result_chisq

# Directions for gender
result_chisq$stdres
```

Independent Chi-square test was performed to see the relationship between gender and submission ratio. The relationship between the two variables was significant. 

$$ \chi^2(1, N = 180) = 7.42 $$

$$ p = 0.006; \alpha = 0.05 $$

Females were significanly more likely to submit their exercises ($ 76.92 $ %) compared to males ($ 57.89 $ %)