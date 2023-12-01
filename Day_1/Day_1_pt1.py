#!/usr/bin/python3

ans = 0
with open('Puzzle_Input.txt') as f:
    for line in f:
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(c)
        score = int(digits[0]+digits[-1])
        ans += score
    print(ans)