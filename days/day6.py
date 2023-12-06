import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import math

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
# parse times and distances
times = input[0].strip().split(':')[1].split()
distances = input[1].strip().split(':')[1].split()

# calculate the number of ways to win
def calculate_num_ways(time, distance):
    # use quadratic formula
    sqare_root = math.sqrt(time**2 - (4 * distance))
    min = int(((-time) + sqare_root)/-2)
    max = int(((-time) - sqare_root)/-2)
    
    return (max - min)

# part 1
result_part_1 = 1

# for every race calculate the number of ways to win and multiply them
for i in range(len(times)):
    result_part_1 *=  calculate_num_ways(int(times[i]), int(distances[i]))

# part 2
# repartse time and distance of race
time = int(''.join(times))
distance = int(''.join(distances))

# calculate number of ways to win for the race
result_part_2 = calculate_num_ways(time, distance)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 2065338
print(f"Part 2: {result_part_2}") # 34934171