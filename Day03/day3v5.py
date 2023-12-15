
import re

def main():
    with open('input.txt', 'r') as file, open('output.txt', 'w') as outfile:
        lines = file.read().splitlines()
        sum_part_nb = 0
        # print(f"this is the first line: {lines[0]}")
        # print(f"this is lines[4][2], equivalent to line 5 character 3: {lines[4][2]}")
        for i, line in enumerate(lines):
            matches = re.finditer(r'\d+', line)
            for match in matches:
                # print(f"Line {i+1}, Value: {match.group()}, Position: {match.start()} to {match.end()-1}")
                # print(f"{lines[i][match.start()]} - {lines[i][match.end() - 1]}")
                # print(f"matchend -2: {lines[i][match.end() - 2]}")
                # print(f"matchend -1:{lines[i][match.end() - 1]}")
                # print(f"matchend 0:{lines[i][match.end()]}")
                # print(f"matchstart -1: {lines[i][match.start() - 1]}")
                # print(f"matchstart 0: {lines[i][match.start()]}")
                # print(f"matchstart 1: {lines[i][match.start() + 1]}")
                part_nb = 0

# # Strat & line above
# if lines[i-1][match.start() - 1] != "."
# or lines[i-1][match.start()] != "."
# or lines[i-1][match.start() + 1] != "."
# # End & line above
# or lines[i-1][match.end() - 2] != "."
# or lines[i-1][match.end() -1 ] != "."
# or lines[i-1][match.end() ] != "."
# # before & after on the same line
# or lines[i][match.end()] != "."
# or lines[i][match.start() - 1] != "."
# # Start & line under
# or lines[i+1][match.start() - 1] != "."
# or lines[i+1][match.start()] != "."
# or lines[i+1][match.start() + 1] != "."
# # End & line under
# or lines[i+1][match.end() - 2] != "."
# or lines[i+1][match.end() -1 ] != "."
# or lines[i+1][match.end()]

                # Exeption for the fist line:
                if i == 0:
# before & after on the same line
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
                # Exceptin for the last line: 
                elif i == len(lines) - 1:
# Strat & line above
                    if (lines[i-1][match.start() - 1] != "."
                    or lines[i-1][match.start()] != "."
                    or lines[i-1][match.start() + 1] != "."
# End & line above
                    or lines[i-1][match.end() - 2] != "."
                    or lines[i-1][match.end() -1 ] != "."
                    or lines[i-1][match.end() ] != "."
# before & after on the same line
                    or lines[i][match.end()] != "."
                    or lines[i][match.start() - 1] != "."):
                        part_nb = int(match.group())
                # Exaeption when match is the first in line:
                elif match.start() == 0:
# Strat & line above
                    if (lines[i-1][match.start()] != "."
                    or lines[i-1][match.start() + 1] != "."
# End & line above
                    or lines[i+1][match.end() - 2] != "."
                    or lines[i+1][match.end() -1 ] != "."
                    or lines[i+1][match.end() ] != "."
# before & after on the same line
                    or lines[i][match.end()] != "."
# Start & line under
                    or lines[i+1][match.start()] != "."
                    or lines[i+1][match.start() + 1] != "."
# End & line under
                    or lines[i+1][match.end() - 2] != "."
                    or lines[i+1][match.end() -1 ] != "."
                    or lines[i+1][match.end()]) != ".":
                        part_nb = int(match.group())
                # Exception when match is at the end of the line:
                elif match.end() == len(line):
# Strat & line above
                    if (lines[i-1][match.start() - 1] != "."
                    or lines[i-1][match.start()] != "."
                    or lines[i-1][match.start() + 1] != "."
# End & line above
                    or lines[i-1][match.end() - 2] != "."
                    or lines[i-1][match.end() -1 ] != "."
# before & after on the same line
                    or lines[i][match.start() - 1] != "."
# Start & line under
                    or lines[i+1][match.start() - 1] != "."
                    or lines[i+1][match.start()] != "."
                    or lines[i+1][match.start() + 1] != "."
# End & line under
                    or lines[i+1][match.end() - 2] != "."
                    or lines[i+1][match.end() -1 ] != "."):
                        part_nb = int(match.group())
                else:
# Strat & line above
                    if (lines[i-1][match.start() - 1] != "."
                    or lines[i-1][match.start()] != "."
                    or lines[i-1][match.start() + 1] != "."
# End & line above
                    or lines[i-1][match.end() - 2] != "."
                    or lines[i-1][match.end() -1 ] != "."
                    or lines[i-1][match.end() ] != "."
# before & after on the same line
                    or lines[i][match.end()] != "."
                    or lines[i][match.start() - 1] != "."
# Start & line under
                    or lines[i+1][match.start() - 1] != "."
                    or lines[i+1][match.start()] != "."
                    or lines[i+1][match.start() + 1] != "."
# End & line under
                    or lines[i+1][match.end() - 2] != "."
                    or lines[i+1][match.end() -1 ] != "."
                    or lines[i+1][match.end()])!= ".":
                        part_nb = int(match.group())
                print(part_nb) #, file = outfile)
                sum_part_nb += part_nb
        print(f"sum of part number is: {sum_part_nb}") #, file=outfile)


main()

