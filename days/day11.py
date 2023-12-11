import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import numpy as np

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
def expand_galaxies(galaxies, amount):
    # expand galaxies:
    # rows
    expanded_rows = np.zeros(len(galaxies), dtype=int)
    for y, row in enumerate(galaxies):
        expanded_rows[y] = expanded_rows[y-1]
        if '#' not in row:
            expanded_rows[y] += amount

    # colums
    expanded_cols = np.zeros(len(galaxies[0]), dtype=int)
    for x in range(len(galaxies[0])):
        col = galaxies[:, x]
        expanded_cols[x] = expanded_cols[x-1]
        if '#' not in col:
            expanded_cols[x] += amount
    
    return expanded_rows, expanded_cols

def manhatten_distance(first, second):
    y1, x1 = first
    y2, x2 = second
    return abs(y2 - y1) + abs(x2 - x1)

# convert to numpy 2d array
universe = np.array([list(line) for line in input])

# part 1
# expand the galaxies
expanded_rows, expanded_cols = expand_galaxies(universe, 1)

# get all galaxy positions
galaxies = list(zip(*np.where(universe == '#')))

# calculate sum of shortest paths between all pairs of galaxies
result_part_1 = 0

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        y1, x1 = galaxies[i]
        y2, x2 = galaxies[j]
        first = (y1 + expanded_rows[y1], x1 + expanded_cols[x1])
        second = (y2 + expanded_rows[y2], x2 + expanded_cols[x2])
        
        result_part_1 += manhatten_distance(first, second)

# part 2
# expand the galaxies
expanded_rows, expanded_cols = expand_galaxies(universe, 999999)

# get all galaxy positions
galaxies = list(zip(*np.where(universe == '#')))

# calculate sum of shortest paths between all pairs of galaxies
result_part_2 = 0

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        y1, x1 = galaxies[i]
        y2, x2 = galaxies[j]
        first = (y1 + expanded_rows[y1], x1 + expanded_cols[x1])
        second = (y2 + expanded_rows[y2], x2 + expanded_cols[x2])
        
        result_part_2 += manhatten_distance(first, second)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 10077850
print(f"Part 2: {result_part_2}") # 504715068438