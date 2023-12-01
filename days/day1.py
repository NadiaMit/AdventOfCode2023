import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

import re

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
calibration_values = []

# part 1
for line in input.splitlines():
    digits = [char for char in line if char.isdigit()]
    calibration_values.append(int(digits[0]+digits[-1]))

result_part_1 = sum(calibration_values)


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

calibration_values = []

for line in input.splitlines():
    digits = []
    for key, value in string_digits.items():
        idx = [m.start() for m in re.finditer(key, line)]
        if(len(idx) != 0):
            for i in idx:
                digits.append([f"{value}", i])
    
    digits.sort(key=lambda x: x[1])
    calibration_values.append(int(digits[0][0] + digits[-1][0]))

result_part_2 = sum(calibration_values)

# run both parts and print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")