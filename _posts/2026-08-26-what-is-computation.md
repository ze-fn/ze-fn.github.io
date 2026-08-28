---
layout: post
title: "What is Computation?"
description: Theories and aspects of computational thinking.
tags: [MIT OCW, Autonomous Learning, Electrical Engineering, Computer Science]
categories: [Learning]
date: 2026-08-26
featured: false
mermaid:
  enabled: true
  zoomable: true
tabs: true
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

## Lecture Notes

I have prior knowledge on computation and programming, so I will recall instead of noting something new.

{% tabs lns %}

{% tab lns computation %}

Computation is the process of counting something. It comes from the word "compute" which means "to count".

Computers do computation. That's why they are called computer, they do computation.

Computers are not human. Well, at the time when I write this you may have heard of AI which seems to give "life" to computer but that's nothing compared to life. Computer only *memorize* and _do things_ as we told them. Explicitly. If we ask the computer to "calculate the area of this square using this formula", then the computer will do the job.

You might be thinking that it is basic. But wait, that's not all.

What if we give our computer the formula of a "triangle area" instead of a "square area"? Guess what, computers don't understand it and will use triangle area instead of square formula. Why this happens? It's because computer will only do the task they are told to. If we told them to calculate the area of a square but we give them the formula of a triangle area, then the computer will use the triangle area formula.

Explicit is the key.

{% endtab %}

{% tab lns algorithm %}

As said in the previous tab section, computers only know how to memorize and do things (explicitly). For computers to memorize, we simply declare it to the computer. It's something similar to, "this is a pen", in a way that "x is 9". It's [object] = [value]. That is how we declare a **variable** for the computers to memorize. And they are good at it.

Algorithm, on the other hand, is equivalent to a recipe, a procedure text, or "how to do things orderly". Let's say we want to toast a bread.

1. Prepare two slices of bread.
2. Plug the toaster into a wall socket.
3. Put the bread slices into the toaster.
4. Pull down the lever on the toaster that makes the bread comes down.
5. Wait for the timer to end.
6. As soon as the toaster finished toasting the bread, it will pull out the bread.
7. Take out the bread.
8 Serve the bread on a plate.

Above is an example of algorithm for humans. For computers, it's quite the same but they need extra details and meticulous instructions. For example:

`1. Prepare two slices of bread` 

is equivalent to:

1. Pick up the bread bag.
2. Move to nearby desk.
3. Put bread bag on the desk.
4. Open the bread bag.
5. Take two slices of bread out of the bag.
6. Put the bread on a temporary plate.

{% endtab %}

{% tab lns Binary Search %}

I have seen how binary or bisection search on YouTube. Guess what? I watched searching algorithm at 2 AM when I was should have slept. 

In short, binary search is a searching algorithm to find the best value from a simple true/false condition. For example: a number guessing game with binary search.

Take a number between 0 and 100, the computer will guess it.

The way the computer guess the number is by asking the whether the value is greater than or less than.

Say you think of 45. The computer will take a random number and ask you back with a True or False question.

```txt
Computer: "Is your number lower than 50?"
You: "Yes"
Computer: "Is your number lower than 25?"
You: "No"
Computer: "Is your number lower than 37?"
You: "No"
Computer: "Is your number lower than 43?"
You: "No"
Computer: "Is your number lower than 46?"
You: "Yes"
Computer: "Is your number lower than 44?"
You: "No"
Computer: "Your number is 45."
```

{% endtab %}

{% endtabs %}

## Problem Sets

There are 6 problem sets in this topic. I intentionally made all problem sets hidden under an expandable details.

{% details **Problem Set 0** %}

[Link to the problem set 0](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps0/)

Instructions:

Write a program that does the following in order:

1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”. 

```python
import math

x = float(input("Input a value for X: "))
y = float(input("Input a value for Y: "))
exponent = x ** y
log2ofx = math.log(x, 2)

print(f"\n")
print(f"{x} raised to the power of {y} is {exponent}")
print(f"The log base 2 of {x} is {log2ofx}")
```

{% enddetails %}


{% details **Problem Set 1** %}

There are three parts in problem set 1:

* Part A: House Hunting
* Part B: Saving, with a raise
* Part C: Finding the right amount to save away

[Link to the problem set 1](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/mit6_0001f16_ps1/)

{% tabs ps1 %}

{% tab ps1 Part A %}

