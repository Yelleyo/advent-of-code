input_file = 'test_input.txt'

lines = []

# Put input into an array of lines
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.strip())

lin = []
for i, line in enumerate(lines):
    if not '#' in line: 
        lin.append(i)

print('line separtion: ', lin)

col = []
for i in range(len(lines[0])):
    if all(line[i] == '.' for line in lines):
        col.append(i)

print('colomn seperation: ', col)

#exit()

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
        vertical_distance = abs(positions[i][0] - positions[j][0])
        horizontal_distance = abs(positions[i][1] - positions[j][1])
        total_distance = vertical_distance + horizontal_distance
        distances.append(total_distance)

print("Distances between all points:", distances)

total = sum(distances)
print(total)


# for each values under the separtion line, add 1000 000 for each values above the separtion line 
# for each seperation line. horizontaly and vertivaly
# under line 3
vert_added = 0
for l in lin:
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            if positions[i][0] < l and positions[j][0] > l:
                vert_added += 100

hor_added = 0
for c in col:
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            if positions[i][1] < c and positions[j][0] > c:
                hor_added += 100

total_added = total + vert_added + hor_added
print(total_added)

# close but no sigar!