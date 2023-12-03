import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
def check_part(array, y, x, gearCheck=False):
    height = len(array)-1
    width =  len(array[0])-1
    
    # top
    if y > 0 and array[y-1][x] != '.' and not array[y-1][x].isdigit():
        if gearCheck and array[y-1][x] == '*':
            return (True, (y-1, x))
        elif not gearCheck:
            return (True, (y-1, x))
    
    # top right
    if y > 0 and x < width and array[y-1][x+1] != '.' and not array[y-1][x+1].isdigit():
        if gearCheck and array[y-1][x+1] == '*':
            return (True, (y-1, x+1))
        elif not gearCheck:
            return (True, (y-1, x+1))
    
    # right
    if x < width and array[y][x+1] != '.' and not array[y][x+1].isdigit():
        if gearCheck and array[y][x+1] == '*':
            return (True, (y, x+1))
        elif not gearCheck:
            return (True, (y, x+1))
    
    # bottom right
    if y < height and x < width and array[y+1][x+1] != '.' and not array[y+1][x+1].isdigit():
        if gearCheck and array[y+1][x+1] == '*':
            return (True, (y+1, x+1))
        elif not gearCheck:
            return (True, (y+1, x+1))
    
    # bottom
    if y < height and array[y+1][x] != '.' and not array[y+1][x].isdigit():
        if gearCheck and array[y+1][x] == '*':
            return (True, (y+1, x))
        elif not gearCheck:
            return (True, (y+1, x))
    
    # bottom left
    if y < height and x > 0 and array[y+1][x-1] != '.' and not array[y+1][x-1].isdigit():
        if gearCheck and array[y+1][x-1] == '*':
            return (True, (y+1, x-1))
        elif not gearCheck:
            return (True, (y+1, x-1))
    
    # left
    if x > 0 and array[y][x-1] != '.' and not array[y][x-1].isdigit():
        if gearCheck and array[y][x-1] == '*':
            return (True, (y, x-1))
        elif not gearCheck:
            return (True, (y, x-1))
    
    # top left
    if y > 0 and x > 0 and array[y-1][x-1] != '.' and not array[y-1][x-1].isdigit():
        if gearCheck and array[y-1][x-1] == '*':
            return (True, (y-1, x-1))
        elif not gearCheck:
            return (True, (y-1, x-1))
    
    return (False, (0,0))

lines = input.splitlines()

result_part_1 = 0
result_part_2 =  0

part = ''
is_part = False
is_gear_part = False

gears = []
part_gears = {}

for y in range(len(lines)):
    for x in range(len(lines[y])):
        # save part number for sum if its a digit
        if(lines[y][x].isdigit()):
            part+=lines[y][x]
            
            # check if its a part number
            check, _coordinates = check_part(lines, y, x)
            if check:
                is_part = True
            
            # check if it touches a gear
            check, coordinates = check_part(lines, y, x, gearCheck=True)
            if check:
                is_gear_part = True
                gears.append(coordinates)
        
        # if its not a digit
        else:
            # and it is indeed a part number, add it to the result
            if is_part:
                result_part_1 += int(part)
            
            # if it touched a gear add it to the list
            if is_gear_part:
                gear = gears[-1]
                if f"{gear}" in part_gears:
                    result_part_2 += part_gears[f"{gear}"] * int(part)
                else:
                    part_gears[f"{gear}"] = int(part)
            
            # reset part number value and check
            part =''
            is_part = False
            is_gear_part = False

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}")
print(f"Part 2: {result_part_2}")

