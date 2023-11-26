
# get current day number
def getCurrentDay(file_path):
    return file_path.split('\\')[-1].split('.')[0].replace('day', '')

# reads input from the current days txt file
def readInput(day, test=False):
    path = f'./inputs/day{day}.txt' if not test else f'./inputs/test.txt'
    with open(path, 'r') as file:
        return file.read().splitlines()