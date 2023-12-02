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
    # split the line to get the game id and sets
    game, sets = line.split(':')
    
    # for every color find every amount using regex and from them get the maximum
    max_red = max([int(amount) for amount, _color in re.findall("(\d+) (red)", sets)])
    max_green = max([int(amount) for amount, _color in re.findall("(\d+) (green)", sets)])
    max_blue = max([int(amount) for amount, _color in re.findall("(\d+) (blue)", sets)])
    
    # part 1: check if the maximum of every color is smaller than the given numbers if so add the game ids to the result
    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        result_part_1 += int(re.findall("\d+", game)[0])
    
    # part 2: add the 'power' of all the maximum values
    result_part_2 += max_red*max_green*max_blue


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")