**House Hunting**

Instructions: Write a program to calculate how many months it will take you to save up enough money for a down payment.

```python
# Input
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
months = 1
r = 0.04

# Calculations
monthly_salary = annual_salary / 12
portion_down_payment = 0.25
current_savings = 0

# Iteration
while current_savings <= total_cost * portion_down_payment:
    months = months + 1
    current_savings = current_savings + monthly_salary * portion_saved
    current_savings = current_savings + (current_savings * r / 12)

print(f"Number of months: {months}")
```

{% endtab %}

{% tab ps1 Part B %}

**Saving, with a raise**

Instructions: Write a program to calculate how many months it will take you save up enough money for a down payment [given that monthly salary is increasd every 6 month]. LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). 

```python
# Input
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
months = 1
r = 0.04

# Calculations
monthly_salary = annual_salary / 12
portion_down_payment = 0.25
current_savings = 0

# Iteration
while current_savings < total_cost * portion_down_payment:
    months = months + 1
    if months % 6 == 0:
        monthly_salary = monthly_salary + monthly_salary * semi_annual_raise
        current_savings = current_savings + monthly_salary * portion_saved
        current_savings = current_savings + (current_savings * r / 12)
    else: 
        current_savings = current_savings + monthly_salary * portion_saved
        current_savings = current_savings + (current_savings * r / 12)

print(f"Number of months: {months}")
```

{% endtab %}

{% tab ps1 Part C %}

**Finding the right amount to save away**

Instructions: Write a program to find the best saving rate given (1) annual salary, (2) salary raise 0.07 every 6 months, (3) annual return 0.04 ... to achieve 25% of 1000000 (1 million USD), but the rate should be at least 100 USD.

Pseudocode:

1. Annual salary / 12 = monthly salary
2. DP for house = Total cost * 25%
3. Target months to save = 36
4. 

{% endtab %}

{% endtabs %}

{% enddetails %}

## Projects

I got some inspirations while watching some videos about "DIY Jet Engine" on YouTube.

{% tabs projects %}

{% tab projects Project 1 %}

**Scales with different starting value**

Idea: Sometimes you want to measure liquid or granular solid objects (like salt), but you need a container. This container has weight, but we only interested in the weight of the stuff and not with the container.

Goal: Write a program that measures the weight of something while disregarding the weight of the container used to contain the "something".

Pseudocode:

1. User input weight in kg (`true_weight`).
2. Check if `true_weight` is either int or float.
3. If `true_weight` is neither int or float, return error message and ask user to input again.
4. If `true_weight` is either int or float, ask user whether they use container or not (`has_extra`) with default answer of "N".
5. If user input `has_extra` is NOT in list of accepted values ("y", "Y", "n", "N", ""), return error message and ask user to input again.
6. If user input `has_extra` is IN list of accepted values ("y", "Y", "n", "N", ""), check whether `has_extra` again.
7. If `has_extra` is either "y" or "Y"; ask user to input weight for the container (`extra_weight`)
8. If `has_extra` is either "n", "N", or ""; return `true_weight`
9. Check if `extra_weight` is either int or float.
10. If `extra_weight` neither int or float, return error message and ask user to input again.
11. If `extra_weight` either int or float, return `print(f"Weight: {true_weight - extra_weight} kg)`

Code:

```python
# Greetings
greetings_msg = "Welcome to Virtual Scales"
ver = "0.2"
print(greetings_msg)
print(f"version {ver}")

# Base variables
valid_responses = ["y", "Y", "n", "N", ""]

# Input
true_weight = input("Enter weight in kg: ")

# Input validation
while true_weight.isdigit() != True:
    print("Your weight is NOT a number")
    true_weight = input("Enter weight in kg: ")

# Input
has_container = input("Do you use container? [y/N] ")

while has_container not in valid_responses:
    print("Error: Invalid response")
    has_container = input("Do you use container? [y/N] ")

if has_container in valid_responses[3:6]:
    print(f"Weight: {float(true_weight)} kg")
else:
    extra_weight = input("Enter container weight in kg: ")
    
    while extra_weight.isdigit() != True:
        print("Your container weight value is NOT a number")
        extra_weight = input("Enter container weight in kg: ")
    
    new_weight = float(true_weight) - float(extra_weight)
    print(f"Weight: {new_weight} kg")
```

{% endtab %}

{% endtabs %}