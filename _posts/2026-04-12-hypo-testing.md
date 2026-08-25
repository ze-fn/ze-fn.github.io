---
layout: distill
title: Hypothesis Testing
description: How I understand hypothesis testing from the very beginning until getting the z-score and p-value
tags: [Statistics, Hypothesis Testing, English]
categories: [Learning]
date: 2026-04-12
authors:
  - name: Zelvy Fauzan
    affiliations:
     name: Independent
featured: false
mermaid:
  enabled: true
  zoomable: true
toc:
  - name: Hypothesis Testing Overview
  - name: The $ z $-score and $ p $-value
    subsections:
    - name: Bootstrap Distribution
    - name: The $ z $-score
    - name: The $ p $-value
  - name: Tails in Hypothesis Testing
    subsections:
    - name: Two-tailed
    - name: Left-tailed
    - name: Right-tailed
---

# Hypothesis Testing Overview

I learned Hypothesis Testing in R from Datacamp this afternoon. To be frank, I found myself struggling to catch up with grasping the idea of hypothesis testing. But I will try to digest what I have learned in this writing. 

As Datacamp illustrates it, hypothesis testing is like a criminal trial: the defendant is assumed to be **NOT GUILTY** as the default verdict. The defendant will be pronounced **GUILTY** if the evidence is undoubtedly proving crime. These illustrations are not sticking in my head. So I tried to come up with another way of understanding it.

Hypothesis testing, as I understand it, is a way of deciding whether something is **ACCEPTED** or **REJECTED**. Think of it as inquiring. Imagine you are in a situation where you forgot where you put your glasses. You start to guess where your glasses is. The moment you are guessing, that is hypothesis testing. You might guess you left your glasses on the table. To see if this is true, you walked to the table and searched there. Unfortunately, your glasses is nowhere to be found on the table. Let's pause searching your glasses for a moment.

You asked youself where you put your glasses, that is the equivalent of **RESEARCH QUESTION**. Then, you started to guess where your glasses might be. This is the equivalent of **HYPOTHESIS**. When you are hypothesizing, there is only two possible outcomes, it's either **there** or **not there**. Since you are hypothesizing that _"my glasses must be on the table"_, this is the **NULL HYPOTHESIS** ($$ H_0 $$), and the inverse of your hypothesis is _"my glasses is **not** on the table"_ and this is called the **ALTERNATIVE HYPOTHESIS** ($$ H_a $$). So, you tried to prove it by walking and searching your glasses on the table. To no avail, you found nothing. This means that your **null hypothsis** ($$ H_0 $$) is **REJECTED**. Therefore, you started to look somewhere else. This whole process is called **HYPOTHESIS TESTING**.
<aside>
<p>Mind you that the $ H_0$ is pronounced H-naught</p>
</aside>

In hypothesis testing, the way you compose the research question determines how the null and alternative hypotheses appears. If you believe that something to be _"there"_, then the null hypothesis ($$ H_0 $$) would be: "there is". Likewise, since you already have your null hypothesis ($$ H_0 $$), your alternative hypothesis ($$ H_a $$) would be: "there is no". If we are wondering something to be negative, then the null hypothesis ($$ H_0 $$) would be: "there is no", and for the alternative hypothesis ($$ H_a $$) would be: "there is".

# The $ z $-score and $ p $-value

The term $$ z $$-score may haunt anyone who is not accustomed to statistics. In fact, it also frightened me. Well, actually, as the time I write this, I'm still frigghtened by this so called $$ z $$-score. But I do know how to get this $$ z $$-score. Allow me to elaborate here.

## Bootstrap Distribution

First, we need to sample the data from our table/dataset. How many do we need? Good question. We need to sample as many as the number of observation that is available in our dataset. So, if we have 1500 observations, we sample it as many as 1500. Now, you might be wondering _"why do we have to sample 1500 times when the dataset is 1500 observations, isn't just taking all the population?"_. Alright, the 1500 samples are with replacement. So, there will be cases where we pick the same observation point during the sampling. Note that we tell the computer to sample the data, not us picking the observation. An example for this "with replacement sampling" would be that of picking observation number 5 thrice out of 6 possible outcomes. A better illustration would be:

    pool: 1, 2, 3, 4, 5, 6

    pick: 6

    sampling: 1, 5, 5, 3, 5, 6

This is what "with replacement" looks like. Instead of picking 1, 2, 3, 4, 5, 6; we could get 5 thrice. On the other hand, if we, say, manually pick 1, 2, 3, 4, 5, 6 then this is not "with replacement sampling", that is "without replacement sampling". 

