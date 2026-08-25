---
layout: post
title: Traffic Lights in Arduino Uno R3
description: Some of my first circuits
tags: [Arduino, Electrical Engineering, Project]
categories: [Learning]
date: 2026-07-06
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

# 1. Introduction

This one is from the second chapter of Robonyx's course to [Starter Course for Arduino](https://www.skool.com/robonyx/about), which is about "Reaction Speed Game". The idea of the project is simple. 

> Press the button as fast as possible and you win!

But the programming part behind that simple game would be a challenge for my learning.

# 2. Reverse Engineering from Output

The course demonstrated the project first before going into the materials. So I had a glimpse of what I would build from this chapter.

## 2.1. What I Saw

| Parts | Count |
| :---- | :---: |
| Jumper Wire (Male)    | 13    |
| LED                   | 5     |
| Resistor (220)        | 5     |
| Button                | 2     |
| Buzzer                | 1     |

## 2.2. My Guess

I grouped what I saw into different sections: (1) signals, (2) input, (3) output, and (4) algorithm.

### Signals

1. Red, Yellow, Green LEDs are programmed to countdown for the game to start.
2. The last LED signal lit duration is randomized to make it more "reaction-based" instead of fixed delay.
3. When game starts, two LEDs are lit. They are waiting for input from users.

### Input

1. Two buttons are waiting for input from users.
2. User who pressed the button first will has the LED keep lit.
3. User who pressed later will has the LED off. Or, ignore any input.

### Output

1. The LED from the winner will lit.
2. Buzzer will sound when the winner is decided.

## 3. Project

### 3.1. What I Learned

- Negative rail can be used interchangeably to GND on the R3.
- Another design of traffic light circuit! (from instruction)
- CTRL + T for auto format.

### 3.2. Traffic Lights Revisited

I followed what was instructed to build a traffic light circuit design. But then I found something strange. See my traffic light circuit design below. 

(compare img: left-left, right-right)
caption: left lit, right off

### 3.3. Buzzer

It has the same concept with lighting up an LED, but buzzer don't need a resistor. This means we can directly channel the cathode end into the GND.

{% details Script %}
```cpp
int buzzer = 3;

void setup() {
    pinMode(buzzer, OUTPUT);
}

void loop() {
    digitalWrite(buzzer, HIGH);
    delay(1000);
    digitalWrite(buzzer, LOW);
    delay(1000);
}
```
{% enddetails %}

### 3.4. Serial Monitor

This one has something to do with interacting between the Arduino and the computer. For example, we want the Arduino to send repeated message "Hello!" to our computer. We use `Serial.begin()` in the setup function and `Serial.println()` in the loop function.

{% details Script %}
```cpp
void setup() {
    Serial.begin(9600); // 9600 is considered common. Fast but also stable.
}

void loop() {
    Serial.println("Hello!");
    delay(1000);
}
```
{% enddetails %}

### 3.5. Digital Inputs, Buttons, Pull-up/down Resistors

This part is the part where we make the Arduino to take user input, along with other behaviours that follow.

1. Take input from current

```cpp
int inputPin = 5; // Can be any value in the pin

void setup() {
  pinMode(inputPin, INPUT);
  Serial.begin(9600);
}

void loop(){
    Serial.println(digitalRead(inputPin));
    delay(100);
}
```