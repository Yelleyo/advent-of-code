# Advent of Code 2022 - Day 8
# Author: Yelleyo

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
        # print(f'this is lines[1][0] {lines[1][0]}')
    tree_count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if horizontal_check(lines[i], j) or vertical_check(lines, i, j):
                print(f'{lines[i][j]} in line {lines[i]} is counting')
                tree_count += 1
    
    print(f'Total amount of visible trees:\n{tree_count}')
    
def horizontal_check(line, i):
    nbs_before = line[:i]
    nbs_after = line[i+1:]
    check_before = True
    check_after = True
    for nb in nbs_before:
        if line[i] <= nb:
            check_before = False
    for nb in nbs_after:
        if line[i] <= nb:
            check_after = False
    return (check_before or check_after)

def vertical_check(lines, row, col):
    nbs_above = [lines[i][col] for i in range(row)]
    nbs_below = [lines[i][col] for i in range(row + 1, len(lines))]
    check_above = True
    check_below = True
    for nb in nbs_above:
        if lines[row][col] <= nb:
            check_above = False
    for nb in nbs_below:
        if lines[row][col] <= nb:
            check_below = False
    return (check_above or check_below)

if __name__ == '__main__':
    main()




if __name__ == '__main__':
    main()
