#!/usr/bin/python3

# games possible if bag contains the following:
# 12 red cubes
# 13 green cubes
# 14 blue cubes

# Goal: identify possible games and get sum of game IDs

import re

# function to sum up arrays of each cube after converted to INTs

def red_sum(arr):
    red_total = 0
    for num in arr:
        red_total += num
    return red_total

def blue_sum(arr):
    blue_total = 0
    for num in arr:
        blue_total += num
    return blue_total

def green_sum(arr):
    green_total = 0
    for num in arr:
        green_total += num
    return green_total


test_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
red = re.findall(r"(\d+)(?=\s*red)", test_string)
red_int = []
for i in range(len(red)):
    t = int(red[i])
    red_int.append(t)
print(red_sum(red_int))

blue = re.findall(r"(\d+)(?=\s*blue)", test_string)
blue_int = []
for i in range(len(blue)):
    t = int(blue[i])
    blue_int.append(t)
print(blue_sum(blue_int))

green = re.findall(r"(\d+)(?=\s*green)", test_string)
green_int = []
for i in range(len(green)):
    t = int(green[i])
    green_int.append(t)
print(green_sum(green_int))

# add logic to compare if game is possible

