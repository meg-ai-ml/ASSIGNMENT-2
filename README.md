## ASSIGNMENT-2
## Largest of Three Numbers

A beginner-friendly Python program that asks the user for three numbers and tells them which one is the largest, using if, elif and else conditional logic.

## Overview

This project was created as a programming assignment to practice decision-making in Python. 
The program reads three numbers from the user, compares them, and prints the name of the variable (a,b or c) that holds the largest value.

## Features

1. Accepts three numbers from the user through the command line
2. Converts input to integers so numbers are compared by value, not alphabetically.
3. Uses chained conditions (if,elif and else) with the and operator
4. Commented code that explains each step



### Prerequisites

[Python 3.x](https://www.python.org/downloads/) installed on your computer



## How It Works

```
Start
  │
  ▼
Read a, b, c from the user
  │
  ▼
Is a > b AND a > c? ──Yes──► "a is the largest number"
  │ No
  ▼
Is b > a AND b > c? ──Yes──► "b is the largest number"
  │ No
  ▼
"c is the largest number"
  │
  ▼
End
```

1. The user enters three numbers, which are converted to integers.
2. The program checks whether `a` is greater than both `b` and `c`.
3. If not, it checks whether `b` is greater than both `a` and `c`.
4. If neither is true, `c` must be the largest, so the `else` branch handles it.



## Test Cases

| a  | b  | c  | Expected output            |
|----|----|----|----------------------------|
| 10 | 5  | 3  | `a is the largest number`  |
| 4  | 20 | 8  | `b is the largest number`  |
| 1  | 2  | 30 | `c is the largest number`  |
| 9  | 10 | 2  | `b is the largest number`  |
| -5 | -2 | -9 | `b is the largest number`  |


## What I Learned

1. Reading user input with `input()` and converting it with `int()`
2. Why input must be converted before comparing numbers (`"9" > "10"` is `True` for strings)
3. Using comparison operators and the logical `and` operator
4. Structuring decisions with `if`, `elif`, and `else`
5. Writing clear comments to document code

## 👤 Author

Meghana Thalakola 
