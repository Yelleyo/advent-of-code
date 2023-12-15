
# each line have win_nb on the left, and my_num on the right
# for each match on the line: 
# 1 match -> 1 point
# 2 match -> 2 points
# 3 match -> 4 points
# 4 match -> 8 points
# in the en total = sum(line_score)
import re

input = 'input.txt'
card_nb = ''
nb = ''
win_string = ''
my_string = ''
win_nb = []
my_nb = []
matches = 0
line_score = 0
total_score = 0


import re

total_score = 0
with open(input, 'r') as file:
    for line in file:
        line_score = 0
        card_nb = line.split(":")[0]
        nb = line.split(":")[1]
        win_string = nb.split("|")[0]
        my_string = nb.split("|")[1]
        win_nb = [int(i.group()) for i in re.finditer(r'\d+', win_string)]
        my_nb = [int(i.group()) for i in re.finditer(r'\d+', my_string)]
        matches = sum(i in win_nb for i in my_nb)
        print(f"Card nb: {card_nb}\nwin_nb: {win_nb}\nmy_nb: {my_nb}")
        if matches == 1:
            line_score = 1
        elif matches > 1:
            line_score = 2 ** (matches - 1)
        total_score += line_score

print(f"the total score is: {total_score}")