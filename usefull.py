# open file and make a list of lines:
with open('test1.txt', 'r') as file:
    lines = file.read().splitlines()
#eventually split info into lists
list1 = [int(line.split("   ")[0]) for line in lines]
list2 = [int(line.split("   ")[1]) for line in lines]

# find a pattern in the line and get the position i:
import re
for i, line in enumerate(lines):
    matches = re.finditer(r'\d+', line)

# open file and deal with block of text:
with open('test1.txt', 'r') as file:
    content = file.read()
    blocks = content.strip().split("\n\n")
    for block in blocks:
        pass

# split a line in 2, assign first and second part.
first_element = line.split(":")[0]
second_element = line.split(":")[1]

# loop and add to array if condition is met:
line_array = []
line_array = [ch for ch in line if ch.isdigit()]

# check with line number and index
for i in range(len(lines)):
    for j in range(len(lines[i])):
        pass

# Zip through 2 lists
for nb1, nb2 in zip(list1, list2):
    pass