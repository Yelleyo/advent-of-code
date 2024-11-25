 
from collections import Counter

fiveK = []
fourK = []
fullH = []
threeK = []
twoP = []
oneP = []
highC = []
hand_categories = [fiveK, fourK, fullH, threeK, twoP, oneP, highC]

filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().split('\n')

hands_dict = {}
for line in lines:
    key, value = line.split(' ')
    hands_dict[key] = int(value)  # convert value to int

for hand in hands_dict:
    hand_no_J = hand.replace('J','')
    counted_hand = Counter(hand_no_J)
    values = list(counted_hand.values())
    #    print(hand, values)
    if values.count(5) == 1 or hand.count('J') == 5 or (max(values) + hand.count('J')) == 5:
        fiveK.append(hand)
        print(print(f"{hand} to 5K"))
    elif values.count(4) == 1 or (max(values) + hand.count('J')) == 4:
        fourK.append(hand)
        print(print(f"{hand} to 4k"))
    elif (values.count(2) == 1 and values.count(3) == 1 ) or (values.count(2) == 2 and hand.count('J') == 1):
        fullH.append(hand)
        print(print(f"{hand} to fullH"))
    elif values.count(3) == 1 or (max(values) + hand.count('J') == 3):
        threeK.append(hand)
        print(print(f"{hand} to 3K"))
    elif values.count(2) == 2:
        twoP.append(hand)
        print(print(f"{hand} to 2P"))
    elif values.count(2) == 1 or hand.count('J') == 1:
        oneP.append(hand)
        print(print(f"{hand} to oneP"))
    else:
        highC.append(hand)

# print(f"those are the 5K: {fiveK}")
# print(f"those are the 4K: {fourK}")
# print(f"those are the full House: {fullH}")
# print(f"those are the 3K: {threeK}")
# print(f"those are the twoP: {twoP}")
# print(f"those are the oneP: {oneP}")
# print(f"those are the highC: {highC}")

def custom_sort_key(item):
    order = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}
    return [order[i] for i in item]

fiveK = sorted(fiveK, key = custom_sort_key)
fourK = sorted(fourK, key = custom_sort_key)
fullH = sorted(fullH, key = custom_sort_key)
threeK = sorted(threeK, key = custom_sort_key)
twoP = sorted(twoP, key = custom_sort_key)
oneP = sorted(oneP, key = custom_sort_key)
highC = sorted(highC, key = custom_sort_key)


sorted_hands =  highC + oneP + twoP + threeK + fullH + fourK + fiveK
 # print(sorted_hands)

total_winning = 0
for i, hand in enumerate(sorted_hands):
    # print(f"hand: {hand}, with bet: {hands_dict[hand]}")
    total_winning += hands_dict[hand] * (i + 1)

print(f"Total winnings are: {total_winning}")