
filename = 'day5.txt'

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
        input = input.split('\n\n')
    ranges = input[0].split('\n')
    numbers = input[1].split('\n')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    full_ranges = []
    for item in ranges:
        start, end = item.split('-')
        full_ranges.append([int(start), int(end)])
    return full_ranges, numbers

def puzzle_1(full_ranges, numbers):
    fresh_ids = 0
    for num in numbers:
        for arr in full_ranges:
            start, end = arr[0], arr[1]
            if num >= start and num <= end: 
                fresh_ids += 1
                break
    return fresh_ids

def puzzle_2(full_ranges):
    fresh_ids = 0
    sorted_list = sorted(full_ranges, key=lambda x: (x[0], -x[1]))
    prev_end = -1
    for arr in sorted_list:
        start, end = arr[0], arr[1]
        if end <= prev_end: continue # range is subrange of another range 
        new_start = start
        if start <= prev_end: # ranges overlap so we modify the startpoint
            new_start = prev_end+1
        fresh_ids += end - new_start + 1
        prev_end = end
    return fresh_ids

full_ranges, numbers = read_input(filename)
res = puzzle_1(full_ranges, numbers)
print(f'Puzzle 1: {res}')
res = puzzle_2(full_ranges)
print(f'Puzzle 2: {res}')

