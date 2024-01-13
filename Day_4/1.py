#!/usr/bin/python3

import re

with open('Advent-of-Code-2023/Day_4/Day4_input.txt') as f:
    input = f.read()

def totalscore(input):
    regex = r':(.*)\|(.*)'
    points = 0
    for win_nums, true_nums in re.findall(regex, input):
        overlap = set(win_nums.split()) & set(true_nums.split())
        if overlap:
            points += 2 ** (len(overlap) -1)
    return points

print('Total: ', totalscore(input))