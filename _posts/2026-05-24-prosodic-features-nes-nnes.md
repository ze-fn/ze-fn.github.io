---
layout: distill
title: "Prosodic Features of NES vs. NNES"
description: "Differences and Effects on Intercultural Communication"
tags: [Linguistic, Prosodic Features, Intercultural Communication, World Englishes, Data Science, English]
categories: [Portfolio]
date: 2026-05-24
authors:
  - name: Zelvy Fauzan
    affiliations:
     name: Independent
  - name: Tartila Firtianisa
    affiliations:
     name: Independent
featured: false
mermaid:
  enabled: true
  zoomable: true
toc:
  - name: Introduction
  - name: Literature Review
    subsections:
    - name: 
    - name: 
    - name: 
  - name: 
  - name: 
    subsections:
    - name: 
  - name: 
  - name: 
  - name: 
giscus_comments: true
bibliography: papers.bib
---

# Introduction

During my stay in Bandung, precisely on 24th of May 2026, I watched a TV program from TVRI that focused on introducing Indonesian cultures. The hosts were native Indonesian and they spoke mostly in English (except when they talk to locals). When I listen to the host carefully, I noticed a slight difference in prosodic features of the host. To be precise, I usually listen to NES (Native English Speaker) hosts, and this felt different from that of NNES (Non-Native English Speaker). So, this got me thinking:

> "Is there really a difference of prosodic features in NES and NNES?"

# Literature Review

During the conception of this mini study, I thought that the sound features that regulates how meaning is conveyed are (1) pitch, and (2) intonation. But I didn't actually know the difference between the two. I looked up on Google to find out the difference between the two features. 

After doing some literature reviews , I found that there are at least three sound features when human communicate: (1) pitch, (2) intonation, and (3) tone.

## Pitch

The word "pitch" has a slight different meaning across fields. In music studies, pitch refers to the highs and lows note of the instrument. It specifically points at the musical notes such as _re_, _fa_, _la_, _si_, _do_, etc. at octaves. Different notes in different octave level denotes different pitch, which can (usually) be distinguishable from the frequency of the note. For example, a "do" note from a lower octave would fall under low frequency band. Inversely, the same "do" note from a higher octave level would be classified as high frequency. In other words, as the musical note gets higher, frequency gets higher as well (a positive relationship). In linguistics, however, the word "pitch" refers to the highs and lows of the vocal sound being produced by someone. In a sense, it has similar characteristics to that of _pitch_ in the music studies. 

In this study, we focus on the pitch as in the linguistics study, and we record the pitch in Hertz (Hz) unit. To better understand this concept, perhaps it would be better to see the following graph extracted from Thorson, Franklin, and Morgan's <d-cite key="Thorson02102023"></d-cite> study:

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://www.tandfonline.com/cms/asset/7cfb9c99-5321-42c1-bf20-d4eb8820b9eb/hlld_a_2149400_f0002_oc.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## Intonation

Intonation can be described as the "melody" of the pitch produced. As an illustration, intonation can be viewed as a time-series data in which the pitch changes as the time goes by. The intonation one produces may be influenced by many factors. To name a few, culture, emotion, and fluency are influencing the intonation (and the meaning to which the utterance is addressed). In linguistics, intonation maneuver is seen from the contours or the peaks and plunges of the intonation.

## Tone

In this study, we refer "tone" as the perceived meaning of the overall pitch and intonation. Some of the known tones are:

| Pitch | Intonation | Tone |
| :---- | :--------- | :--- |
| High  | raising-raising-raising | Angry |
| Flat  | flat-plunge | Neutral |
| Low   | low-low-raising-low | Sad |

# Methodology

Hereby we disclose the overall materials and procedures of this research project.

## Data Collection

THe following procedure entails how we gathered the data, along with inclusion and exclusion criteria.

### Inclusion

- Filetype: Video, Audio
- Speaker: NES, NNES

### Exclusion

- Text Genre: Song, Poem, and other creative literature.

### Procedure

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/prosodic_features_nes_nnes/promotional_poster.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## Data Processing

For each video or audio, we extracted the pitch, intonation, and the tone using Python. As for the tone, we validate each of the observed data to ensure correctness of the machine learning model used in the Python script.

## Data Storage

For each video or audio file that has been undergo processing step, we created a dedicated sheet to store them for every contributors to access. Once every data observation is stored, we convert each sheet into their respective CSV file, along with their respective sheet name. 

## Data Wrangling

