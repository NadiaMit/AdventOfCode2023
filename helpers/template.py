import sys
sys.path.insert(1, sys.path[0].replace('days', 'helpers'))
import helpers as helpers

# get daily input
day = helpers.getCurrentDay(__file__)
input = helpers.readInput(day, test=True)

# part 1
def part1():
    return 0

# part 2
def part2():
    return 0

# run both parts and print the results
print(f'--- Day {day}: ---')
print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')