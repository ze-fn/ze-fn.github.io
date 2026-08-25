---
layout: post
title: "Microcontroller 1: Speed Reaction Game"
description: A project from Robonyx Academy
tags: [Arduino, Electrical Engineering, Project, C++]
categories: [Learning]
date: 2026-07-16
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

## Introduction

This is actually my second attempt to create a speed reaction game. The first attempt was purely imitating what Hugh did. 

In the second attempt, I tried to create my own functions for `LED countdown` and `Winner Ringtone`.

## Custom Functions

When I was working on the game mechanics, I was wondering on adding a winner ringtone into the game mechanics.

When either of the player pressed the button first, the buzzer will ring for three times with a short interval. But writing it for the two conditions would be tedious.

So, I was thinking of making a function instead of hard-coding it inside each of the conditions.

I created the function for the winner ringtone:

```cpp
int buzzer = 6;

void winnerRingtone() {
    for (int i = 0; i < 4; i++) {
        digitalWrite(buzzer, HIGH);
        delay(50);
        digitalWrite(buzzer, LOW);
    }
}
```

Additionally, I thought of making another custom function. A function for the LED Countdown.

It wouldn't hurt me, would it? It's also a good reinforcement for my learning!

```cpp
// Countdown LEDs
int redLED = 10;
int yellowLED = 9;
int greenLED = 8;

// Put the LEDs pin inside a list
int countdownLEDs[] = {redLED, yellowLED, greenLED}

// Function: LED Countdown
void winnerRingtone() {
    for (int LED : countdownLEDs) {
        digitalWrite(LED, HIGH);
        delay(1000);
        digitalWrite(LED, LOW);
    }
}
```

## Result



```cpp
// Countdown LEDs
int redLED = 10;
int yellowLED = 9;
int greenLED = 8;

// Buzzer
int buzzer = 6;

// Player LEDs
int player1LED = 3;
int player2LED = 12;

// Player Button Input
int player1button = 2;
int player2button = 13;

// Negative Rail = Lane 44 -> GND

// Define default state for the game
int buttonPressed = 0;

// Ringtone for winner
void winnerRingtone() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(buzzer, HIGH);
    delay(50);
    digitalWrite(buzzer, LOW);
    delay(50);
  }
}

// List: Countdown LEDs
int countdownLEDs[] = {redLED, yellowLED, greenLED};

// Function: Countdown LEDs
void countdownLED() {
  for (int currentPin : countdownLEDs) {
    digitalWrite(currentPin, HIGH);
    delay(1000);
    digitalWrite(currentPin, LOW);
  }
}

void setup() {
  // put your setup code here, to run once:
  pinMode(redLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(player1LED, OUTPUT);
  pinMode(player2LED, OUTPUT);
  pinMode(player1button, INPUT_PULLUP);
  pinMode(player2button, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  // Call Countdown LED function
  countdownLED();
  
  // Game Begin
  digitalWrite(player1LED, HIGH);
  digitalWrite(player2LED, HIGH);
  while (buttonPressed == 0) {
    if (digitalRead(player1button) == 0) {
      buttonPressed = 1;
      digitalWrite(player2LED, LOW);
      winnerRingtone(); // Call Winner Ringtone function
      Serial.println("Player 1 Wins!");
      delay(2000);
    } else if (digitalRead(player2button) == 0) {
      buttonPressed = 1;
      digitalWrite(player1LED, LOW);
      winnerRingtone(); // Call Winner Ringtone function
      Serial.println("Player 2 Wins!");
      delay(2000);
    }
  }
  // Reset all to default state
  digitalWrite(player1LED, LOW);
  digitalWrite(player2LED, LOW);
  buttonPressed = 0;
}
```