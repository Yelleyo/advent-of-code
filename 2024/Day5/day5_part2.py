# Advent of Code 2024 - Day 5
# Author: Yelleyo

# fix the lines


import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    with open('test.txt', 'r') as file:
        content = file.read()
        rules_block, updates_block = content.strip().split("\n\n")

    rules_lines = rules_block.splitlines()
    updates_lines = updates_block.splitlines()
    rulebook = making_rules(rules_lines)
    print(rulebook)  # dict[key] = [array of number that should be after]

    count = 0
    bad_lines = []

    for line in updates_lines:
        numbers = line.split(',')
        if not check_line(rulebook, numbers):
            bad_lines.append(line)

    for line in bad_lines:
        numbers = line.split(',')
        fixed_numbers = fix_line(rulebook, numbers)
        middle_index = len(fixed_numbers) // 2
        count += int(fixed_numbers[middle_index])

    print(f'Total count: {count}')

def check_line(rulebook, numbers):
    for i in range(len(numbers)):
        current_number = numbers[i]
        for j in range(i + 1, len(numbers)):
            next_number = numbers[j]
            if next_number in rulebook and current_number in rulebook[next_number]:
                print(f'Rule broken with current_nb {current_number} and other_nb {next_number}')
                return False
    return True

def fix_line(rulebook, numbers):
    i = 0
    print(f'working on line {numbers}')
    while i < len(numbers):
        current_number = numbers[i]
        fixed = False
        for j in range(i + 1, len(numbers)):
            next_number = numbers[j]
            if next_number in rulebook and current_number in rulebook[next_number]:
                # Swap the elements
                numbers[i], numbers[j] = numbers[j], numbers[i] # <---- this is bubble sort
                print(f'Reparing line: {numbers}, switching {numbers[i]} and {numbers[j]}')
                fixed = True
                break
        if not fixed:
            i += 1
    return numbers

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