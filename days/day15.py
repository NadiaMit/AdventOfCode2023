import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import re

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
def HASH(char_sequence):
    hash_value = 0
    for char in char_sequence:
        # calculate ASCII number, multiply by 17 and calculate remainder when dividing by 265
        hash_value = ((hash_value + ord(char)) * 17 ) % 256
    return hash_value

def find_index(list, search_label):
    index = -1
    for i, lens in enumerate(list):
        if lens[0] == search_label:
            index = i
    return index

# initialize part 1 result
result_part_1 = 0

# initialize hash map
HASHMAP = {key: [] for key in range(256)}

# for every sequence in the input string
for sequence in input[0].split(','):
    # part 1
    # simply sum up all hash values of the sequences
    result_part_1 += HASH(sequence)
    
    # part 2
    # divide input sequence into its 3 parts
    [label, operation, length] = re.split(r'([-=])', sequence)
    
    # calculate the labels hash value
    hash = HASH(label)
    
    # depending on the operation, either insert/replace lens or remove lense
    index = find_index(HASHMAP[hash], label)
    if operation == '-':
        if index > -1:
            HASHMAP[hash].pop(index)
    elif operation == '=':
        lense = (label, int(length))
        # replace lense
        if index > -1:
            HASHMAP[hash][index] = lense
        # simply add lense
        else:
            HASHMAP[hash].append(lense)

result_part_2 =  0
# calulate focusing power
for box, lenses in HASHMAP.items():
    for i, (_label, length) in enumerate(lenses):
        result_part_2 += (box+1) * (i+1) * length

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 512950
print(f"Part 2: {result_part_2}") # 247153