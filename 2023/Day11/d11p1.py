input_file = 'test_input.txt'

lines = []

# Put input into an array of lines
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.strip())

new_lines = []

for line in lines:
    if not '#' in line: 
        new_lines.append('zzzzzzzzzz')
        new_lines.append(line)
    else:
        new_lines.append(line)

lines = new_lines
print(lines)

new_lines = []
c = 0
col = []
for i in range(len(lines[0])):
    if all(line[i] == 'z' for line in lines):
        col.append(i)

#print(col)

for line in lines:
    for i, c in enumerate(col):
        line = line[:c + i] + '.' + line[i + c:] 
    new_lines.append(line)

lines = new_lines
for line in lines: 
    print(line)

# get position of each # and loop through dict starting from this values. 
positions = []
for line_num, line in enumerate(lines):
    for char_num, char in enumerate(line):
        if char == '#':
            positions.append([line_num, char_num])

print(positions)

distances = []
for i in range(len(positions)):
    for j in range(i+1, len(positions)):
        distance = abs(positions[i][0]-positions[j][0]) + abs(positions[i][1]-positions[j][1])
        distances.append(distance)

print("Distances between all points:", distances)

total = sum(distances)
print(total)