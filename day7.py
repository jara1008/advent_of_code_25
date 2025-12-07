from functools import lru_cache
filename = 'day7.txt'

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
        input = input.split('\n')
    return input

def puzzle_1(input):
    start = -1
    for i in range(len(input[0])):
        if input[0][i] == 'S': start = i
    beams = set()
    beams.update([(0, start)])
    splits = set()
    while len(beams):
        beam = beams.pop()
        row = beam[0]+1
        col = beam[1]
        while input[row][col] == '.' and row < len(input)-1: row += 1
        if row < len(input)-1:
            if col-1 >= 0: beams.update([(row, col-1)])
            if col+1 < len(input[0]): beams.update([(row, col+1)])
            splits.update([(row, col)])
    return len(splits)

# Helperfunction
@lru_cache(None)
def count_paths(row, col):
    row += 1 
    while input[row][col] == '.' and row < len(input)-1: row += 1
    if row == len(input)-1: return 1
    timelines = 0
    if col-1 >= 0: timelines += count_paths(row, col-1)
    if col+1 < len(input[0]): timelines += count_paths(row, col+1)
    return timelines

def puzzle_2(input):
    start = -1
    for i in range(len(input[0])):
        if input[0][i] == 'S': start = i
    timelines = count_paths(0, start)
    return timelines

input = read_input(filename)
res = puzzle_1(input)
print(f'Puzzle 1: {res}')
res = puzzle_2(input)
print(f'Puzzle 2: {res}')
