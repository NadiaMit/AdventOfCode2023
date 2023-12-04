import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import re
import numpy as np

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
result_part_1 = 0
card_instances = np.ones(len(input.splitlines()), dtype=int)

for line in input.splitlines():
    card, numbers = line.split(': ') 
    
    # parse card number
    card = int(re.findall('\d+', card)[0]) 
    
    # parse winning and my numbers
    winning_numbers, my_numbers = numbers.split(' | ')
    winning_numbers = [number for number in winning_numbers.split(' ') if number != '']
    my_numbers = [number for number in my_numbers.split(' ') if number != '']
    
    is_first = True
    card_value = 0
    num_wins = 0
    
    # for every winning number, check if i have them in my numbers (better performance than the other way round)
    for num in winning_numbers:
        if num in my_numbers:
            # if its the first simply add 1
            if is_first:
                card_value += 1
                is_first = False
            # else double the card value
            else:
                card_value *= 2
            # add win to win counter
            num_wins += 1
            
    # part 1
    result_part_1 += card_value
    
    # part 2
    if num_wins > 0:
        # create all the copies and save them in an array
        for i in range(card, card + num_wins):
            if i < len(card_instances):
                card_instances[i] += card_instances[card-1]

# part 2
result_part_2 = sum(card_instances)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 21485
print(f"Part 2: {result_part_2}") # 11024379