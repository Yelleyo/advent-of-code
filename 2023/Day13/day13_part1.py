# Find the split/mirror line
# if the line is horizontal total +=  first line nb * 100
# if the line is vertical total += fist colomn nb

input_file = 'test1.txt'

with open(input_file, 'r') as file:
    content = file.read()
    blocks = content.strip().split("\n\n")

    # check for a horizontal mirror
for block in blocks:
    lines = block.split("\n")
    horizontal = 0  
    vertical = 0
    num_lines = len(lines)

    for i in range(num_lines - 1):
        if lines[i] == lines[i + 1]:
            print(f'Match found on \nline {i}: {lines[i]}')
            j = 1

            while i - j >= 0 and i + 1 + j < num_lines and lines[i - j] == lines[i + 1 + j]:
                j += 1

            if i - j == -1 or i + 1 + j == num_lines:
                horizontal += i + 1

    print(f'horizontal = {horizontal} after this block')

    first_line = lines[0]
    print(f'this is the first line of each block: {first_line}')
    for i in range(len(first_line) - 1):
        if first_line[i] == first_line[i+1]:
            if all(line[i] == line[i + 1] for line in lines):
                print(f'Mirror found at index: {i}')
                vertical += i+1
    print(f'vertical = {vertical} after this block')