#  Day 1 :
# for each line
# check each caracter is digit or not 
# if yes put it in a temp array
# take first and last value from the array, join, make int
# add this to the calibration total.
# clean-up

input = 'day1inputtest.txt'
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