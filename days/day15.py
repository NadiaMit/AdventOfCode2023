import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
# part 1
result_part_1 = 0

for sequence in input[0].split(','):
    # set curr_value to 0
    curr_value = 0
    
    for char in sequence:
        # calculate ASCII number, multiply by 17 and calculate remainder when dividing by 265
        curr_value = ((curr_value + ord(char)) * 17 ) % 256
    
    result_part_1 += curr_value


# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 512950
print(f"Part 2: {result_part_2}")