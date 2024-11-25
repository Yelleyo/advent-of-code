input_file = 'test_input.txt'

with open(input_file, 'r') as file:
    content = file.read()
    blocks = content.strip().split("\n\n")
    horizontal = 0
    vertical = 0
    for block in blocks:
        lines = block.split("\n")
        for i, line in enumerate(lines):
            # Check if there is a next line
            if i+1 < len(lines):
                # Compare the current line with the next line
                if line == lines[i+1]:
                    print(f'Match found between \nline {i}:{line}\nline {i+1}:{lines[i+1]}')
                    j = 1
                    while i-j >= 0 and i+1+j < len(lines):
                        # Compare the lines before and after the matched lines
                        if lines[i-j] == lines[i+1+j]:
                            print(f'Match found between \nline {i-j}:{lines[i-j]}\nline {i+1+j}:{lines[i+1+j]}')
                            j += 1
                        else:
                            break
                    # Check if match is found until the first or last line
                    if i-j == -1 or i+1+j == len(lines):
                        horizontal += i+1
print(f'Horizontal: {horizontal}')

