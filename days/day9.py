import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
# subtraction function for part 2
def sub(list):
    value = 0
    sign = 1
    for num in list:
        value += num*sign
        sign *= -1
    
    return value

# inizialize both results
result_part_1 = 0
result_part_2 =  0

# for every line in input
for line in input:
    # parse line as int array
    numbers = [int(num) for num in line.split()]
    
    # save the first and last numbers for before and after history
    first_nums = [numbers[0]]
    last_nums = [numbers[-1]]
    
    # calculate difference of numbers until all values are zero
    all_zeros = False
    while not all_zeros:
        # calculate differences of current numbers
        diff = []
        for i in range(0, len(numbers)-1):
            diff.append(numbers[i+1] - numbers[i])
        
        # set numbers to be the differences
        numbers = diff
        
        # save first and last number seperately for before and after history
        first_nums.append(numbers[0])
        last_nums.append(numbers[-1])
        
        # check if all numbers are zero
        if numbers.count(0) == len(numbers):
            all_zeros = True
    
    # part 1
    result_part_1 += sum(last_nums)
    
    # part 2
    result_part_2 += sub(first_nums)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 1666172641
print(f"Part 2: {result_part_2}") # 933