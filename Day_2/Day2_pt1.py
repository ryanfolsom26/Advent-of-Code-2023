#!/usr/bin/python3

import os
import re

input_path = os.path.join(os.path.dirname(__file__), "Day2_input.txt")
input_file = open(input_path, "r")
values = input_file.readlines()

r_cubes = 12
g_cubes = 13
b_cubes = 14

re_pattern = r"\d+ (red|green|blue)"
possible_games = 0 

for game in values:
    game_id = game.split(" ")[1][:-1]
    matches = [m.group() for m in re.finditer(re_pattern, game)]
    is_possible = True
    for match in matches:
        (n, color) = match.split(" ")
        if (
            (color == "red" and int(n) > r_cubes)
            or (color == "green" and int(n) > g_cubes)
            or (color == "blue" and int(n) > b_cubes)
        ) :
            is_possible = False
            break
    if is_possible:
        possible_games += int(game_id)

print("Sum of possible games: ", possible_games)