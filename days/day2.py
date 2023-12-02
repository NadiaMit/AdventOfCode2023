import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

import re

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
result_part_1 = 0
result_part_2 =  0

for line in input.splitlines():
    game, sets = line.split(':')
    max_red = max([int(amount.split(' ')[0]) for amount in re.findall("\d+ red", sets)])
    max_green = max([int(amount.split(' ')[0]) for amount in re.findall("\d+ green", sets)])
    max_blue = max([int(amount.split(' ')[0]) for amount in re.findall("\d+ blue", sets)])
    
    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        result_part_1 += int(re.findall("\d+", game)[0])
    
    result_part_2 += max_red*max_green*max_blue


# run both parts and print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")