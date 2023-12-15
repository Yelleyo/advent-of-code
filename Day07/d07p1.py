# strength of cards: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
# strength of hands: 
    # 5 of kind
    # 4 of kind
    # full house: 3 of kind and 2 of kind
    # 3 of a kind
    # 2 pairs
    # 1 pair
    # high card

# when hands a same, order on first card, then on second...

# make a dict of the input -> to get the right bet later (hopefully no double values)
# group hands into types
# sort inside the types 
# bring everybody back together 
# distribute points 
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
    counted_hand = Counter(hand)
    values = list(counted_hand.values())
    #    print(hand, values)
    if values.count(5) == 1:
        fiveK.append(hand)
    elif values.count(4) == 1:
        fourK.append(hand)
    elif values.count(2) == 1 and values.count(3) == 1:
        fullH.append(hand)
    elif values.count(3) == 1:
        threeK.append(hand)
    elif values.count(2) == 2:
        twoP.append(hand)
    elif values.count(2) == 1:
        oneP.append(hand)
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
    order = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
    return [order[i] for i in item]

fiveK = sorted(fiveK, key = custom_sort_key)
fourK = sorted(fourK, key = custom_sort_key)
fullH = sorted(fullH, key = custom_sort_key)
threeK = sorted(threeK, key = custom_sort_key)
twoP = sorted(twoP, key = custom_sort_key)
oneP = sorted(oneP, key = custom_sort_key)
highC = sorted(highC, key = custom_sort_key)


sorted_hands =  highC + oneP + twoP + threeK + fullH + fourK + fiveK
print(sorted_hands)

total_winning = 0
for i, hand in enumerate(sorted_hands):
    print(f"hand: {hand}, with bet: {hands_dict[hand]}")
    total_winning += hands_dict[hand] * (i + 1)

print(f"Total winnings are: {total_winning}")


