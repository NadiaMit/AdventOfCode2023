import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
almanac = {
    'seed-to-soil map': [],
    'soil-to-fertilizer map': [],
    'fertilizer-to-water map': [],
    'water-to-light map': [],
    'light-to-temperature map': [],
    'temperature-to-humidity map': [],
    'humidity-to-location map': [],
}

def get_mapping(mapping, seed):
    return_value = 0    
    for map in mapping:
        destination, source, length = map 
        if source <= seed <= (source+(length-1)):
            return_value = destination + (seed-source)
        
    
    return return_value if return_value != 0 else seed

seeds = []
instructions = input.split('\n\n')

# get seeds from input
seeds = [int(seed) for seed in instructions[0].split(':')[1].split()]

# get mappings from input and save in dictionary
for i in range(1, len(instructions)):
    step, mapping_list = instructions[i].split(':\n')
    mapping = []
    for line in mapping_list.split('\n'):
        mapping.append([int(num) for num in line.split()])
        
    almanac[step] = mapping

result_part_1 = 0

for seed in seeds:
    curr_value = seed
    for key, values in almanac.items():
        curr_value = get_mapping(values, curr_value)
    
    if result_part_1 > curr_value or result_part_1 == 0:
        result_part_1 = curr_value


# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")