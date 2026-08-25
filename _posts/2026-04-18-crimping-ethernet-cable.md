---
layout: distill
title: "Crimping Ethernet Cable"
description: This is my very first attempt at crimping an ethernet cable
tags: [Ethernet, IT Support, Network Infrastructure, English]
categories: [Portfolio]
date: 2026-04-18
authors:
  - name: Zelvy Fauzan
    affiliations:
     name: Independent
featured: false
mermaid:
  enabled: true
  zoomable: true
toc:
  - name: Introduction
  - name: Tools and Preparations
  - name: Literature Review
  - name: Execution
  - name: Lesson Learned
---

## Introduction

This post is my first step of my bigger project: [Expanding Home Network](https://ze-fn.github.io/blog/2026/Expanding-My-Home-Network). I learned first-hand experience about crimping an Ethernet cable. This experience is invaluable for me so that I can become an IT support or Network Engineer in the future. I initiated this project even though I have bachelor and master degree in English Language Education is because I want to switch my career from education into the IT field. You may ask why I wanted to switch career. It is because I have fallen in love with IT field since I was in early elementary school (around 2005), but I was not eligible to be enrolled into the computer sciences faculty (I was overqualified in other subject so the university accepted my "second choice").

## Tools and Preparations

I bought crimping toolkit the other day. It contains:

- 467 Multifunction Network Cable Tester
- Network Crimper
- Coax Stripper
- Upgraded Wire Punch Down Impact Tool
- Multifunctional Wire Stripper Cutter
- Mini Wire Strippper Knife
- Cross Screwdriver
- Flat Screwdriver
- Transparent Box
- RJ45 Crystal Connector

Additionally, I also have an unused <u>ethernet cable</u> lying around in my garage so I used it to practice crimping.
<aside>
<p>
Turned out, it was not a cable for computer networking!
</p>
</aside>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/crimping_ethernet/network-crimping-tools.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

In short, one set of crimping toolkit and an unused ethernet cable.

## Literature Review

Before I start crimping, I looked up on the internet about how to crimp an ethernet cable. I found several sources but I chose two main sources. One is from WikiHow and the other one is from a YouTube video.

I read the steps in the [WikiHow](https://www.wikihow.com/Crimp-Rj45) first because I like and prefer reading compared to video tutorial, although I went to watch a YouTube video that demonstrated how to crimp an Ethernet cable :D

As I perceive it, the procedure was simple.
1. First, I cut the outer layer of the cable using the network crimping tool.
2. Untwine the inner cables and order it in a correct order, either using T568A or T568B.
3. Push the cable into the RJ45 connector head.
4. Crimp the RJ45 connector head using the network crimping tool.

## Execution

As I inspect my unused "ethernet cable", I found something peculiar about the cable. As I remember it correctly, I bought the ethernet cable long ago so that I can transfer between my PCs without using a thumbdrive. But it was never a success. So, this time, I tried to take a closer look into the cable. See the orange, orange-white, green, and green-white inner cables.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/crimping_ethernet/inspecting-the-supposedly-ethernet-cable.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

_"Why there is only four pins inside?"_, I thought to myself while holding the supposedly ethernet cable. I clealy remembered that ethernet cable should be consisted of 8 pins but this one only had 4 pins. This got me nervous.

So, I looked up the internet again and see what cable that has 4 pins. Turned out, it was not meant for network connection. It was mainly for handheld or something like that. I thought to myself, _"Ah! So that's why I never able to connect my PCs with this cable. It lacks pins!"_ Still feeling dumb inside, I proceed to continue my first ever crimping excercise.

I cut the cable at one of its end. Then, I peeled off the outer cable layer, leaving the smaller cable exposed. I ended up with this:

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/crimping_ethernet/cutting-ethernet-cable.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/crimping_ethernet/cutting-off-ethernet-cable.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Left: I slice the cable outer layer coating. Right: I cut off the "ethernet" cable.
</div>

Referencing back to the sources that I reviewed, they said that after the outer layer of the cable is cut and the inner cables are exposed and reordered, the next thing to do was just to slide the cables into the RJ45 connector head and crimp it. I thought the ethernet cable needs to be cut again until the copper wires are exposed. So, I cut the cable coating of the inner cables like in the following photo:

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/crimping_ethernet/eth-cable-copper-exposed.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

I tried to slide the overly exposed cable into the RJ45 only to find out that it was so hard, and that it was not supposed to be inserted like that (silly me!).

I spent about 30 minutes figuring out how to slide the ethernet cable into the RJ45 connector head because it was so hard to align the coppers into the respective connectors. Then I consulted to a video [YouTube](https://www.youtube.com/watch?v=yRJCdozMnzU), but I didn't get it. Still confused. Then, I took a very, very close look into the original cable. Turned out, I was not supposed to expose the copper of the ethernet cable!

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/crimping_ethernet/example-cable.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

See the picture above. The cable at the end of the RJ45 connector head has no exposed copper. So, it got me thinking, _"Wait, is it what I'm thinking? There is some kind of fork-shaped metal right below the cables. Perhaps I was not supposed to expose the inner cables after all! All I need to do is just rearrange the inner cables into the proper order and slide it into the RJ45 connector head. After that, I crimp it."_

To gather the evidence on my hypothesis above, I compared two RJ45 connectors side by side.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/crimping_ethernet/compare-rj45.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

I was right! The RJ45 connector on the right side has not "punched" yet and the fork-shaped metal is not set in place whereas the RJ45 connector on the left side has its fork-shaped metal "punched". So, the fork-shaped metal in the RJ45 connector head is supposed to be piercing the inner cables of the ethernet cable! 

Today I learned!

## Lesson Learned

One does not simply **EXPOSE THE COPPER WIRES** of an ethernet cable and crimp it. One **DOES CRIMP** it with the copper still protected by the coating.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://imgflip.com/s/meme/One-Does-Not-Simply.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>