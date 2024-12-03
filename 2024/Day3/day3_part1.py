# Advent of Code 2024 - Day 3
# Author: Yelleyo
import re
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
    matches = []
    for line in lines:
        matches_line = re.finditer(r'mul\(\d{1,3},\d{1,3}\)', line)
        for match in matches_line:
            matches.append(match.group()) 
            
    matches_cleaned = []
    for match in matches:
        matches_cleaned.append(match.replace('mul(', '').replace(')', ''))

    match_final = []
    for match in matches_cleaned:
        match_final.append(match.split(','))
    
    print(f'this is match final: {match_final}')

    total = 0
    for match in match_final:
        total += int(match[0]) * int(match[1])
    
    print(f'this is the total: {total}')

if __name__ == '__main__':
    main()
