#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:10:00 2019

Integers, floats, methods for numeric data and casting
"""
# Aritmetic operations
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(3 % 2)

#sequence pf opertations is same as BODMAS

# changing a value
num = 3
num += 1
num *= 10

# built-in functions
print(abs(-3))
print(round(3.75))
print(round(3.75, 1)) #the scond argument tells upto how many integers after decimal

# Comparison
print(3 == 2)
print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)

# Strings that look like number
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)

# Convert the strings into numbers using CASTING
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)

