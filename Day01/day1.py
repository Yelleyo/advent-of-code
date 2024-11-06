#  Day 1 :
# for each line of input get first and last digit, glue them together. 
# then add them all up.

# for each line
# check each caracter is digit or not 
# if yes put it in a temp array
# take first and last value from the array, join, make int
# add this to the calibration array.
# after this add up all values in the array, maybe there is function for that or, just a loop.



input = 'day1input.txt'
line_array = []
calibration = 0

with open(input, 'r') as file:
    for line in file:
        for char in line.strip():
            if char.isdigit():
                line_array.append(char)
        line_output = int(str(line_array[0]) + str(line_array[-1]))
        calibration = line_output + calibration
        line_array.clear()

print(calibration)

# the "pro" version: from https://www.youtube.com/watch?v=y-kOUFrHaKs
# but this one is not correct yet

total = 0

for x in open(input):
    digits = [ch for ch in input if ch.isdigit()]
    total += int(digits[0] + digits[-1])

print(f"This is the second total: {total}")

