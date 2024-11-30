# A -> Rock -> 1
# B -> Paper -> 2
# C -> sissors -> 3

# My Response
# X -> Rock
# Y -> Paper
# Z -> sissors

# Score
# 0 if lost
# 3 if draw
# 6 if won
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

input_file = 'input_file.txt'

with open(input_file, 'r') as file:
    lines = file.read().splitlines()
    #content = file.read()
    # lines = content.strip().split("\n")
    score_total = 0
    for line in lines:
        score_line = 0
        oppo = line[0]
        me = line[-1]
        if me == 'X':
            score_line += 1
        if me == 'Y':
            score_line += 2
        if me == 'Z':
            score_line += 3
        if (me == 'X' and oppo == 'A') or (me == 'Y' and oppo == 'B') or (me == 'Z' and oppo == 'C'):
            score_line += 3
        if (me == 'X' and oppo == 'C') or (me == 'Y' and oppo == 'A') or (me == 'Z' and oppo == 'B'):
            score_line += 6
        score_total += score_line
    
    print(f'this is total: {score_total}')



