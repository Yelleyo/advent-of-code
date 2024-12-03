# Advent of Code 2024 - Day 3
# Author: Yelleyo

import re
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()

    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t')
    matches = [match.group() for line in lines for match in pattern.finditer(line)]
    print(matches)

    total = 0
    do = True

    for match in matches:
        if match == 'do()':
            do = True
        elif match == "don't":
            do = False
        elif match.startswith('mul') and do:
            total += multiply_raw(match)

    print(f'this is the total: {total}')

def multiply_raw(match):
    a, b = map(int, re.findall(r'\d+', match))
    return a * b

if __name__ == '__main__':
    main()