# Advent of Code 2024 - Day 3
# Author: Yelleyo

import re
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()

    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    matches = [pattern.findall(line) for line in lines]
    matches_flat = [item for sublist in matches for item in sublist]

    total = sum(int(a) * int(b) for a, b in matches_flat)

    print(f'this is match final: {matches_flat}')
    print(f'this is the total: {total}')

if __name__ == '__main__':
    main()