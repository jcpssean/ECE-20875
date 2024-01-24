#!/usr/bin/python3
import math
n = 21
# Your code should be below this line

h = n + 13 * (13 + 1) // 5 + (2021 % 100) + (2021 % 100) // 4 + (2021 // 100) // 4 + 5 * (2021 // 100)
h = h % 7

if n < 1 or n > 31:
    print("Not valid")
elif h < 2:
    print("Weekend")
else:
    print("Weekday")
