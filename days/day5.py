import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, split_lines=False, test=False)

# code for both parts
# parse seeds and mappings
instructions = input.split('\n\n')
initial_seeds = [int(seed) for seed in instructions[0].split(':')[1].split()]
mapping_lists = []

for instruction in instructions[1:]:
    # parse mapping steps
    mapping_lines = instruction.split(':\n')[1]
    mappings = []
    for line in mapping_lines.split('\n'):
        mappings.append([int(num) for num in line.split()])
    
    # sort mappings from smallest range start to largest
    mappings.sort(key=lambda x: x[1])
    mapping_lists.append(mappings)



# part 1
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

# parse seeds into set
seeds = set(initial_seeds)

# loop through mapping of every step
for mappings in mapping_lists:
    # calculate the new seed values for every mapping step
    seeds = {get_mapping(mappings, seed) for seed in seeds}

result_part_1 = min(seeds)


# part 2
# reparse seeds
seeds = []
for i in range(0, len(initial_seeds), 2):
    seeds.append((initial_seeds[i], initial_seeds[i+1]))

# loop through mapping of every step
for mappings in mapping_lists:
    # calculate the new seed values for every mapping step
    i = 0
    # used while loop, because for loop doesn't work with changed lists
    while i < len(seeds):
        # get seed range start, range length and seed range end
        start_seed, seed_range = seeds[i]
        end_seed = start_seed + seed_range - 1
        
        # for every mapping in the mapping list check
        for mapping_step in mappings:
            start_destination, start_mapping, length = mapping_step
            end_mapping = (start_mapping + (length - 1))
            end_destination = (start_destination + (length - 1))
            
            # whole seed range is inside mapping range, map the whole range
            if start_mapping <= start_seed <= end_seed <= end_mapping:
                seeds[i] = (start_destination + (start_seed - start_mapping), seed_range)
                break
            
            # first part is inside mapping range, map first part
            elif start_mapping <= start_seed <= end_mapping <= end_seed:
                first_range = end_mapping - start_seed
                # create new range for second part
                seeds.append((start_seed + first_range + 1, seed_range - first_range))
                # map first part
                seeds[i] = (start_destination + (start_seed - start_mapping), first_range)
                break
            
            # second part is inside mapping range, map second part
            elif start_seed <= start_mapping <= end_seed <= end_mapping:
                second_range = end_mapping - end_seed
                # create new range for first part
                seeds.append((start_seed, seed_range - second_range))
                # map second part
                seeds[i] = (start_destination + (end_seed - start_mapping), second_range)
                break

            # mapping range is inside seed range
            elif start_seed <= start_mapping <= end_mapping <= end_seed:
                # create new first outer part
                first_range = start_mapping - start_seed
                second_range = end_mapping - start_mapping
                third_range = end_seed - end_mapping
                
                # map inner part
                seeds.append((start_mapping, second_range))
                
                # create new third part
                seeds.append((end_mapping, third_range))
                
                # set new range
                seeds[i] = (start_seed, first_range)
                break
        
        # increment counder
        i+=1
    
result_part_2 = min([seed_start for seed_start, _range_len in seeds])

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 261668924
print(f"Part 2: {result_part_2}") # 24261545