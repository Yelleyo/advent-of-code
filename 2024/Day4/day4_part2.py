
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
        for j in range(len(lines[i])): # j is the char index
            if lines[i][j] == 'A':
                if 1 <= i <= len(lines) - 2 and 1 <= j <= len(lines[i]) - 2:
                    print(f'line {[i]}, index {[j]}: TOP: {lines[i-1][j-1]}.{lines[i-1][j+1]} and bottom: {lines[i+1][j-1]}.{lines[i+1][j+1]}')
                    if check_A1(lines, i, j):
                        count += 1
                    if check_A2(lines, i, j):
                        count += 1
                    if check_A3(lines, i, j):
                        count += 1
                    if check_A4(lines, i, j):
                        count += 1
    print(f'count = {count}')


def check_A1(lines, i, j):
    if lines[i-1][j-1] == 'M' and lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S' and lines[i+1][j+1] == 'S':
        print(f'A1 XMAS found at line {i} index {j}')
        return True

def check_A2(lines, i, j):
    if lines[i-1][j-1] == 'S' and lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S' and lines[i+1][j+1] == 'M':
        print(f'A1 XMAS found at line {i} index {j}')
        return True

def check_A3(lines, i, j):
    if lines[i-1][j-1] == 'S' and lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M' and lines[i+1][j+1] == 'M':
        print(f'A1 XMAS found at line {i} index {j}')
        return True

def check_A4(lines, i, j):
    if lines[i-1][j-1] == 'M' and lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M' and lines[i+1][j+1] == 'S':
        print(f'A1 XMAS found at line {i} index {j}')
        return True

if __name__ == '__main__':
    main()
