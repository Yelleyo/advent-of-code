from itertools import product

input_file = 'input.txt'

lines = []
codes = []
counter = 0

with open(input_file, 'r') as file:
    for line in file:
        parts = line.split(' ')
        lines.append(parts[0])
        codes.append(list(map(int, parts[1].split(','))))
print(f'Those are the lines: {lines}')
print(f'Those are the codes: {codes}')

for i, line in enumerate(lines):
    num_question_marks = line.count('?')
    # generate all combinations of '.' and '#' of length num_question_marks
    combinations = product('.#', repeat=num_question_marks)
    # for each combination, replace the '?' characters in the original string
    for combination in combinations:
        temp_s = line
        for c in combination:
            temp_s = temp_s.replace('?', c, 1)
        if tuple(len(p) for p in temp_s.split('.') if p) == tuple(codes[i]):
            counter += 1
            print(f'line {temp_s}: counter: {counter}')








