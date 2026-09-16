---
layout: distill
title: "2. Intro to GitHub"
description: "Lesson Journey from Microsoft's Web Dev for Beginners"
tags: [Web Development]
category: [Learning]
date: 2026-09-16
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
This is a post about my learning into Web Dev for Beginners from Microsoft. It contains my reflections, notes, and many more.

## First Repository Check-in: How Did That Feel?

> How did it feel to see your code appear on GitHub for the first time?

My first ever commit to GitHub was long ago, about 1 to 2 years ago. But honestly, it felt like I was a true developer! The feeling of successfully committing my very first code into my GitHub repository was amazing. I can't believe with my very own eyes that I could do what other developers can do. Nowadays, as my commit increase largely, I feel accustomed to git push and pull. Although I think I still touching the surface of Git. There are so many commands which function is unknown to me. That is why I think this course is good for me to get to know better about Git.

> Which step felt the most confusing, and which felt surprisingly easy?

The most confusing part was when I was first trying it back then. Everything felt alien even for making an empty directory and the `.gitignore` felt hard. But as I used more and more git commands, it became second nature, really. Especially when I learned more about Linux and the terminal. All those frustrations getting to know Linux paid off now.

> Can you explain the difference between git add, git commit, and git push in your own words?

`git add` is when we want to stage the file(s) or folder(s) of your selection. We can add the whole directory along with its sub directories using the dot `.`; or we can specify it to a directory or file (but this one takes very long time to do, even more when you have many files to commit).

`git commit` is a required command to execute after we perform `git add`. It is a command to give notes to our file(s) and folder(s) in the staging. I still don't know why it is a must, though. Maybe it has something to do with hashing?

`git push` is when we want to send the file(s) and folder(s) in our staging into the cloud/GitHub. It's very straightforward. We push what we have in the staging into our GitHub repository of choice. What I mean by "of choice" is that GitHub allow collaboration, so it can be your own repository or even someone else's. I read that collaboration is next in the sub chapter so I will stop here.


## Collaboration Skills Check: Ready to Work With Others?

> Does the idea of forking and pull requests make sense to you now?

Quite. Forking is when we want to copy other's repository into our profile. For example, person A created a repo called "Website Project 1", but person A worked in collaboration with person B and C. Person B and person C need to have the same draft from person A (let's just assume that person A is the leader). Just like in a writing collaboration project where everyone write on the same paper (well, that would be chaotic, to be honest), but instead of in one paper we copy the draft so that everyone got one copy. This is called "fork". It's like asking and getting the exact copy of somneone else's repository. 

Pull Request (shorthand: PR) has quite the confusing term. It's "pull" but not to our local machine. I mean, we use `git pull` to get changes from main branch into our local machine, right? But PR is actually comes from other contributors. If we use the context in the previous example, and let's say that person B made changes inside their branch and want to push it to the `main` branch (of the repo created by person A). Person B need to conduct Pull Request. It's like telling person A and person C that person B made some changes and want everyone to apply it in their working space. 

> What's one thing about working with branches that you want to practice more?

I think I want to practice more about collaborating in general. I get the idea of collaborating in GitHub is quite the same with collaborating with people in Google Docs or other real-time document editing platform. The difference being that GitHub is not quite that real-time, and that we are working in a copy of the main draft. That said, I think I need to find some friends who are willing to collaborate with me. About coding, that is. 

> How comfortable do you feel about contributing to someone else's project?

I love helping others. But now, I think my skill in coding is not enough for collaboration. I mean, I'm still beginner at coding or developing a system or anything, and people are already making good and awesome projects. So, for the time being, I will work alone. I have a friend who is willing to learn code but she seems to be busy with her businesses.


## Testing Skill Check: Ready to Find Issues?

> Which testing method seems most approachable to you right now?

I think the screen reader is the most approachable right now. I myself have a visual impairment. I have Stargardt disease (low vision). I navigate mostly using keyboard now, although sometimes I still use mouse. When gaming, I also prefer to use a controller than a keyboard and mouse (previously the opposite). 

> Can you imagine using keyboard-only navigation for a full day?

Actually, I'm doing it right now. Navigating through keyboard and keystrokes. It's actually faster for me because I have a visual impairment.

> What's one accessibility barrier you've personally experienced online?

Thanks to my disability, I find it hard to see screen in bright environment. Small texts are hard to read. And also there is this blind spots around my central vision that prevent me from seeing whatever lies beneath it. 

## POUR Principles Check: Making It Stick

> Can you think of a website feature that fails each POUR principle?

A website that violates each of POUR princple. I will start with the P first.

* Perceivable: A website that don't give alt text to media.
* Operable: A website that can only accept mouse pointer input, neglecting keyboard input.
* Understandable: A website that is meant for middle schoolers but the content of the posts used university-level vocabulary.
* Robust: A website that is only designed specifically for a certain device, say, PCs only; Users with small screen (smartphones) will struggle to see or even understand the website.


> Which principle feels most natural to you as a developer?

I would say Understandable and Robust are the "must have" features of a website.

> How might these principles improve design for everyone, not just disabled users?

People may need accessibility features even if they don't have any disabilities. For example, people who is reading an email in bright sunlight (let's just say that this person is outdoor) may struggle to read the screen because the light of the screen is lower than the light of the sun. This will make the screen look dark and hard to see, not to mention read the texts inside that little screen.


## Semantic HTML Mastery Check: Building Strong Foundations

> Can you identify the landmarks on a webpage just by looking at the HTML?

Yes. Landmarks are usually inside a `<nav>` HTML element. 

> How would you explain the difference between <section> and <div> to a friend?

The difference between `<section>` and `<div>` lies in the compliance. Div is like the general purpose tag. You can use it literally for anything you like. But that leaves problems. If everything is built upon the div tag, you wouldn't know which one is which. As a developer, I see this as a nightmare. Hard to read. The section tag on the other hand tells us that what lies inside the tag is actually a part of the main content of the page. You wouldn't place a section tag in the navigation tag, would you? Or in the buttons. So, section tag is actually behaves just like the div tag but it has semantic features that helps differentiate which tag is which and belong to which element group. Using section tag in the main body of the content is considered best practice, but you can still use div for other parts of the webpage.

> What's the first thing you'd check if a screen reader user reported navigation problems?

I would check the HTML tag used in the HTMl document. First, I would ask which specific part is the problem. Users may not be proficient enough in reading HTML so I would ask for which part of the content. From there, I would backtrack which tag is that paragraph or content is from.

