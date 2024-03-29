## Unit Testing Assignment

by Patteera Likitamnuayporn

![Build status](https://travis-ci.org/mmookptr/unittesting-mmookptr.svg?branch=master)
[![codecov](https://codecov.io/gh/mmookptr/unittesting-mmookptr/branch/master/graph/badge.svg)](https://codecov.io/gh/mmookptr/unittesting-mmookptr)


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| what other test case?  |  what result?       |


## Test Cases for Fraction

### Test Case for INIT

| Test case              |  Expected Result    |
|------------------------|---------------------|
| (int) Numerator, (int) Denominator  |  Fraction(numerator,denominator)  |
| (not int) Numerator,Denominator |  NameError   |

### Test Case for STR

| Test case              |  Expected Result    |
|------------------------|---------------------|
| (int) Numerator, (int) Denominatotr | Numerator / Denominator  |
| (int) Numeratotr, Denominator = 1 |  Numerator   |
| (negative) Numerator, Denominator = 0 | -1/0 |
| (positive) Numerator, Denominator = 0 | 1/0 |
| Numerator = 0 , (non-zero) Denominator | 0 |

### Test Case for ADD

| Test Case              |  Expected Result    |
|------------------------|---------------------|
| (Non-zero) Fraction added together | (Non-zero) Fraction |
| 1/0 added with (Non-zero) Fraction | 1/0 |
| -1/0 added with (Non-zero) Fraction | -1/0 |
| 1/0 added with -1/0 | 0/0 |

### Test Case for MUL 

| Test Case              |  Expected Result    |
|------------------------|---------------------|
| (Non-zero) Fraction multiply together | (Non-zero) Fraction |
| (Non-zero) Fraction multiply by 0 | 0 | 
| 1/0 or -1/0 multiply by (Non-zero) Fraction | 1/0 or -1/0 |
| 1/0 or -1/0 multiply tpogether | 1/0 or -1/0 |

### Test Case for EQ 

| Test Case              |  Expected Result    |
|------------------------|---------------------|
| Functions with the same simple form compare together | True |
| Functions with different simple form compare together | False |





