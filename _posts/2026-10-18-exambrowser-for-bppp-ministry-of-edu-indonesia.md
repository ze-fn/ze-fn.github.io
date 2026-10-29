---
layout: distill
title: "Found bug in Indonesia's Ministry of Education's Software Installer"
description: "Surface level Reverse Engineering with Network Flow using Wireshark"
tags: [Network Analysis, Network Engineering, Computer Science]
category: [Journal]
date: 2026-10-18
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

I'm enrolled in a teacher professional program from Indonesia government. At the end of the program, there is an exam. When I took the program, the exam was online from home, and we had to install a specific software, most of the time it's called "exambrowser". But some bugs prevented me and the other participants to download and install the software.

I'm going to tell it in chronological order just like a report.

## URL Analysis

On 18th of October 2026, I received a notification from the program administrator (from the university) that all participants to download the exambrowser for final exam. This was where my analyst instinct kicked in. The administrator (or perhaps more of a manager or coordinator) of the program sent a link to the exambrowser software. The link was referring to a subdomain of `kemdikbud` (previous nomenclature for Ministry of Education) while in fact the ministry changed name since the new president ruled. The ministry changed name from `Kemdikbudristekdikti` to `Kemendikdasmen` (for primary and secondary education) and `Kemendiktisaintek` (for higher education and research). The link, of course, returned an error. It couldn't be accessed. 

```txt
[omitted]

Windows:
http://exam.bppp.kemdikbud.go.id/win

Mac:
http://exam.bppp.kemdikbud.go.id/mac

[omitted]
```

I found two problems here. The network protocol is in `http` when it should usually be in `https`. The former being insecure connection and the latter is a secured connection protocol for http network transfer. The second problem was the domain name. It should be `*.kemendikdasmen.go.id` instead of `*.kemdikbud.go.id`.

To test it, I opened the link for Windows and (you guessed it!) it returned an error of "expired server certificate".

As a work around, I changed the link to use the new ministry domain. And, sure enough, it worked and a download started.

## The Exambrowser Installer

The downloaded software turned out to be an installer instead of the program itself. I didn't think much that time so I ran the program. It tried to fetch the "real" exambrowser but apparently the installer returned a "download error" and that I need to check my internet connection. This was ridiculous because my internet connection was not to blame. Good internet connection from the ISP, even from two different VPN provider. Despite many alternatives, the installer refused to continue and showed the same error again and again.

I consulted to the video tutorial on how to install the exambrowser installer _(*insert yo dawg meme)_. I know, I know. For an IT practicioner like me to watch a video on how to install a software is kind of awkward and embarrassing, but hey, I know my stuff alright.

The video showed the installer "downloading exambrowser..." status log. This is a huge evidence that the software I installed was actually an online installer, not a standalone installer. It's like when you install a browser for a newly born PC. You download, say, "internet_browser.exe" but it turned out it's an online installer and not a standalone installer. This case was the same. But this part of information became a crucial turning point for my investigation.

Now I knew that the software fetches the installer from the ministry's server, and then installs the exambrowser on the client PC. But what if I told you that the online installer fetches from the wrong address? I mean, when the ministry name changed, the domain name for that ministry have to be changed too. Well, they didn't. At that time.

## Network Analysis using Wireshark

My hypothesis was that the online installer fetches from the wrong address. To prove this, I used wireshark to see where this "online installer" is fetching from.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/online-installer-exambrowser-bppp-kemdikbud-kemendikdasmen.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Network connection captured when the Online Installer "start to Install" the exambrowser.
</div>

[Also check the `.pcap` file for yourself if you are curious like me.](https://ze-fn.github.io/assets/pcap/exam_bppp_kemdikbud_kemendikdasmen.pcapng)

It is evident that the online installer fetches from `*.kemdikbud.go.id` and not `*.kemendikdasmen.go.id`.

I reported this to the administrator to be relayed to the IT dept in Ministry of Education.

By the way, in all of my post, I use **Ministry of Education** or **Ministry of Higher Education** instead of whatever the ministry name is at the moment. I hate when the ministry name is always changing. It confuses the hell out of people (go make up your mind, dear oh so distinguished Mr. or Mrs. President of Indonesia. Like, seriously.)

## Follow up

The online installer has been fixed on 19th of October 2026.