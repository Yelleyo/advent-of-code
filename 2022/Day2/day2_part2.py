# A -> Rock -> 1
# B -> Paper -> 2
# C -> sissors -> 3

# My Response
# AX Rock
# BY Paper
# CZ sissors

# Score
# X if lost
# Y if draw
# Z if won

input_file = 'input_file.txt'

with open(input_file, 'r') as file:
    content = file.read()
    lines = content.strip().split("\n")
    score_total = 0
    for line in lines:
        score_line = 0
        me = ''
        oppo = line[0]
        tip = line[-1]
        if (oppo == 'A' and tip == 'X') or (oppo == 'C' and tip == 'Y') or (oppo == 'B' and tip == 'Z'):
            me = 'Z'
        if (oppo == 'B' and tip == 'X') or (oppo == 'A' and tip == 'Y') or (oppo == 'C' and tip == 'Z'):
            me = 'X'
        if (oppo == 'C' and tip == 'X') or (oppo == 'B' and tip == 'Y') or (oppo == 'A' and tip == 'Z'):
            me = 'Y'

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