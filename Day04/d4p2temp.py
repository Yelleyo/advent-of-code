import re

input = 'test_inputp2.txt'
card_nb = ''
nb = ''
win_string = ''
my_string = ''
win_nb = []
my_nb = []
matches = 0
line_score = 0
total_score = 0
card_copies = {1: 0}

total_score = 0
with open(input, 'r') as file:
    for line_nb, line in enumerate(file, start=1):
        card_copies[line_nb] = 1


with open(input, 'r') as file:
    for line in file:
        line_score = 0
        card_nb_part = line.split(":")[0]
        card_nb = int(card_nb_part.split(' ')[1])
        nb = line.split(":")[1]
        win_string = nb.split("|")[0]
        my_string = nb.split("|")[1]
        win_nb = [int(i.group()) for i in re.finditer(r'\d+', win_string)]
        my_nb = [int(i.group()) for i in re.finditer(r'\d+', my_string)]
        matches = sum(i in win_nb for i in my_nb)
        print(f"Cards {card_nb} score: {matches}")
        for i in range(1, matches + 1):  # start from 1 because you want to increment the next keys
            card_copies[card_nb+i] = card_copies.get(card_nb+i, 0) + 1  # increment the value by 1
            print(f"Card {card_nb}: {card_copies} copies")
    total_score = sum(card_copies.values())
    print(f'This is the total score for this set of cards: {total_score}')