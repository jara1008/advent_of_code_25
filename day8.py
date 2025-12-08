import sys
import math

filename = 'day8.txt'

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()
        input = input.split('\n')
    input_triplets = []
    for line in input:
        input_triplets.append(line.split(','))
    return input_triplets

# Helperfunction
def closest_two(input):
    connections = []
    for i in range(len(input)-1):
        for j in range(i+1, len(input), 1):
            distance = ((int(input[i][0]) - int(input[j][0]))**2 + (int(input[i][1]) - int(input[j][1]))**2  + (int(input[i][2]) - int(input[j][2]))**2)**0.5 
            connections.append((input[i], input[j], distance))
    connections.sort(key=lambda x: x[2])
    return connections

def puzzle_1(input):
    circuits = []
    junction_nr = 1000
    connections = closest_two(input)
    for i in range(junction_nr):
        junction1, junction2, d = connections[i]
        add = False
        for c in circuits:
            if tuple(junction1) in c or tuple(junction2) in c: 
                c.update([tuple(junction1), tuple(junction2)])
                add = True
                break
        if not add:
            circuits.append({tuple(junction1), tuple(junction2)})
    merged = True
    while merged:
        merged = False
        new_circuits = []
        while circuits:
            first = circuits.pop(0)
            overlap = False
            for i in range(len(circuits)):
                other = circuits[i]
                if first & other:
                    circuits[i] = first | other
                    overlap = True
                    merged = True
                    break
            if not overlap:
                new_circuits.append(first)
        circuits = new_circuits
    circuits = sorted(circuits, key=len)
    return len(circuits[-1]) * len(circuits[-2]) * len(circuits[-3])

def puzzle_2(input):
    circuits = []
    connections = closest_two(input)
    all_junctions = set()
    for c in connections:
        junction1, junction2, d = c
        all_junctions.add(tuple(junction1))
        all_junctions.add(tuple(junction2))
    length = 0
    index = 0
    junction1, junction2, d = connections[0]
    while (len(circuits) > 1 or index < 3) or length < len(all_junctions):
        junction1, junction2, d = connections[index]
        add = False
        for c in circuits:
            if tuple(junction1) in c or tuple(junction2) in c: 
                c.update([tuple(junction1), tuple(junction2)])
                add = True
                break
        if not add:
            circuits.append({tuple(junction1), tuple(junction2)})
        index+=1
        merged = True
        while merged:
            merged = False
            new_circuits = []
            while circuits:
                first = circuits.pop(0)
                overlap = False
                for i in range(len(circuits)):
                    other = circuits[i]
                    if first & other:
                        circuits[i] = first | other
                        overlap = True
                        merged = True
                        break
                if not overlap:
                    new_circuits.append(first)
            circuits = new_circuits
        if len(circuits) == 1:
            length = len(circuits[0])
    return int(junction1[0]) * int(junction2[0])

input = read_input(filename)
res = puzzle_1(input)
print(f'Puzzle 1: {res}')
res = puzzle_2(input)
print(f'Puzzle 2: {res}')
