# only number with simbol next to each to them count (event diagonaly)
# in the test input 114 and 58 are the ones that are excluded. 
# add up the rest

# Make an array with each line is an value

# find numbers with regex => import re
import re

input_arr = []
lines = []
sum_part_nb = 0

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
        # print(f"this is the first line: {lines[0]}")
        # print(f"this is lines[4][2], equivalent to line 5 character 3: {lines[4][2]}")
        for i, line in enumerate(lines):
            matches = re.finditer(r'\d+', line)
            for match in matches:
                print(f"Line {i+1}, Value: {match.group()}, Position: {match.start()} to {match.end()-1}")
                print(f"{lines[i][match.start()]} - {lines[i][match.end() - 1]}")
                # print(f"matchend -1: {lines[i-1][match.end() - 2]}")
                # print(f"matchend {lines[i-1][match.end() - 1]}")
                # print(f"matchend+1 {lines[i-1][match.end()]}")
                # print(f"matchstart -1: {lines[i-1][match.end() - 2]}")
                # print(f"matchstart {lines[i-1][match.end() - 1]}")
                # print(f"matchstart +1: {lines[i-1][match.end()]}")
                part_nb = 0
                if i == 0:
                    if match.start() == 0:
                        check_first_right()
                        chek_first_down()
                    elif match.end() == len(line):
                        check_last_left()
                        check_last_down()
                    else:
                        check_middle_down()
                elif i == len(lines):
                    if match.start() == 0:
                        check_first_right()
                        check_first_up()
                    elif match.end() == len(line):
                        check_last_left()
                        check_first_up()
                    else:
                        check_middle_up()
                elif match.start() == 0:
                    check_first_right()
                    check_first_up()
                    check_last_down()
                elif match.end() == len(line):
                    check_last_left()
                    check_first_up()
                    check_last_down()
                else:
                    check_middle_up()
                    check_middle_down()
                print(part_nb)
                sum_part_nb += part_nb
        print(f"sum of part number is: {sum_part_nb}")


def check_first_right():
    if lines[i][match.end()] != ".":
        part_nb = int(match.group())
    
def check_first_up():
    if lines[i-1][match.start()] != "." or lines[i-1][match.start() + 1] != ".":
        part_nb = int(match.group())

def chek_first_down():
    if lines[i+1][match.end()] != "." or lines[i+1][match.end() + 1] != ".":
        part_nb = int(match.group())


def check_last_left():
    if lines[i][match.start() - 1] != ".":
        part_nb = int(match.group())

def check_last_up():
    if lines[i-1][match.end() - 2] != "." or lines[i-1][match.end() - 1] != ".":
        part_nb = int(match.group())

def check_last_down():
    if lines[i+1][match.end() - 2] != "." or lines[i+1][match.end() -1 ] != ".":
        part_nb = int(match.group())

def check_middle_up():
    if lines[i-1][match.start() - 1] != "." or lines[i-1][match.start()] != "." or lines[i-1][match.start() + 1] != ".":
        part_nb = int(match.group())
    elif lines[i-1][match.end() - 2] != "." or lines[i-1][match.end() - 1] != "." or lines[i-1][match.end()] != ".":
        part_nb = int(match.group())
    
def check_middle_down():
    if lines[i+1][match.start() - 1] != "." or lines[i+1][match.start()] != "." or lines[i+1][match.start() + 1] != ".":
        part_nb = int(match.group())
    elif lines[i+1][match.end() - 2] != "." or lines[i+1][match.end() -1] != "." or lines[i+1][match.end()] != ".":
        part_nb = int(match.group())

main()