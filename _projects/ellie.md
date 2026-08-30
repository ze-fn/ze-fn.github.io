---
layout: post
title: "Project: ELLIE"
description: "Contains Researcher's Log"
tags: [Teaching Methodology, English as a Foreign Language, Indonesia]
category: Research
importance: 1
mermaid:
  enabled: true
  zoomable: true
code_diff: false
map: false
chart:
  chartjs: true
  echarts: true
  vega_lite: false
tikzjax: false
typograms: false
# bibliography: 
related_publications: false
toc:
  sidebar: true
pretty_table: true
_styles: >
  .highlight p {
    color: green;
  }
---

## **Researcher's Log**

0. 2026-08-30: Links with 403 code are stashed. Proceeding with scrape procedure.
0. 2026-08-29: Some links returned 403 Forbidden. Trying HTTP Header request forgery.
0. 2026-08-28: [Pseudocode for web scrapping](https://ze-fn.github.io/blog/2026/pseudocode-to-retrieve-vol-and-issue/)
0. 2026-08-27: Initial draft of research report

## **Found Problems**

### **403 Forbidden on Some Websites**

<div class="highlight"> 
  <p><strong style="color: green">Lesson Learned:</strong> Some websites have security measures against bots or tools</p> 
</div>

I thought it would be appropriate for me to test whether all of the links that I have gathered are accessible. This is something that I learned from Cybersecurity courses. Manually visiting them were no problem. I could enter them just right. Things got tricky when I tried to access the journal websites using a tool (i.e., R using the httr2 package). Some of the links didn't accept any tools or bots to access them. As a workaround (again, I learned this from Cybersecurity), I patched the HTTP Header request with custom headers. Below are the headers I tried along with the results.

| Header | Value | Outcome | Iteration |
| :----- | :---: | :------ | :-------: |
| `N/A`  | `N/A` | Failed  | 11/15     |
| User-Agent | "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0" | Failed | 12/15 |
| Referer | "" |   | x/x |
| X-Origin-Site | "" |   | x/x |

### **The Fate of URLs with 403 Codes**

As of the writing of this section (2026-08-30), I haven't found any workaround to automate the retrieval of websites with bot protection. I will periodically update this section as I stumble upon new ways to bypass the 403 code. In the meantime, I think of doing a manual input into the database.

### **rvest-ing the Websites**

<div class="highlight"> 
  <p><strong style="color: green">Lesson Learned:</strong> Different website, different structure, even if they use the same website template</p> 
</div>

I was naive to assume that all journal websites have identical HTML structure. Turned out, even though they use the same template website, they structure the pages differently. Some appended the URL for each issue right in the HTML text content, like the following:



```html
...
  <a href="#">Vol XX, No XX</a>
...
```


```html
...
  <div class="ex" href="#">April</div>
  <p>Vol. XX, No. XX</p>
...
```


I had to use wildcard instead and leave the data cleaning at a later stage.