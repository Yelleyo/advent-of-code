import re

def main():
    with open('test_input.txt', 'r') as file:
        lines = file.read().splitlines()
        sum_part_nb = 0
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
                        part_nb = check_first_right(lines, i, match)
                        part_nb = chek_first_down(lines, i, match)
                    elif match.end() == len(line):
                        part_nb = check_last_left(lines, i, match)
                        part_nb = check_last_down(lines, i, match)
                    else:
                        part_nb = check_middle_down(lines, i, match)
                elif i == len(lines) - 1:
                    if match.start() == 0:
                        part_nb = check_first_right(lines, i, match)
                        part_nb = check_first_up(lines, i, match)
                    elif match.end() == len(line):
                        part_nb = check_last_left(lines, i, match)
                        part_nb = check_first_up(lines, i, match)
                    else:
                        part_nb = check_middle_up(lines, i, match)
                elif match.start() == 0:
                    part_nb = check_first_right(lines, i, match)
                    part_nb = check_first_up(lines, i, match)
                    part_nb = check_last_down(lines, i, match)
                elif match.end() == len(line):
                    part_nb = check_last_left(lines, i, match)
                    part_nb = check_first_up(lines, i, match)
                    part_nb = check_last_down(lines, i, match)
                else:
                    part_nb = check_middle_up(lines, i, match)
                    part_nb = check_middle_down(lines, i, match)
                part_nb = int(part_nb)
                print(part_nb)
                sum_part_nb += part_nb
        print(f"sum of part number is: {sum_part_nb}")


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