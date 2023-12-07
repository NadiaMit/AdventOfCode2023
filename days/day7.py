import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
from enum import Enum

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
# enum for type of hand and value
class E_Hand_Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

# dict for sorting part 1
sort_1_dict = {
    '2': 'A',
    '3': 'B',
    '4': 'C',
    '5': 'D',
    '6': 'E',
    '7': 'F',
    '8': 'G',
    '9': 'H',
    'T': 'I',
    'J': 'J',
    'Q': 'K',
    'K': 'L',
    'A': 'M'
}

# dict for sorting part 2
sort_2_dict = {
    'J': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '7': 'G',
    '8': 'H',
    '9': 'I',
    'T': 'J',
    'Q': 'K',
    'K': 'L',
    'A': 'M'
}

def calculate_type(cards, part):
    card_amounts = []
    joker_amount = 0
    
    # extract card amounts and (joker amounts if part 2) from cards
    for card in set(cards):
        if part == 2 and card == 'J':
            joker_amount = cards.count(card)
        else:
            card_amounts.append(cards.count(card))
    
    # use joker cards to get strogest card if part 2
    if part == 2:
        if joker_amount == 5:
            card_amounts.append(5)
        else:
            max_count = max(card_amounts)
            max_idx = card_amounts.index(max_count)
            card_amounts[max_idx] = max_count + joker_amount
    
    # sort card_amounts for better comparability
    card_amounts.sort()
    
    # check if cards are of type HIGH_CARD
    if card_amounts == [1, 1, 1, 1, 1]:
        return E_Hand_Type.HIGH_CARD
    
    # check if cards are of type ONE_PAIR
    if card_amounts == [1, 1, 1, 2]:
        return E_Hand_Type.ONE_PAIR
    
    # check if cards are of type TWO_PAIR
    if card_amounts == [1, 2, 2]:
        return E_Hand_Type.TWO_PAIR
    
    # check if cards are of type THREE_OF_A_KIND
    if card_amounts == [1, 1, 3]:
        return E_Hand_Type.THREE_OF_A_KIND
    
    # check if cards are of type FULL_HOUSE
    if card_amounts == [2, 3]:
        return E_Hand_Type.FULL_HOUSE
    
    # check if cards are of type FOUR_OF_A_KIND
    if card_amounts == [1, 4]:
        return E_Hand_Type.FOUR_OF_A_KIND
    
    # check if cards are of type FIVE_OF_A_KIND
    if card_amounts == [5]:
        return E_Hand_Type.FIVE_OF_A_KIND

# convert cards to sort string using sort_dict values
def convert_to_sort_string(cards, part):
    sorting_list = []
    
    if part == 1:
        sorting_list = [sort_1_dict[card] for card in cards]
    if part == 2:
        sorting_list = [sort_2_dict[card] for card in cards]
    
    return ''.join(sorting_list)

# hand class for better handling of all values and sorting
class Hand:
    cards: str
    bid: int
    type: E_Hand_Type
    sort_string: str
    
    # constructor
    def __init__(self, cards, bid, part):
        self.cards = cards
        self.bid = bid
        # calculate type
        self.type = calculate_type(cards, part)
        # convert cards to sortstring
        self.sort_string = convert_to_sort_string(cards, part)


# part 1
# parse hands as touple of cards and bid value
hands = [Hand(cards, int(bid), 1) for line in input for cards, bid in [line.split()]]

# sort hands based on type and secondly based on the value of the cards
hands.sort(key=lambda x: ([x.type.value], [x.sort_string]))

# calculate each value using the rank = index + 1 and the bid number of the cards, then sum it up
result_part_1 = sum([hand.bid * (index+1) for index, hand in enumerate(hands)])


# part 2
# parse hands as touple of cards and bid value
hands = [Hand(cards, int(bid), 2) for line in input for cards, bid in [line.split()]]

# sort hands based on type and secondly based on the value of the cards
hands.sort(key=lambda x: ([x.type.value], [x.sort_string]))

# calculate each value using the rank = index + 1 and the bid number of the cards, then sum it up
result_part_2 = sum([hand.bid * (index+1) for index, hand in enumerate(hands)])

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 251216224
print(f"Part 2: {result_part_2}") # 250825971