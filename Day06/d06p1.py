from functools import reduce
import operator

input = 'test_input.txt'

times, distances = open(input).read().split("\n")
print(f"this is the Times line: {times}")
print(f"this is the distances line: {distances}")

times = list(map(int, times.split(':')[1].split()))
distances = list(map(int, distances.split(':')[1].split()))
print(f"New times array: {times}")
print(f"New distances array: {distances}")

winning_races = []

for time in times:
    i = 0
    won_races = 0
    while i <= time:
        race = i * (time - i) 
        print(f'race distance: {race}')
        i += 1
        if race > distances[times.index(time)]:
            won_races += 1
    winning_races.append(won_races)
    print(f'{won_races} races beat the record in race {time}')

print(winning_races)
result = reduce(operator.mul, winning_races, 1)
print(result)