Now, the sampling result `1, 5, 5, 3, 5, 6` in the previous example is then aggregated using mean: we sum it up and then divided it by the number of the datapoint that we picked. 

$$ \bar{x} = \frac{1 + 5 + 5 + 3 + 5 + 6}{6} $$

$$ \bar{x} = \frac{25}{6} $$

$$ \bar{x} = 4.166667 $$

The resul of the mean aggregation is what we actually need. Notice that from 5 data points we ended up with only a single data point: the mean. This process is only one-time sampling. We need more. After sampling once, we then **repeat** the sampling process as much as we need. Usually we take 1000 times or 5000 times. 

If you are familiar with R programming (like I do), below is a code snippet of creating a bootstrap distribution. I wrapped "the mean of sampling with replacement" inside a `replicate` function to repeat the sampling process 5000 times (specific to this example; other casees may differ).

```r
bootstrap_distribution <- replicate(n = 5000,
    expr = {
        table %>%
            slice_sample(prop = 1, replace = TRUE) %>%
            summarize(mean(x)) %>%
            pull(x)
        }
)
```

This collection of means that we get from our sampling with replacement (proportion = 100%) is then organized into a new table/dataset: we call it `bootstrap_dist` and it contains a column called `boot_samp_mean`.

## The $$ z $$-score

Remember that we have our hypothesis in mind and we want to check the truth (whether our null hypothesis is rejected or accepted). Let's take another example of hypothesizing.

What would you assume about the students' numeration skills in the Arts faculty?

You probably hypothesized that:
_arts person perform less in numeration skills, probably around 50 in a scale of 100._

Let's just pretend that we have conducted a survey or a test to a population of Arts students from a university. We got 550 observations. When we take the average score of numeration of Arts students, we found that the Arts students scored 65 in average. Then we take the conclusion that _"the Arts students averaged higher than what was hypothesized"_

... or can we? _*VSauce SFX playing_

We have to verify the mean score that we got is actually **meaningful**. But how? 

Well, we use the $$ z $$-score!

Don't worry, I will walk you through. :wink:

So, here is the ingredients that we need to get the $$ z $$-score:

$$
standardized \space value = \frac{value - mean}{std \space deviation}
$$

or (if you prefer a more Mathematics nuances):

$$
standardized \space value = \frac{x_i - \bar{x}}{s}
$$

where:

$$
s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}}
$$

The formula above may look quite intimidating at first (actually, it still is in my eyes!). But fret not for it will be simplified in the coding process. We don't need to write that complicated formula, there are people who already make a function that we can call at any time. As simple as telling someone to "do standard deviation calculation!" and then the person will return with the answer. The only difference here is that instead of askins a person, we ask computer to do it. Trust me, it is as simple as flipping your hands!

Now, below is the second step for getting the $$ z $$-score.

$$
z \space score = \frac{sample \space stat - hypothesis \space value}{std \space error} 
$$

where:

$ sample \space stat $: The mean of the variable from the original (sampled) dataset

$ hypothesis \space value $: Our hypothesis. It can be anything really, but in academic settings, we have to make an educated guesses. Read some papers and see what their results (see their results!)

$ std \space error $: The standard deviation (sd) from Bootstrap Distribution

Remember our hypothesis about Arts students' numeration skill, it is $ 50 $. Now, let's take another pretender (no, not that Pretender song by Hige Dandism), that the actual average we got from the dataset is $ 60 $. Then, let's also pretend that we have our standard error value from the bootstrap distribution and plugged everything into the $$ z $$-score formula. We got the $$ z $$-score of $ 1.76665 $.

