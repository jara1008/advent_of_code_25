
filename = 'day3.txt'

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
        input = input.split('\n')
    number_array = []
    for line in input:
        arr = []
        for c in line:
            arr.append(int(c))
        number_array.append(arr)
    return number_array

def puzzle_1(input):
    sum = 0
    for row in input:
        max = 0
        index_first = -1
        for i in range(len(row)-1):
            if row[i] > max:
                max = row[i]
                index_first = i
        firstpart = str(row[index_first])
        max = 0
        index_second = -1
        for i in range(index_first+1, len(row)):
            if row[i] > max:
                max = row[i]
                index_second = i
        secondpart = str(row[index_second])
        full_number = firstpart + secondpart
        sum += int(full_number)
    return sum

def puzzle_2(input):
    sum = 0
    for row in input:
        joltage = ""
        index = -1
        for a in range(11, -1, -1):
            max = 0
            for i in range(index + 1, len(row)-a, 1):
                if row[i] > max:
                    max = row[i]
                    index = i
            joltage += str(row[index])
        sum += int(joltage)
    return sum

input = read_input(filename)
res = puzzle_1(input)
print(f'Puzzle 1: {res}')
res = puzzle_2(input)
print(f'Puzzle 2: {res}')