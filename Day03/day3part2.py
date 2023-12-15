import re

# maybe store all matches in a an array of array:
# match[num][]

# def main():
#     with open('test_input_part2.txt', 'r') as file, open('output.txt', 'w') as outfile:
#         lines = file.read().splitlines()
#         for i, line in enumerate(lines):
#             matches = re.finditer(r'\d+', line)
#             if "*" in line:
#                 print(f"* found at line i:{i} with index +1: {line.index('*')+1}")
#                 # print(f"{lines[i][line.index('*')-1]}")
#                 # print(f"{lines[i][line.index('*')]}")
#                 # print(f"{lines[i][line.index('*')+1]}")
#                 # Check up:
#                 if (lines[i-1][line.index('*')-1].isdigit()
#                 or lines[i-1][line.index('*')].isdigit()
#                 or lines[i-1][line.index('*')+1].isdigit()):
#                     print(f"There is a digit above")
# 


#### little talk with ChatGPT: 
# This will store the numbers with their line numbers and positions.
numbers = []

# This will store each character with its line number and position.
characters = {}

def main():
    with open('test_input_part2.txt', 'r') as file, open('output.txt', 'w') as outfile:
        lines = file.read().splitlines()
        for i, line in enumerate(lines):
            matches = re.finditer(r'\d+', line)
            for match in matches:
                numbers.append((i+1, match.start()+1, match.end(), match.group()))
            
            for j, char in enumerate(line):
                characters[(i+1, j+1)] = char
        
        # Now you can iterate over the characters.
        for position, char in characters.items():
            if char == '*':
                # Check the adjacent positions.
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        adjacent_position = (position[0] + dx, position[1] + dy)
                        if adjacent_position in characters and characters[adjacent_position].isdigit():
                            # If the adjacent character is a digit, find and print the whole number.
                            for number in numbers:
                                if number[0] == adjacent_position[0] and number[1] <= adjacent_position[1] <= number[2]:
                                    print(f'Number {number[3]} is adjacent to * in line {position[0]} at position {position[1]}')







 #
 #This code will output:
 #
 #Number 35 is adjacent to * in line 2 at position 4
 #Number 617 is adjacent to * in line 5 at position 4
 #Number 755 is adjacent to * in line 9 at position 5
 #Number 664 is adjacent to * in line 9 at position 5
 #
 #In this code, characters is a dictionary where the keys are tuples (line_number, position) and the values are the characters at those positions.
 #When a * is encountered, the adjacent positions are checked. If an adjacent character is a digit, 
 #the numbers list is searched to find the whole number that the digit is part of.
 #









main()
