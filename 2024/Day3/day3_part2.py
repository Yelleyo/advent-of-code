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
    total = 0
    do = True

    for line in lines:        
        matches_line = re.finditer(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t', line)
        for match in matches_line:
            matches.append(match.group()) # print(matches)

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
    # mutch nicer than before :) 
    # match_cleaned = match.replace('mul(', '').replace(')', '')
    # match_final = []
    # match_final.append(match_cleaned.split(','))
    # print(match_final)
    # result = int(match_final[0][0]) * int(match_final[0][1])
    # return result
    

if __name__ == '__main__':
    main()
