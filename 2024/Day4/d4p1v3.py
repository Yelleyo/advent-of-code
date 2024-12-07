
# Advent of Code 2024 - Day 4
# Author: Yelleyo

# find all the XMAS in the input
# any direction right left up down diagonal (up left, down left, up right, down right)
# DO NOT COME AROUND 

# check for X if adjacent char is a M
# then check again in the same direction if the ones after are an A and a S

# how to go around the block?

# check fundtions: right(i, j, letter), left(i, j, letter)

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()

    for line in lines:
        print(line)
    count = 0
    for i in range(len(lines)): # i is the line index
        # print(f'checking line {i}: {new_lines[i]}')
        for j in range(len(lines[i])): # j is the char index
            # print(f'checking ch: {new_lines[i][j]} at line {i} index {j}')
            if lines[i][j] == 'X':
                # print(f'Checking on X {new_lines[i][j]}: {new_lines[i][j-3:j+1]}')
                if right(lines, i, j):
                    count += 1
                if left(lines, i, j):
                    count += 1
                if up(lines, i, j):
                    count += 1
                if down(lines, i, j):
                    count += 1
                if up_right(lines, i, j):
                    count += 1
                if up_left(lines, i, j):
                    count += 1
                if down_right(lines, i, j):
                    count += 1
                if down_left(lines, i, j):
                    count += 1
    print(f'count = {count}')

def right(lines, i, j):
    if j <= len(lines[i]) - 3:
        if lines[i][j:j+4] == 'XMAS':
            print(f'right XMAS found at line {i-3} index {j-3}')
            return True

def left(lines, i, j):
    if j >= 3:
        if lines[i][j-3:j+1] == 'SAMX':
            print(f'left SAMX found at line {i-3} index {j-3}')
            return True

def up(lines, i, j):
    if i >= 3:
        if lines[i][j] == 'X' and lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S':
            print(f'up XMAS found at line {i-3} index {j-3}')
            return True

def down(lines, i, j):
    if i <= len(lines) - 4:
        if lines[i][j] == 'X' and lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
            print(f'down XMAS found at line {i-3} index {j-3}')
            return True

def up_right(lines, i, j):
    if i >= 3 and j <= len(lines[i]) - 3:
        if lines[i][j] == 'X' and lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
            print(f'up right XMAS found at line {i-3} index {j-3}')
            return True

def down_right(lines, i, j):
    if i <= len(lines) - 4 and j <= len(lines[i]) - 4:
        if lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
            print(f'down right XMAS found at line {i-3} index {j-3}')
            return True
####
def up_left(lines, i, j):
    if i >= 3 and j >= 3:
        if lines[i][j] == 'X' and lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
            print(f'up left XMAS found at line {i-3} index {j-3}')
            return True

def down_left(lines, i, j):
    if i <= len(lines) - 4 and j >= 3:
        if lines[i][j] == 'X' and lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
            print(f'down left XMAS found at line {i-3} index {j-3}')
            return True

if __name__ == '__main__':
    main()
