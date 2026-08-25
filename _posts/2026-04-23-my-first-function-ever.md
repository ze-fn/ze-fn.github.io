---
layout: post
title: My Very First Ever Function and Equation
description: I formulated an equation and a function to solve my engineering problem!
tags: [Measurement, Physics, Programming, R, English]
categories: [Diary, Journal]
date: 2026-04-23
featured: false

authors:
  - name: Zelvy Fauzan
    url: https://ze-fn.github.io/
    affiliations:
      name: Independent
      url: https://github.com/ze-fn/
---

Today is Thursday, 23 April 2026.

This marks the very first day I made my own function. Ever. In my life!

In the past few days, I have been working on a project of my own. A project about [Network Engineering](https://ze-fn.github.io/blog/2026/expanding-home-network). It is where I extend my home network so that it can cover more areas.

The idea of this Network Engineering project was very simple. I wanted my second house to get internet connection. To do so, I needed to extend a LAN cable to my second house. In simple, baby words:

1. taka a cable,
2. plug one end to router #1,
3. extend,
4. plug the other end to router #2.

It's a very simplified process. But... inside those processes, I fought my way from the ground up. 

To determine how much cable I need, I had to measure the length of the cable so that I won't run out of cable when connecting the two routers. I grabbed my tape measurement, hand-bagged my personal journal, clipped my fountain pen onto my T-shirt, plugged my TWS and played my favorite playlist at the moment (I tend to change playlist over time). 

When it was time to do the calculation, I thought to myself, 

> _"it would be a pain in the arse if I had to figure out the equation to calculate the length of the cable over and over again."_ 

So I wondered to myself whether there is a formula for this kind of problem. But, before I started looking on the internet or even asking to ChatGPT or Gemini, my head was struck by who-knows-what. I miraculously thought, 

> _"Why don't I just write or create one by myself? For my future self, for my future works?"_ 

At that moment, I decided to delve into physics.

I recalled my studies in senior high school about physics. But I couldn't come up with anything. So I changed the way I think. Instead of recalling, I started observing. I wrote the length of each cable segments. Once I finished jotting down the measurements, I thought to myself that it'd be a piece of cake to find out the total cable length for this project.

Few moments passed by and I, then, was kind of getting a revelation. 

> _"Wait, each cable segment must turn in 90 degrees. But if I bend the cable too extreme, I fear that it would damage the cable. There has to be a way or at least someone have had thought about this before."_ 

I googled for bend cable recommendation on the internet and found out that there was in fact a discussion about this. I can only say that humans are awesome creatures! So, after I found the missing last piece of the puzzle, I embarked on another journey: defining the equation.

I developed my very own equation to solve the specific problem I'm facing and asked some of my friends what they think about it, about the equation that I have developed. Their reviews, suggestions, and criticisms were invaluable for me.

Long story short, my equation was approved to be "reproducible" by my fellow friends who majored in subjects related to physics. Then, the last step is to make the equation applicable, reproducible, and can be used with ease.

To be honest, while I'm studying physics in the past few days (until now), I'm also learning to be a Data Scientist. I enrolled in a Career Track from Datacamp and, coincidentally, the part I was currently learning was "Functions". Maybe the stars have aligned so perfectly. I learned how to write my very own custom function in R language and BOOM ... My very first function ever. It took me about half an hour to port my measurement equation into an R function. The moment I substituted the arguments in the functions and ran the function and then it printed out the expected value, I was beyond happy. My satisfaction was immeasurable and my day was prosperous.

You can review my equation and R code for calculating the LAN cable length needed below.

$$
L_{reach} = p_1 + p_n - 2r + \frac{1}{2} \pi r + \sum_{i=2}^{n-1} p_i - 2r + \frac{1}{2} \pi r 
$$

$$
L_{total} = ((\sum_{i = 1}^{n} p) + (\sum_{i = 1}^{n} p) - L_{reach}) / 100
$$

where:

$ L_{reach} $ : The length of the cable with bends (resulted in shorter length compared to $ \sum p $) (in meter)

$ L_{total} $ : The total cable length needed (in cm)

$ p $ : Stands for the "part" of the cable (in cm)

$ r $ : The radius for "the turn" (in cm)

And below is the R code. Since different cable type has different rigidity and different recommended radius bend value multiplier, I designed the function to take `type_cable` arguments ("utp", "ftp", "stp") and it will lead to different multiplier value.

```r
l_cable_needed <- function(x, d_cable = 0.5, type_cable = "utp", r_round = TRUE) {
  # defining needed variables
  pi <- 3.1415
  
  # defining the radius based on type_cable
  if (type_cable == "utp") {
    radius <- d_cable * 6
  } else if (type_cable == "ftp") {
    radius <- d_cable * 8
  } else if (type_cable == "stp") {
    radius <- d_cable * 8
  }
  
  # adjust radius when r_round = TRUE
  if (r_round == TRUE){
    radius <- ceiling(radius)
  } else {
    radius <- radius
  }
  
  # the equation
  cable_reach <- x[1] + x[length(x)] - 2*radius + pi*radius/2 + sum(x[2:length(x) - 1] - 2*radius + pi*radius/2)
  distance <- sum(x)
  rec_cable_length <- cable_reach + cable_reach - distance
  
  # print the result
  output <- paste0(
    "Cable length needed: ", rec_cable_length/100, " meters \n",
    "Bend radius: ", radius, " cm")
  cat(output)
}

l_cable_needed(o_measurements, 0.6, "stp", r_round = TRUE)

```

I hope you find this diary entry useful. I find it useful... for my works :wink: