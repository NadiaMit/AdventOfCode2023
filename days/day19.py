import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import re

# get daily input
day = helpers.get_current_day(__file__)
input = helpers.read_input(day, test=False)

# code for both parts
class Rating:
    ratings: dict = {}
    sum: int
    
    # parse rating string to object
    def __init__(self, rating: str):
        [x, m, a, s] = re.findall(r"\d+", rating)
        self.ratings = {
            "x": int(x),
            "m": int(m),
            "a": int(a),
            "s": int(s)
        }
        self.sum = int(x) + int(m) + int(a) + int(s)

class Condition:
    check: str = None
    send: str
    has_check: bool = False
    
    # parse condition string to object
    def __init__(self, condition: str):
        condition = condition.split(":")
        if len(condition) > 1:
            self.has_check = True
            self.check = condition[0]
            self.send = condition[1]
        else:
            self.send = condition[0]

# parse workflow string to workflow dict
def parse_workflow(dict, workflow):
    [name, conditions] = workflow.split("{")
    conditions = conditions.replace("}", "").split(",")
    conditions = [Condition(condition) for condition in conditions]
    dict[name] = conditions

workflows = {}

# find empty line in input
empty_line = input.index("")
# parse workflows from input
for workflow in input[:empty_line]:
    parse_workflow(workflows, workflow)
# parse ratings from input
ratings = [Rating(rating) for rating in input[empty_line+1:]]

# part 1
result_part_1 = 0

# get the sum of all parts that get accepted
for rating in ratings:
    workflow_name = "in"
    while workflow_name != "R" and workflow_name != "A":
        workflow = workflows[workflow_name]
        
        for condition in workflow:
            # if it has a check, evaluate it
            if condition.has_check:
                # if true, set the workflow name to the send value and break the loop
                if eval(condition.check, rating.ratings):
                    workflow_name = condition.send
                    break
            # if there is no check in the condition, just set the workflow name to the send value
            else:
                workflow_name = condition.send                
    
    # if workflow name is A, part is accepted and result gets the sum of the parts added
    if workflow_name == "A":
        result_part_1 += rating.sum

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 323625
print(f"Part 2: {result_part_2}")