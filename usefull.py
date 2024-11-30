# open file and make a list of lines:
with open('test1.txt', 'r') as file:
    lines = file.read().splitlines()

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