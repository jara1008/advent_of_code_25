
filename = 'day2.txt'

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
        input = input.split(',')
    return input

def puzzle_1(input):
    sum = 0
    for obj in input:
        numrange = obj.split('-')
        start, end = int(numrange[0]), int(numrange[1])
        for i in range(start, end + 1):
            numstr = str(i)
            if numstr.startswith('0'): print("invalid")
            firstpart, secondpart = numstr[:len(numstr)//2], numstr[len(numstr)//2:]
            if firstpart == secondpart: 
                sum += i
    return sum

# Helperfunction
def check_same_seq(s, numstring):
    first = numstring[:s]
    if len(numstring) < 2*s: return False
    for i in range(s, len(numstring), s):
        if numstring[i:i+s] != first:
            return False
    return True

def puzzle_2(input):
    sum = 0
    for obj in input:
        numrange = obj.split('-')
        start, end = int(numrange[0]), int(numrange[1])
        for i in range(start, end + 1):
            numstr = str(i)
            seq_sizes = [s for s in (1,2,3,4,5) if len(numstr) % s == 0]
            for s in seq_sizes:
                if check_same_seq(s, numstr):
                    sum += i
                    break
    return sum

input = read_input(filename)
res = puzzle_1(input)
print(f'Puzzle 1: {res}')
res = puzzle_2(input)
print(f'Puzzle 2: {res}')
