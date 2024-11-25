from functools import reduce
import operator
from tqdm import tqdm 

input = 'input.txt'

time, distance = open(input).read().split("\n")
print(f"this is the Times line: {time}")
print(f"this is the distances line: {distance}")

time = int(time.replace(' ', '').split(':')[1])
distance = int(distance.replace(' ', '').split(':')[1])
print(f"New time array: {time}")
print(f"New distances array: {distance}")

winning_races = []

won_races = 0
for i in tqdm(range(time+1)):
    race = i * (time - i) 
    print(f'race distance: {race}')
    if race > distance:
        won_races += 1
winning_races.append(won_races)
print(f'{won_races} races beat the record in race {time}')

print(f'the amount of won races is: {won_races}')