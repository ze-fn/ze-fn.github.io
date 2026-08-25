---
layout: post
title: "Second Travel to Bandung"
description: "Why TV programs in NHK Wold is different from that of in Indonesia?"
tags: [Travel, Critical Thinking, Data Science, English]
categories: [Journal]
date: 2026-05-21
featured: false
mermaid:
  enabled: true
  zoomable: true

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

# Changelog

2026-05-23: Add new points in `Brainstorming`
2026-05-21: Initial draft


# Introduction

Tuesday, 19 May 2026, I went to Bandung again to attend some tests. It was a recruitment test for a manager position in the Indonesian President's Priority Program "Koperasi Desa Merah Putih". The announcement was on 19 May 2026 and the schedule for my first two tests were on 20 May 2026. Talk about professionalism, eh?

Anyway, during my stay at a hotel, I watched a TV channel from Japan. NHK World. They offered useful information about Japan and other part of the world. But something piqued my interest.

NHK World broadcasted a TV program talking about "emergency food research". At first, I was intrigued by the way the information was packed. They wrapped scientific results into an easy-to-digest information for the mass very cleanly.

I wonder how they prepared the animation, the data, the visualization, the research, and so on. 

But then again, something came to my mind.

> _"Why did I rarely (or maybe never) watched any Indonesian TV program with this level of detail, scientific, and transparency?"_

# Brainstorming

To answer such question, I need to think of the methodology systematically. But before that, I also need to raise some questions that might affect how my first question arose.

1. Is there any TV channel in Indonesia that offers informative, research-driven TV program from year 2000 to 2026?
2. If there is a TV channel in Indonesia that offers informative, research-driven TV program, how many times do they air in a day, in a week?
3. If there is a TV channel in Indonesia that offers informative, research-driven TV program, is the TV channel intended for international audience or national audience (i.e., World channel or National channel)?

4. Is there any TV channel outside of Indonesia that offers informative, research-driven TV program from year 2000 to 2026?
5. If there is a TV channel outside of Indonesia that offers informative, research-driven TV program, how many times do they air in a day, in a week?
6. If there is a TV channel outside of Indonesia that offers informative, research-driven TV program, is the TV channel intended for international audience or national audience (i.e., World channel or National channel)?

# Database Design

The table below is a level 1 normalized (N1) databse design

| variable | description | data type |
| :------- | :---------- | :-------- |
| tv_channel | TV channel name | `chr` |
| tv_program | TV program name | `chr` |
| country_origin | Country origin of the TV channel | `chr` |
| dist_type | Whether the TV channel is broadcasted for National or Intenational audience | `chr` |
| audience | The audience to whom the program is intended for | `chr` |

