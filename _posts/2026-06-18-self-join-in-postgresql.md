---
layout: distill
title: Self-Join in DBMS
description: Revisiting the SQL Syntax and the Logic Behind It
tags: [DBMS, SQL, English]
categories: [Diary, Journal]
date: 2026-06-18
featured: false
mermaid:
  enabled: true
toc:
  - name: Introduction
  - name: Recalling The JOINS
  - name: How I Started
  - name: How I Ended up
giscus_comments: true
authors:
  - name: Zelvy Fauzan
    url: https://ze-fn.github.io/
    affiliations:
      name: Independent
      url: https://github.com/ze-fn/
pretty_table: true
---

# Introduction

It had been one day since I resigned from teaching position at a local Junior High School. This presented me with a thought of next career.

> "What's the next step?"

In my mind, I already knew what I wanted to achieve and how to achieve it. I wanted to be a Data Scientist or Data Analyst. However, in the past few months, I learned primarily R programming in general and R programming for inferential statistics. This, of course, shifted my focus from one language to another. Previously, I was quite confident in MySQL and PostgreSQL skills. But when I tried to recall them, I found my memory to be hazy, to say the least. Therefore, I looked up some PostgreSQL exercises.

I found this website called [PostgreSQL Exercises](https://pgexercises.com/). It has many exercises from basic to advanced querying skill, from basic query to string manipulation and recursive. I found the basic exercises refreshing for my skill. It was as if a plant getting watered. However, when it comes to "Joins and SUbqueries", my brain stalled.

# Recalling The JOINS

I remembered that there are some techniques of table joins.
- `INNER (LEFT/RIGHT) JOIN`: where one of the table is merged into another upon a row match.
- `OUTER (LEFT/RIGHT) JOIN`: where the value in one table is matched with another table but when there is no match then the value in one of the table is left blank.
- FULL JOIN: where the tables are merged upon match in both tables.
- CROSS JOIN: where for every value in one table is paired with every value in the other table.

One of the exercises in the exercise website was ["Produce a list of all members, along with their recommender"](https://pgexercises.com/questions/joins/self2.html). In essence, it was a "self-join" problem. The idea is to get a list of members along with the _recommender_. 

For example:
I joined a gym membership. The gym gave me 10% discount for the subscription because I joined their membership. The gym also said that I can get another 10% discount if I invite people to joing the gym membership, on a condition that the people I invited have to use my unique code upon registering the gym membership. Long story short, I invited 8 people to the gym and all of them joined the gym membership.

Now, let's shift to the gym's management point of view. 

The staff wanted to know who invited who. So they looked up the database and used self-join to see the answer.

Naturally, each member has an identifier attached to their information in the database (usually in a column called `id`), along with a column (usually) called `referral`. 

| id    | fname     | referral    |
| :---- | :-------- | :---------- |
| 1     | Andy      |             |
| 2     | Braun     | 1           |
| 3     | Claire    | 1           |
| 4     | Donny     | 2           |
| 5     | Francis   | 2           |
| 6     | Gwenda    | 1           |
| 7     | Historia  | 3           |
| 8     | Igna      |             |
| 9     | Jill      |             |
| 10    | Kamila    | 2           |

The table above shows the database for gym membership. We can see that:

- Andy (id = 1) has invited Braun, Claire, and Gwenda.
- Braun (id = 2) has invited Donny, Francis, and Kamila.
- Claire (id = 3) has invited Historia.

Usually, this kind of information is presented in the following table format:

| id    | referal_name | referee  |
| :---- | :----------- | :------- |
| 1     | Andy         | Braun    |
| 1     | Andy         | Claire   |
| 1     | Andy         | Gwenda   |
| 2     | Braun        | Donny    |
| 2     | Braun        | Francis  |
| 2     | Braun        | Kamila   |
| 3     | Claire       | Historia | 


Seeing the original table as is (or maybe even the joined table) may prove difficult to understand, so let's illustrate this referral process bit-by-bit. I will walk you through.

# JOINS in Details

1. First, let's imagine we make a copy of the original table.

| id    | fname     | referral    |
| :---- | :-------- | :---------- |
| 1     | Andy      |             |
| 2     | Braun     | 1           |
| 3     | Claire    | 1           |
| 4     | Donny     | 2           |
| 5     | Francis   | 2           |
| 6     | Gwenda    | 1           |
| 7     | Historia  | 3           |
| 8     | Igna      |             |
| 9     | Jill      |             |
| 10    | Kamila    | 2           |

---

| id    | fname     | referral    |
| :---- | :-------- | :---------- |
| 1     | Andy      |             |
| 2     | Braun     | 1           |
| 3     | Claire    | 1           |
| 4     | Donny     | 2           |
| 5     | Francis   | 2           |
| 6     | Gwenda    | 1           |
| 7     | Historia  | 3           |
| 8     | Igna      |             |
| 9     | Jill      |             |
| 10    | Kamila    | 2           |

2. Let's put the tables side-by-side.

(image 1.1)

Since the two table are identical, I will call the table in the left one as "lt" (shorthand of _left table_) and the table on the right side as "rt" (abbreviated from _right table_). 

3. Notice that the column `referral` in both tables are actually _"referring"_ to the `id`column.

(image 1.2)

If we draw a line between `id` and `referral`, we will get lines of connections. Let's call it "relationship".

4. Now comes the rather tricky part: joining the tables.

The idea is to match the value in the `referral` column with the `id` column. In this case, we only care to see who has successfully invited people. Therefore, want to see only the matching values between the two columns from the two tables. Take a look at the table below.

| lt.id | lt.fname  | lt.referral | rt.id    | rt.fname | rt.referral |
| :---- | :-------- | :---------- | :------- | :------- | :---------- |
| 1     | Andy      |             | 2        | Braun    | 1           |
| 1     | Andy      |             | 3        | Claire   | 1           |
| 1     | Andy      |             | 6        | Gwenda   | 1           | 
| 2     | Braun     | 1           | 4        | Donny    | 2           |
| 2     | Braun     | 1           | 5        | Francis  | 2           |
| 2     | Braun     | 1           | 10       | Kamila   | 2           |
| 3     | Claire    | 1           | 7        | Historia | 3           |

Did you notice that the value in `lt.id` has identical value as in the `rt.referral`? This is because we just performed a table join. In PostgreSQL term, this is called `INNER JOIN`.

Some of you may feel uneasy or intimidated by the `lt.referral` and `rt.id` columns. Fear not for they are usually not shown or are intentionally not included. I intentionally showed this so that you can see the _"behind the scenes"_. And we can always exclude the unnecessary columns, like the following:

| lt.id | lt.fname  | rt.fname | rt.referral |
| :---- | :-------- | :------- | :---------- |
| 1     | Andy      | Braun    | 1           |
| 1     | Andy      | Claire   | 1           |
| 1     | Andy      | Gwenda   | 1           | 
| 2     | Braun     | Donny    | 2           |
| 2     | Braun     | Francis  | 2           |
| 2     | Braun     | Kamila   | 2           |
| 3     | Claire    | Historia | 3           |

Or even more, you can also exclude the `rt.referral` if you are confident in your querying skill. Me personally prefer printing out the `rt.referral` so that I can validate whether my query answers the right question, or whether the resulting table query is aligned with whatever was requested.

# Recapau 

All in all, the self-join takes a "parent" and a "child" from the same table, creates duplicate of the same table, and combines the two based on value match between the parent and the child.

To put it practically,

```sql
SELECT
  lt.fname,   -- First name of the parent
  lt.lname,   -- Last name of the parent
  rt.fname,   -- First name of the child
  rt.lname    -- Last name of the child
FROM database AS lt       -- Original table
LEFT JOIN database rt     -- Duplicated table
  ON rt.id = lt.id        -- Mutual identifier
/* ... 
Any kinds of conditionals can be inserted past this line 
*/
```