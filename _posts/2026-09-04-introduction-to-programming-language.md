---
layout: distill
title: "1. Intro to Programming Language"
description: "Lesson Journey from Microsoft's Web Dev for Beginners"
tags: [Web Development]
category: [Learning]
date: 2026-09-04
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

This post is my notes from individual lesson of Microsoft's Web Dev for Beginners learning course. 

## Check-in Time: How Are You Feeling?

> Does the idea of "giving instructions to computers" make sense to you now?

I have prior knowledge about programming so the idea of giving instructions to computers did make sense easily. In fact, I was an informatics teacher who taught this exact idea to students.

Human use languages, and so do the computers. But, the two speak different languages and yet we still have to interact with each others. This is where programming language come into play.

Programming language bridges between human and computers. What so different between human and computer languages, anyway? Well, computers only understand `0`s and `1`s. The don't understand human language, heck they don't even understand what I'm writing now. 

In a way, computers are just like human. They will do whatever thing that we asked them to. Say, you asked your friend to take the pen on the table, and your friend asked again "which pen? there are a lot of pens here with different colors". So you tell your friend that you need the "red pen" that is the shortest among the pens there, not the tallest, not the middle, only the shortest one. That is quite a detailed instruction, no? Your friend understand it and brought you the pen you needed.

If we change this friend with a computer as well as the environment, we ask the same kind of instruction. Say you asked the computer to take a file named "exercise1.docx" but you have files named "exercise1.docx" all over your folders. You need to specify with incredible detail of the location of the file. Let's say that you want to take the one inside the `/school/geography/exercises/` folder.

The difference between our friend and computer is that our friend can ask again to us for confirmation, reconfirmation, etc. if something is amiss. But our computer will do exactly what we told them to even though our instruction is false. 

> Can you think of a daily task you'd like to automate with programming?

There are a lot of daily task that I would like to automate. 

* Dishwashing
* Laundry
* Cooking
* Reminder
* Writing Curriculum Vitae
* Grading student's work
* Providing students with generic feedbacks for generic errors

> What questions are bubbling up in your mind about this whole programming thing?

Well, why are there so many programming languages? Why not use one, single programming language for all?

## Concept Check: Building Blocks Mastery

> Can you explain the difference between a variable and a statement in your own words?

Variables and statements are often come in pair, but the two are different.

Variables are container. Just like that. Its function is to contain a value.

Statements are a way of telling the computer to do a single, specific task. In this case, one may understand statements as a "declaration". 


{% tabs varstats %}

{% tab varstats js %}

```js
let variable; # This is variable
variable = "I'm the content of variable" # This one is a statement
console.log(variable) # This one is also considered a statement
```

{% endtab %}

{% tab varstats r %}

```r
dummy_object <- vector("numeric") # Variable declaration
dummy_object <- c(1, 2, 3, 4, 5, 6) # Statement
dummy_object # Also a statement
```

{% endtab %}

{% endtabs %}


> Think of a real-world scenario where you'd use an if-then decision (like our voting example)

There are so many, in fact. To list some:

* IF day is Saturday or Sunday, THEN don't work
* IF distance to ground is 5, THEN initiate safe landing
* IF score is less than 75, THEN declare "Not Pass"
* The list goes on ...

> What's one thing about programming logic that surprised you?

The IF-THEN for multiple cases in `js`. I didn't know that you can make conditional statement with such easy-to-understand way. I'm pointing at the `switch`. It's just so clever and intuitive.

## Tool Mastery Check: WHat Resonates With You?

> Which tool are you most excited to try first?

There are so many tools that excite me right now. But if I had to pick only one, I would chose Text Editor. I mean, this is basically the backbone of every programming languages. As long as we have a media to write and a tool to write, we can build practically anything.

> Does the command line still feel intimidating, or are you curious about it?

Well, to be honest, the terminal is also one of the thing that excite me the most. They do intimidate me, even until now, but as long as I can tame it down, they are basically the most obedient assistant. There were times when I play around with command line and messed up many things. In fact, this day (Sunday, 6 September 2026), I used a terminal in my laptop (Ubuntu) to connect to a VPN. My home internet was quite the "picky" one when it comes to connection. It won't allow me to access many websites. So, to tackle this, I tried to connect to cloudflare VPN (1.1.1.1). Since linux is heavily "terminal", I looked up the internet on how to connect to the internet through a VPN, and I accidentally deleted the content of `/etc/resolv.conf`. When I thought nothing happened, all of a sudden I can't connect to the internet. It was because I entered:

```bash
$ sudo su cat /etc/resolv.conf
$ sudo su tee /etc/resolv.conf
$ sudo su cat /etc/resolv.conf
$ sudo su nano /etc/resolv.conf
```

Yeah, it was quite the experience! But I won't step back from trying to tame the command line. I know that if I tame this beast, I would be unstoppable.

> Can you imagine using browser DevTools to peek behind the curtain of your favorite websites?

Well, my latest project (Project: ELLIE) is about web scrapping and many of my times spent on looking on the inspect element panel! It has become a second nature for me to open the DevTools of the browser. Sometimes I even do some tricks to show/hide HTML tags with specific CSS elements to get something that I needed (not my fault. They started designing the web unbearable that it made me the user difficult to navigate or get what I wanted).

## Challenge

### Language Explorer

**Mission:** Pick three programming languages of different "universe" and look up a simple code using that three programming languages.

**My Answers:**

{% tabs langexplorers %}

{% tab langexplorers js %}

```js
let a;
let r;

console.log("Circle Area Calculator");
r = parseFloat(prompt("Enter radius value of your choice: "));
a = Math.PI * (r ** 2);
console.log(`Your circle is : ${a}`);
```

{% endtab %}

{% tab langexplorers r %}

```r
r <- as.numeric(readline(prompt = "Enter radius value of your choice: "))
a <- pi * (r ^ 2)
print(paste("Your circle is: ", a))
```

{% endtab %}

{% tab langexplorers python %}

```py
import math
r = float(input("Enter radius value of your choice: "))
a = math.pi() * (r ^ 2)
```

{% endtab %}

{% endtabs %}

## Uncover their Origin Stories

Since I picked JS, R, and Python in the previous section, I will stick to it for this one as well.

### Javascript

It all started ...

### R

It was a sunny day...

### Python

Snakes? I don't think so...

## Meet the Communities

I need to find communities for each programming languages.

## Follow Your Gut Feeling

I have been practising programming for quite some time. The first programming language that clicks with me was R. But then as I gain more experiences from my practices and other people's experience, I think I want to try Python, JS, Bash, C++ and many more. 

After trying learning SQL, PostgreSQL, Python, Javascript, and many others, R language is still what clicks with me the most. I think I will stay with R for the time being.

## Final Reflection Check-In

> What's one thing about programming that excited you today?

All developers out there still look up the basic stuff. I thought senior developers remember the basic stuff as if it's second nature to them. Now I feel more confident.

> Which tool or concept do you want to explore first?

Among all the exciting topics, I think it'd would be better for me to explore mora about control flow. I do get excited about parallel computing using CUDA, computer networking, etc. but fundamentals are called "fundamentals" not without a reason.

Control Flow it is!

> How do you feel about starting this programming journey?

At first, I thought it would be another classic programming course. But after I read it, it's actually more engaging.

> What's one question you'd like to ask a developer right now?

How do you cope with client's *request* when developing their design?

