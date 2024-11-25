import re

def main():
    with open('test_input.txt', 'r') as file, open('output.txt', 'w') as outfile:
        lines = file.read().splitlines()
        sum_part_nb = 0
        # print(f"this is the first line: {lines[0]}")
        # print(f"this is lines[4][2], equivalent to line 5 character 3: {lines[4][2]}")
        for i, line in enumerate(lines):
            matches = re.finditer(r'\d+', line)
            for match in matches:
                print(f"Line {i+1}, Value: {match.group()}, Position: {match.start()} to {match.end()-1}")
                print(f"{lines[i][match.start()]} - {lines[i][match.end() - 1]}")
                print(f"matchend -2: {lines[i][match.end() - 2]}")
                print(f"matchend -1:{lines[i][match.end() - 1]}")
                print(f"matchend 0:{lines[i][match.end()]}")
                print(f"matchstart -1: {lines[i][match.start() - 1]}")
                print(f"matchstart 0: {lines[i][match.start()]}")
                print(f"matchstart 1: {lines[i][match.start() + 1]}")
                part_nb = 0
                # Exeption for the fist line:
                if i == 0:
                    if lines[i+1][match.end() - 2] != "." or lines[i+1][match.end() -1 ] != "." or lines[i+1][match.end() ] != ".":
                        part_nb = int(match.group())
                    elif lines[i+1][match.start() - 1] != "." or lines[i-1][match.start()] != "." or lines[i+1][match.start() + 1] != ".":
                        part_nb = int(match.group())
                # Exceptin for the last line: 
                elif i == len(lines) - 1:
                    if lines[i-1][match.start() - 1] != "." or lines[i-1][match.start()] != "." or lines[i-1][match.start() + 1] != ".":
                        part_nb = int(match.group())
                    elif lines[i-1][match.end() - 2] != "." or lines[i-1][match.end() - 1] != "." or lines[i-1][match.end()] != ".":
                        part_nb = int(match.group())
                # Exaeption when match is the first in line:
                elif match.start() == 0:
                    if lines[i][match.end()] != ".":
                        part_nb = int(match.group())
                    elif lines[i-1][match.start()] != "." or lines[i-1][match.start() + 1] != ".":
                        part_nb = int(match.group())
                    elif lines[i+1][match.end() - 2] != "." or lines[i+1][match.end() -1 ] != "." or lines[i+1][match.end()] :
                        part_nb = int(match.group())
                # Exception when match is at the end of the line:
                elif match.end() == len(line):
                    if lines[i][match.start() - 1] != ".":
                        part_nb = int(match.group())
                    if lines[i-1][match.start() - 1] != "." or lines[i-1][match.start()] != "." or lines[i-1][match.start() + 1] != ".":
                        part_nb = int(match.group())
                    elif lines[i+1][match.end() - 2] != "." or lines[i+1][match.end() -1 ] != ".":
                        part_nb = int(match.group())
                else:
                    if lines[i-1][match.start() - 1] != "." or lines[i-1][match.start()] != "." or lines[i-1][match.start() + 1] != ".":
                        part_nb = int(match.group())
                    elif lines[i-1][match.end() - 2] != "." or lines[i-1][match.end() - 1] != "." or lines[i-1][match.end()] != ".":
                        part_nb = int(match.group())
                    elif lines[i+1][match.start() - 1] != "." or lines[i+1][match.start()] != "." or lines[i+1][match.start() + 1] != ".":
                        part_nb = int(match.group())
                    elif lines[i+1][match.end() - 2] != "." or lines[i+1][match.end() -1] != "." or lines[i+1][match.end()] != ".":
                        part_nb = int(match.group())
                    elif lines[i][match.end()] != "." or lines[i][match.start() - 1] != ".":
                        part_nb = int(match.group())
                part_nb = int(part_nb)
                print(part_nb) #, file = outfile)
                sum_part_nb += part_nb
        print(f"sum of part number is: {sum_part_nb}") #, file=outfile)


def check_first_right(lines, i, match):
    if lines[i][match.end()] != ".":
        part_nb = int(match.group())
    return 0
    
def check_first_up(lines, i, match):
    if lines[i-1][match.start()] != "." or lines[i-1][match.start() + 1] != ".":
        part_nb = int(match.group())
    return 0

def chek_first_down(lines, i, match):
    if lines[i+1][match.end()] != "." or lines[i+1][match.end() + 1] != ".":
        part_nb = int(match.group())
    return 0


def check_last_left(lines, i, match):
    if lines[i][match.start() - 1] != ".":
        part_nb = int(match.group())
    return 0

def check_last_up(lines, i, match):
    if lines[i-1][match.end() - 2] != "." or lines[i-1][match.end() - 1] != ".":
        part_nb = int(match.group())
    return 0

def check_last_down(lines, i, match):
    if lines[i+1][match.end() - 2] != "." or lines[i+1][match.end() -1 ] != ".":
        part_nb = int(match.group())
    return 0

def check_middle_up(lines, i, match):
    if lines[i-1][match.start() - 1] != "." or lines[i-1][match.start()] != "." or lines[i-1][match.start() + 1] != ".":
        part_nb = int(match.group())
    elif lines[i-1][match.end() - 2] != "." or lines[i-1][match.end() - 1] != "." or lines[i-1][match.end()] != ".":
        part_nb = int(match.group())
    return 0
    
def check_middle_down(lines, i, match):
    if lines[i+1][match.start() - 1] != "." or lines[i+1][match.start()] != "." or lines[i+1][match.start() + 1] != ".":
        part_nb = int(match.group())
    elif lines[i+1][match.end() - 2] != "." or lines[i+1][match.end() -1] != "." or lines[i+1][match.end()] != ".":
        part_nb = int(match.group())
    return 0

main()
