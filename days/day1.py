import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

import re

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)


# part 1
result_part_1 = 0

for line in input:
    # get out all digits of the line
    digits = [char for char in line if char.isdigit()]
    # add only the first and last digit to the result
    result_part_1 += int(digits[0] + digits[-1])


# part 2
# dictionary for simpler string-to-int conversion
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

for line in input:
    # find all occourences of a number or written number in the string (even if overlapping or double)
    digits = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
    # add only the first and last digit to the result
    result_part_2 += string_digits[digits[0]]*10 + string_digits[digits[-1]]


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 55607
print(f"Part 2: {result_part_2}") # 55291