Now, the question is... is this $ 1.76665 $ number high or low? We will discuss it in [The $ p $-value](#the--value) section.

Oh, before we answer whether the $ z $-score we get is low or high, I will show you how easy it is to perform $ z $-score calculation in R. Check out below.

```r
# Take appropriate sample
random_sampling <- dataset %>%
  select(numeric_col) %>%
  slice_sample(n = 150)

# Generate a bootstrap distribution
bootstrap_distn <- replicate(n = 3000, 
  expr = {
    random_sampling %>%
    slice_sample(prop = 1, replace = TRUE) %>%
    summarize(resample_mean = mean(numeric_col)) %>%
    pull(resample_mean)
  }
)

# Calculate Standard Error
std_error <- sd(bootstrap_distn)

# Determing hypothesis value
hypo <- .6

# Calculate the z-score
z_score = (mean(random_sampling$numeric_col) - hypo) / std_error
```
<a name="the--value"></a>


## The $ p $-value

You might have heard it thousands of time about this $$ p $$-value, perhaps in research articles. I also stumbled upon this $$ p $$-value many times as a student.

Did you know that the $$ p $$-value is an abbreviation of _"probability"_? I know. When I discovered this, it also blew my mind away. I didn't know it was "probability" all along!

So, what is this _"probability"_-value refers to in hypothesis testing? 

The $ p $-value, recall in the previous paragraph, is a probability value. To be precise, it is the probability of whether the hypothesis happened bacause of coincidence or not. So, it is a kind of a way to make sure of our hypothesis. Imagine it like when someone asked you about something and you reassured them.

> **You:** "Kids nowadays have less motivation to learn in the classroom"
> 
> **Person 1:** "Are you sure?"
> 
> **You:** "Yeah, it is."

The short conversation above roughly demonstrates the $ p $-value (though. I believe there are better illustrations).

Now, let's dive deeper into $ p $-value. In hypothesis testing, the $ p $-value is state of the $ H_0 $, and it ranges from $ 0 $ to $ 1 $: around/close to $ 0 $ means $ H_0 $ is rejected while closer to $ 1 $ means $ H_0 $ is (*still*) accepted.
<aside>
<p>Note that in hypothesis testing, we try to dethrone or challenge the $ H_0 $ <italic>(null hypothesis)</italic></p>
</aside>

THere are two ways to make a verdict on our hypothesis:

1. The $ \alpha $ value
2. The Confidence Interval (CI)

Let's discuss them one by one.

### The $ \alpha $ value

It is perhaps the easiest way to make a verdict on our hypothesis. We just need to compare the $ p $-value with the $ \alpha $ value. 

- If $ p \leq \alpha $ then **REJECT** $ H_0 $ 
- If $ p \geq \alpha $ then **ACCEPT** $ H_0 $

You might be wondering, what is this $ \alpha $ value. Well, it is the value that we use to challenge against the hypothesis ($ H_0 $). Usually, researchers use $ 0.100 $, $ 0.050 $, or $ 0.001 $. These $ \alpha $ values have their own use case.

- $ \alpha = 0.100 \space (90\%) $ is usually for exploratory studies
- $ \alpha = 0.050 \space (95\%) $ is usually for general studies (this is the most widely used)
- $ \alpha = 0.001 \space (99\%) $ is usually for medicine studies (or strict scientific studies)

Implementing it in R is easy peasy lemon squeezy! Check this out.

```r
# Assume we have calculated the z-value which is stored in `z_score`
p_value <- pnorm(z_score, lower.tail = TRUE)

# Hypothesis test
p_value <= .050
```

### The Confidence Interval (CI)

Alright, I mentioned that there are two ways. We have discussed the first one and now we move to the second way of making a verdict on our hypothesis. The Confidence Interval (CI).

We use CI the similar way as the $ \alpha $ value. We check if the $ p $-value lies within the interval range of the bootstrap distribution. Let's take a look into the code, shall we?

```r
# Let's also assume that we have our bootstrap distribution called `dataset_boot_distn`
ci_dataset_boot_distn <- dataset_boot_distn %>%
  summarize(
    lower = quantile(resample_mean, 0.005),
    upper = quantile(resample_mean, 0.995))

# Check whether the p_value lies within the CI range
p_value <- ci_dataset_boot_distn$upper & p_value >= ci_dataset_boot_distn$lower
```

Now, you might have something on your mind, probably wondering about the values of the quantiles in the summarize() function. Let me be clear. The value of the `lower` and `upper` is actually the $ \alpha $ value divided by two: one for the lower and one for the upper. So, if we decided to use $ \alpha = 0.050 \space (95\%) $ then we divide the $ \alpha $ value into two parts. $ 0.025 $ into the `lower` part and $ 0.975 $ into the `upper` part.



```markdown
2. Confidence Interval evaluation (Check if 50 is inside the interval)
 Note: Because this is a one-directional alternative hypothesis (lower than 50), 
 researchers often use a one-sided confidence bound, but a standard 99% CI works 
 to see if 50 is a plausible value.
is_hypo_in_ci <- hypo >= conf_interval_quantile[1] & hypo <= conf_interval_quantile[2]
```



# Tails in Hypothesis Testing

## Two-, left-, right-tailed hypothesis testing

I learned the kinds of tails in Datacamp the other day. To be fair, I haven't fully grasped the idea of this tails. But, when I came across the exercise, I think I understand what the tails mean.

In the exercise the Datacamp provided, I was instructed to pair research questions with their respective tails, whether the research question should use two-tailed, left-tailed, or right-tailed hypothesis testing. There, I found emerging patterns.

- **Two-tailed:** is when we want to figure whether something is 