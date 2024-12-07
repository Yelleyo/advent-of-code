# Advent of Code 2022 - Day 8
# Author: Yelleyo

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('test.txt', 'r') as file:
        lines = file.read().splitlines()
        # print(f'this is lines[1][0] {lines[1][0]}')
    tree_score = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            h_socre = horizontal_check(lines[i], j)
            v_score = vertical_check(lines, i, j)
            print(f'Score for {lines[i][j]} in line {lines[i]}: h = {h_socre} and v = {v_score}')
            tree_score.append(h_socre * v_score)
    
    print(f'result: {max(tree_score)}')
    
def horizontal_check(line, i):
    nbs_before = line[:i][:-1]
    nbs_after = line[i+1:][:-1]
    before = 0
    after = 0
    for nb in nbs_before:
        if line[i] >= nb:
            before += 1
        else:
            break
    for nb in nbs_after:
        if line[i] >= nb:
            after += 1
        else:
            break
    return (before * after)

def vertical_check(lines, row, col):
    nbs_above = [lines[i][col] for i in range(row)]
    nbs_below = [lines[i][col] for i in range(row + 1, len(lines))]
    above =0
    below = 0
    for nb in nbs_above:
        if lines[row][col] >= nb:
            above += 1
        else:
            break
    for nb in nbs_below:
        if lines[row][col] >= nb:
            below =+ 1
        else:
            break
    return (above * below)

if __name__ == '__main__':
    main()




if __name__ == '__main__':
    main()
