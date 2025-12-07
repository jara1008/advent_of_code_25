
filename = 'day6.txt'

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
        input = input.split('\n')
    input_clean = []
    for i in input:
        arr = i.split('\n')
        for a in arr: 
            to_append = a.strip().split()
            input_clean.append(to_append)
    return input_clean, input

def puzzle_1(input):
    sum = 0
    for i in range(len(input[0])):
        sign = input[len(input)-1][i]
        if sign == '+':
            curr = 0
        else:
            curr = 1
        for j in range(len(input)-1):
            if sign == '+':
                curr += int(input[j][i])
            else:
                curr *= int(input[j][i])
        sum += curr
    return sum

def puzzle_2(input, ops):
    sum = 0
    pointer_ops = len(ops)-1
    rows = len(input)-1
    to_add = 1
    for i in range(len(input[0])-1, -2, -1):
        sign = ops[pointer_ops]
        add = False
        if sign == '+': add = True 
        num = ''
        for j in range(rows):
            num += input[j][i]
        if num == rows * ' ' or i == -1:
            if add: sum -= 1 
            sum += to_add
            to_add = 1
            pointer_ops -= 1
        elif add: 
            to_add += int(num)
        else: 
            to_add *= int(num)
    return sum

input_clean, input = read_input(filename)
res = puzzle_1(input_clean)
print(f'Puzzle 1: {res}')
ops = input_clean[len(input_clean)-1]
res = puzzle_2(input, ops)
print(f'Puzzle 2: {res}')
