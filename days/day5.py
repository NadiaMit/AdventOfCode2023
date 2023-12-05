import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
def calculate_seed_locations(instruction_list, seeds):
    # loop through mapping of every step
    for instruction in instruction_list:
        # parse mapping steps
        mapping_list = instruction.split(':\n')[1]
        mapping = []
        for line in mapping_list.split('\n'):
            mapping.append([int(num) for num in line.split()])
        
        # calculate the new seed values for every mapping step
        seeds = [get_mapping(mapping, seed) for seed in seeds]
    
    return seeds

def get_mapping(mapping_list, seed):
    return_value = 0    
    # for every mapping in the mapping list
    for mapping in mapping_list:
        destination, source, length = mapping 
        
        # check if seed value is in the source range
        if source <= seed <= (source + (length - 1)):
            # calculate new seed value
            return_value = destination + (seed-source)
    
    return return_value if return_value != 0 else seed


instructions = input.split('\n\n')
# parse seeds into set
seeds = {int(seed) for seed in instructions[0].split(':')[1].split()}

# part 1
result_part_1 = min(calculate_seed_locations(instructions[1:], seeds))

# part 2
result_part_2 = 0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 261668924
print(f"Part 2: {result_part_2}")