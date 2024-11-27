input = 'day1inputtest.txt'
result = 0

with open(input, 'r') as file:
    for line in file:
        line_array = []
        line_array = [ch for ch in line if ch.isdigit()]
        result += int(str(line_array[0]) + str(line_array[-1]))

print(result)