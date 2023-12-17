input_file = 'test_input.txt'

lines = []

# Put input into an array of lines
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.strip())

new_lines = []

for line in lines:
    if not '#' in line: 
        new_lines.append(line)
        new_lines.append(line)
    else:
        new_lines.append(line)

lines = new_lines
print(lines)

new_lines = []
c = 0
col = []
for i in range(len(lines[0])):
    if all(line[i] == '.' for line in lines):
        col.append(i)

print(col)
exit()


for line in lines:
    line = line[:i + c] + 'z' + line[i + c:] 
    new_lines.append(line)
c =+ 1
lines = new_lines
print(f". added at index {i}")
for line in lines: 
    print(line)