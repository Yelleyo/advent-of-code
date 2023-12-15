# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# same same, but number spelled out also count :)

# make a dict for each line -> line_dict = {position:nb}
# then sort the dict on position, and take first and last values

# solution 2: no dict, for each char in line check if line starting from this char start in digit_array -> add the corresponding int
num_dic = dict([
    ('one', '1'),
    ('zero', '0'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
])
input = 'day1input.txt'
line_dict = {}
line_array = []
calibration = 0

with open(input, 'r') as file:
    for line in file:
        for i, char in enumerate(line.strip()):
            if char.isdigit():
                line_array.append(char)
            else:
                for key in num_dic.keys():
                    if line[i:].startswith(key):
                        line_array.append(num_dic[key])
        line_output = int(str(line_array[0]) + str(line_array[-1]))
        print(line_output)
        calibration = line_output + calibration
        line_array.clear()

print(calibration)
