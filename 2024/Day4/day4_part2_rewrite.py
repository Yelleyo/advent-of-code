import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    with open('test.txt', 'r') as file:
        lines = file.read().splitlines()

    count = 0
    for i in range(len(lines)):  # i is the line index
        for j in range(len(lines[i])):  # j is the char index
            if lines[i][j] == 'A':
                if is_within_bounds(lines, i, j):
                    count += check_patterns(lines, i, j)
    print(f'count = {count}')

def is_within_bounds(lines, i, j):
    return 1 <= i <= len(lines) - 2 and 1 <= j <= len(lines[i]) - 2

def check_patterns(lines, i, j):
    patterns = [
        ('M', 'M', 'S', 'S'),
        ('S', 'M', 'S', 'M'),
        ('S', 'S', 'M', 'M'),
        ('M', 'S', 'M', 'S')
    ]
    
    count = 0
    # check for each pattern
    for pattern_index, (top_left, top_right, bottom_left, bottom_right) in enumerate(patterns, start=1):
        if (lines[i-1][j-1] == top_left and lines[i-1][j+1] == top_right and
                lines[i+1][j-1] == bottom_left and lines[i+1][j+1] == bottom_right):
            print(f'A{pattern_index} XMAS found at line {i} index {j}')
            count += 1
    return count

if __name__ == '__main__':
    main()