
filename = 'day1.txt'

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
        input = input.split('\n')
    return input

def puzzle_1(input):
    zeros = 0
    curr = 50
    for obj in input: 
        direction, distance = obj[:1], int(obj[1:])
        distance = distance % 100
        if direction == 'L':
            if curr - distance < 0:
                distance -= curr + 1
                curr = 99 - distance
            else:
                curr -= distance
        elif direction == 'R':
            if curr + distance > 99:
                distance -= (100-curr)
                curr = distance
            else: 
                curr += distance
        if curr == 0: zeros += 1
    return zeros

def puzzle_2(input):
    zeros = 0
    curr = 50
    index = 0
    for obj in input: 
        index += 1
        direction, distance = obj[:1], int(obj[1:])
        zeros += int(distance / 100)
        distance = distance % 100
        if direction == 'L':
            if curr - distance < 0:
                if curr == 0: zeros -= 1 # else some zeros are counted twice
                distance -= curr + 1
                curr = 99 - distance
                zeros += 1
            else:
                curr -= distance
                if curr == 0: zeros += 1
        elif direction == 'R':
            if curr + distance > 99:
                distance -= (100-curr)
                curr = distance
                zeros += 1
            else: 
                curr += distance
    return zeros

input = read_input(filename)
res = puzzle_1(input)
print(f'Puzzle 1: {res}')
res = puzzle_2(input)
print(f'Puzzle 2: {res}')

