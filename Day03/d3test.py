
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
                if i == 1:
# before & after on the same line
                    print("hello")
                    if (lines[i][match.end()] != "."
                    or lines[i][match.start() - 1] != "."
# Start & line under
                    or lines[i+1][match.start() - 1] != "."
                    or lines[i+1][match.start()] != "."
                    or lines[i+1][match.start() + 1] != "."
# End & line under
                    or lines[i+1][match.end() - 2] != "."
                    or lines[i+1][match.end() -1 ] != "."
                    or lines[i+1][match.end()]) != ".":
                        part_nb = int(match.group())
                        print(lines[i][match.end()])
                        print(lines[i][match.start() - 1])
    # Start & line underprin
                        print(lines[i+1][match.start() - 1])
                        print(lines[i+1][match.start()])
                        print(lines[i+1][match.start() + 1])
    # End & line under
                        print(lines[i+1][match.end() - 2])
                        print(lines[i+1][match.end() -1 ])
                        print(lines[i+1][match.end()])        