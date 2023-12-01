import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

import re

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)


# part 1
result_part_1 = 0

for line in input.splitlines():
    digits = [char for char in line if char.isdigit()]
    result_part_1 += int(digits[0] + digits[-1])


# part 2
string_digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

result_part_2 = 0

for line in input.splitlines():
    digits = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
    result_part_2 += string_digits[digits[0]]*10 + string_digits[digits[-1]]


# run both parts and print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")