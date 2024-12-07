# Advent of Code 2024 - Day 5
# Author: Yelleyo

# make 3 blocks : rules and updates 
# order the rules in some way 

# line by line
# check each if each value in the line obey the rules
# return the middle number of validated lines

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
        rules_block, updates_block = content.strip().split("\n\n")
    rules_lines = rules_block.splitlines()
    updates_lines = updates_block.splitlines()
    rulebook = making_rules(rules_lines)
    print(rulebook) # dict[key] = [array of number that should be after]
    count = 0
    for line in updates_lines:
        numbers = line.split(',')
        good_line = True
        for i in range(len(numbers)):
            current_number = numbers[i]
            for j in range(i + 1, len(numbers)):
                next_number = numbers[j]
                if next_number in rulebook and current_number in rulebook[next_number]:
                    print(f'Rule broken with current_nb {current_number} and other_nb {next_number}')
                    good_line = False
                    break
            if not good_line:
                break
        
        if good_line:
            print(f'Good line: {line}')
            middle_index = len(numbers) // 2
            count += int(numbers[middle_index])
    
    print(f'Total count: {count}')

def making_rules(updates_lines):
    rules = {}
    for line in updates_lines:
        first, second = line.split("|")
        if first not in rules:
            rules[first] = []
        rules[first].append(second)
    return rules



if __name__ == '__main__':
    main()
