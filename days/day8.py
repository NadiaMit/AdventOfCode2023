import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import re

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
# parse instructions
instructions = input[0]

# parse nodes into dictionary
nodes = {}
for line in input[2:]:
    # use regex to match node, left and right
    node, left, right = re.findall(r"\b\w{3}\b", line)
    nodes[node] = (left, right)


# go through nodes starting at AAA until ZZZ is reached and count number of steps
result_part_1 = 0

curr_node = 'AAA'
goal_node = 'ZZZ'
step_idx = 0

while curr_node != goal_node:
    # get left and right child nodes of current node
    left, right = nodes[curr_node]
    
    # next step = left
    if instructions[step_idx] == 'L':
        curr_node = left
        
    # next step = right
    elif instructions[step_idx] == 'R':
        curr_node = right
    
    # increment step counter
    result_part_1 += 1
    
    # increment step index
    if (step_idx + 1) == len(instructions):
        step_idx = 0
    else:
        step_idx += 1

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")