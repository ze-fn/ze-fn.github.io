---
layout: post
title: Questioning My Comprehension about Hypothesis Testing
description: I'm sure this isn't an Impostor Syndrome!
tags: [Statistics, Hypotheis Testing, English]
categories: [Diary, Journal]
date: 2026-04-24
featured: false
toc: 
  sidebar: true
authors:
  - name: Zelvy Fauzan
    url: https://ze-fn.github.io/
    affiliations:
      name: Independent
      url: https://github.com/ze-fn/
---

# Thoughts

Today, I wanted to advance in my learning on becoming a Data Scientist through Datacamp's [Associate Data Science Career Track](https://app.datacamp.com/learn/career-tracks/associate-data-scientist-in-r) but I was distracted by other things. One of them was whether I understand Hypothesis Testing.

At first, I continued my learning progress on [Intermediate R](https://app.datacamp.com/learn/courses/intermediate-r) and focused on how to write custom functions, use `lapply()` and `sapply()` to execute functions. A function to execute other function(s). **_Funct-ception!_** But then, at the middle of my learning session, I remembered that I haven't practiced what I have learned in the Hypothesis Testing part of the [Data Analyst in R](https://app.datacamp.com/learn/career-tracks/data-analyst-with-r) Career Track. So, I paused my learning on the Intermediate R and switched to exercise.

When I opened my project, I was petrified. I couldn't figure out what to do to perform hypothesis testing. My mind was blocked as if a mist filled my thoughts. _"What do I do?"_

I reviewed my project. I reread what I had written. 

Little by little, I regained what I was trying to achieve from working on this project. I wanted to find out whether Group A has higher mean score than Group B. But then I stumbled upon another question: 
> _"So, how do I find it out? Surely, I can do it by just aggregating the variable from the whole dataset since I have a dataset of the full population, but that wouldn't be always available in the future. So I have to use this hypothesis testing of a sample of a population."_

I spent an hour figuring this out. I avoided using AI like Gemini or ChatGPT because I want to figure it out myself. But then I gave up. In the end, I asked Gemini for an assistance. However, instead of making progress on the working project, I ended up asking Gemini to train me in performing hypothesis tests. Guess what? My head was overloaded. The exercises were simple enough (see below excerpt) but it took a toll on my head! Even for a very basic hypothesis test, I took 15 minutes completing that! What a shame!

<details>
    <summary>See chat</summary>
    <p>Don't be too hard on yourself! Hypothesis testing is one of those concepts that feels intuitive until you're staring at a p-value and a messy dataset. It’s a bit like learning to drive—you can read the manual all day, but you don't really "get it" until you're behind the wheel.</p>

    <p>In R, the syntax is often straightforward, but the <strong>setup</strong> (knowing which test to use and why) is where the real skill lies. Here are three challenges ranging from "warm-up" to "real-world" to help you sharpen those skills.</p>

    <hr>

    <h2>Challenge 1: The "Classic" Two-Sample T-Test</h2>
    <p><strong>Scenario:</strong> You are analyzing the fuel efficiency of two types of cars: 4-cylinder and 6-cylinder. You want to know if there is a statistically significant difference in their miles per gallon (mpg).</p>
    
    <ul>
        <li><strong>Dataset:</strong> Use the built-in <code>mtcars</code> dataset.</li>
        <li><strong>Tasks:</strong>
            <ol>
                <li>Filter the data to include only 4 and 6 cylinder cars (<code>cyl</code>).</li>
                <li>Check the assumption of normality for both groups using a Shapiro-Wilk test (<code>shapiro.test</code>).</li>
                <li>Perform an <strong>Independent Two-Sample T-Test</strong> to see if <code>mpg</code> differs by <code>cyl</code>.</li>
            </ol>
        </li>
        <li><strong>Goal:</strong> State your null hypothesis ($H_0$) and whether you reject it at $\alpha = 0.05$.</li>
    </ul>

    <hr>

    <h2>Challenge 2: Proportions and the A/B Test</h2>
    <p><strong>Scenario:</strong> An e-commerce site is testing two different "Buy Now" button colors.</p>
    <ul>
        <li><strong>Group A (Red Button):</strong> 1,000 visitors, 50 clicks.</li>
        <li><strong>Group B (Green Button):</strong> 1,100 visitors, 72 clicks.</li>
    </ul>

    <ul>
        <li><strong>Tasks:</strong>
            <ol>
                <li>Use the <code>prop.test()</code> function in R.</li>
                <li>Calculate the 95% confidence interval for the difference in proportions.</li>
            </ol>
        </li>
        <li><strong>Goal:</strong> Determine if the Green button actually performs better or if the result is likely due to random chance.</li>
    </ul>

    <hr>

    <h2>Challenge 3: Analysis of Variance (ANOVA)</h2>
    <p><strong>Scenario:</strong> You are testing three different fertilizers to see if they result in different plant heights.</p>

    <ul>
        <li><strong>Dataset:</strong> Create a dummy frame or use <code>PlantGrowth</code>.</li>
        <li><strong>Tasks:</strong>
            <ol>
                <li>Visualize the data using a boxplot to see the distribution.</li>
                <li>Run a <strong>One-Way ANOVA</strong> using <code>aov()</code>.</li>
                <li>If the ANOVA is significant, perform a <strong>Tukey HSD</strong> post-hoc test (<code>TukeyHSD()</code>) to find out <em>which</em> specific fertilizers differ from one another.</li>
            </ol>
        </li>
        <li><strong>Goal:</strong> Explain why we use ANOVA instead of just doing three separate t-tests.</li>
    </ul>

    <hr>

    <h2>Pro-Tips for R Testing</h2>
    <ul>
        <li><strong>The P-Value Logic:</strong> If $p < 0.05$, the result is "surprising" enough under the null hypothesis that we ditch the null.</li>
        <li><strong>Formula Notation:</strong> R loves the <code>y ~ x</code> (Response ~ Predictor) syntax. For the t-test, it looks like <code>t.test(mpg ~ cyl, data = my_data)</code>.</li>
        <li><strong>Assumptions Matter:</strong> Always check if your data is normal and if the variances are equal (<code>var.equal = TRUE</code> or <code>FALSE</code>) before trusting your t-test.</li>
    </ul>
</details>
<br>

From this experience, I question myself whether I truly deserve the Data Analyst in R completion certificate. I need to improve. I need to learn more. I need to get my hands dirty into hypothesis testing. I need more practive. I need to overcome this shortcoming. I want to be a Data Scientist.

# Today's Exercise

```r
# Task 1: Is there a difference between cars with 4 and 6 cyls?
alpha <- .05

## filter only cyl 4 and 6
cyl46 <- mtcars %>% 
  filter(cyl %in% c(6,4)) # filter cyl only 4 and 6

## normality test of cyl = 6
cyl46 %>% filter(cyl == 6) %>% 
  pull(mpg) %>% 
  shapiro.test()

## normality test of cyl = 4
cyl46 %>% filter(cyl == 4) %>% 
  pull() %>% 
  shapiro.test()

## Independent Two-Sample T-Test
### base package T-Test
t.test(mpg ~ cyl, data = cyl46, alternative = "two.sided", var.equal = TRUE)

### infer package T-Test
cyl46 %>% 
  t_test(mpg ~ cyl, alternative = "two-sided")

# Verdict: There is statistical difference in mpg between cyl = 4 and cyl = 6
```

```r
# task 2: Is Green button better than Red button
# declare variables
visitor <- c(1000, 1100)
clicks <- c(50,72)
groups <- c("Red Button", "Green Button")
ex2 <- data.frame(groups, visitor, clicks)

# proportion test
ex2 <- ex2 %>% mutate(prop = clicks/visitor)

prop.test(clicks, visitor, alternative = "less", conf.level = .95)

# Verdict: Evidence not enough to tell Green button performs better than Red button
```

```r
# task 3: How each fertilizer perform?

## Boxplot
PlantGrowth %>% 
  ggplot(aes(x = weight)) +
  geom_boxplot()

# One-way ANOVA
PGaov <- aov(weight ~ group, data = PlantGrowth)

# TukeyHSD
TukeyHSD(PGaov)

# Verdict: Control > Treatment 2 > Treatment 1 
```

# Reflection

When I wrote this diary, I also reviewed my code in the exercise. I realized that if I had read the scenario more meticulously, perhaps I could've done it better. But, oh well.

I learned that I have to be more careful and thorough when doing hypothesis testing. It is a good thing to fully understand what problem I'm facing.

> _Update (19:45 GMT +7):_
> 
> I found a [table](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*dg_yj0Zr_6EJtHLVJgf29g.jpeg) that summarizes **_"what h-test"_** for **_"what data types"_**! It's really good.
{: .block-warning}

<div class="row mt-3"><a href="https://miro.medium.com/v2/resize:fit:2000/format:webp/1*dg_yj0Zr_6EJtHLVJgf29g.jpeg">
    <div class="col-sm mt-3 mt-md-0" href="https://miro.medium.com/v2/resize:fit:2000/format:webp/1*dg_yj0Zr_6EJtHLVJgf29g.jpeg">
        {% include figure.liquid loading="eager" path="https://miro.medium.com/v2/resize:fit:2000/format:webp/1*dg_yj0Zr_6EJtHLVJgf29g.jpeg" class="img-fluid rounded z-depth-1" %}
    </div>
</a></div>

