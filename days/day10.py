import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
from enum import Enum

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
# direction enum
class DIRECTION(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# calculates new coordinates from direction and current coordinates
def next_coordinates(coordinates, direction):
    y, x = coordinates
    
    if direction == DIRECTION.UP:
        return (y-1, x)
    if direction == DIRECTION.DOWN:
        return (y+1, x)
    if direction == DIRECTION.LEFT:
        return (y, x-1)
    if direction == DIRECTION.RIGHT:
        return (y, x+1)

# calculates new direction from pipe and current direction
def next_direction(pipe, direction):
    if pipe == '|':
        return DIRECTION.UP if direction == DIRECTION.UP else  DIRECTION.DOWN
    if pipe == '-':
        return DIRECTION.LEFT if direction == DIRECTION.LEFT else DIRECTION.RIGHT
    if pipe == 'L':
        return DIRECTION.RIGHT if direction == DIRECTION.DOWN else DIRECTION.UP
    if pipe == 'J':
        return DIRECTION.LEFT if direction  == DIRECTION.DOWN else DIRECTION.UP
    if pipe == '7':
        return DIRECTION.LEFT if direction == DIRECTION.UP else DIRECTION.DOWN
    if pipe == 'F':
        return DIRECTION.RIGHT if direction == DIRECTION.UP else DIRECTION.DOWN


# find starting point S
start = (0, 0)
for y, row in enumerate(input):
    if 'S' in row:
        start = (y, row.index('S'))
        break


# find starting direction
y, x = start
direction = None

if y > 0:
    pipe = input[y-1][x]
    if pipe == '|' or pipe == 'F' or pipe == '7':
        direction = DIRECTION.UP
if y < len(input) - 1:
    pipe = input[y+1][x]
    if pipe == '|' or pipe == 'J' or pipe == 'L':
        direction = DIRECTION.DOWN
if x > 0:
    pipe = input[y][x-1]
    if pipe == '-' or pipe == 'F' or pipe == 'L':
        direction = DIRECTION.LEFT
if x < len(input[0]) - 1:
    pipe = input[y][x+1]
    if pipe == '-' or pipe == 'J' or pipe == '7':
        direction = DIRECTION.RIGHT

# take first step in direction
coords = next_coordinates(start, direction)
cycle = {start}
result_part_1 = 1

# go through all pipes until start is reached again and count the steps
while coords != start:
    y, x = coords
    pipe = input[y][x]
    direction = next_direction(pipe, direction)
    coords = next_coordinates(coords, direction)
    cycle.add(coords)
    result_part_1 += 1


# part 1
result_part_1 = int(result_part_1/2)

# part 2
result_part_2 = 0

# go through map and check if coordinate is inside the loop or not
for y in range(len(input)):
    inside = False
    # for L--7 and F--J pipes
    prev_pipe = ''
    
    for x in range(len(input[y])):
        # if a coordinate is not part of the pipe cycle and the inside the loop add it to the result
        if (y, x) not in cycle:
            if inside is True:
                result_part_2 += 1
        
        # if it's part of the cycle check what kind of pipe it is and handle inside loop boolean
        else:
            pipe = input[y][x]
            # handle cycle cases and set inside true respectively
            if pipe == '|':
                inside = not inside
            
            # check if L--7 or F--J pipes happen, since that is basically |
            elif pipe == 'L' or pipe == 'F':
                prev_pipe = pipe
            elif pipe == '7' or pipe == 'J':
                pipe_seq = prev_pipe + pipe
                if pipe_seq == 'L7' or pipe_seq == 'FJ':
                    inside = not inside
                else:
                    prev_pipe = ''


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 6815
print(f"Part 2: {result_part_2}") # 269