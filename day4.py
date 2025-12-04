
filename = 'day4.txt'

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
        input = input.split('\n')
    number_array = []
    for line in input:
        arr = []
        for c in line:
            arr.append(c)
        number_array.append(arr)
    return number_array

def puzzle_1(input):
    sum = 0
    for i in range(len(input)):
        row = input[i]
        for j in range(len(row)):
            if input[i][j] == '.': continue
            adj = 0
            if i > 0 and j > 0 and input[i-1][j-1] == '@': adj += 1
            if i > 0 and j < len(row)-1 and input[i-1][j+1] == '@': adj += 1
            if i > 0 and input[i-1][j] == '@': adj += 1
            if i < len(input)-1 and j > 0 and input[i+1][j-1] == '@': adj += 1
            if i < len(input)-1 and j < len(row)-1 and input[i+1][j+1] == '@': adj += 1
            if i < len(input)-1 and input[i+1][j] == '@': adj += 1
            if j > 0 and input[i][j-1] == '@': adj += 1
            if j < len(row)-1 and input[i][j+1] == '@': adj += 1
            if adj < 4: sum += 1
    return sum

def puzzle_2(input):
    sum = 0
    cont = 1
    while cont:
        indicies_to_remove = []
        for i in range(len(input)):
            row = input[i]
            for j in range(len(row)):
                if input[i][j] == '.': continue
                adj = 0
                if i > 0 and j > 0 and input[i-1][j-1] == '@': adj += 1
                if i > 0 and j < len(row)-1 and input[i-1][j+1] == '@': adj += 1
                if i > 0 and input[i-1][j] == '@': adj += 1
                if i < len(input)-1 and j > 0 and input[i+1][j-1] == '@': adj += 1
                if i < len(input)-1 and j < len(row)-1 and input[i+1][j+1] == '@': adj += 1
                if i < len(input)-1 and input[i+1][j] == '@': adj += 1
                if j > 0 and input[i][j-1] == '@': adj += 1
                if j < len(row)-1 and input[i][j+1] == '@': adj += 1
                if adj < 4: 
                    sum += 1
                    indicies_to_remove.append((i, j))
        if indicies_to_remove == []: cont = 0
        for i in range(len(input)):
            row = input[i]
            for j in range(len(row)):
                if (i, j) in indicies_to_remove: 
                    input[i][j] = '.'
    return sum

input = read_input(filename)
res = puzzle_1(input)
print(f'Puzzle 1: {res}')
res = puzzle_2(input)
print(f'Puzzle 2: {res}')