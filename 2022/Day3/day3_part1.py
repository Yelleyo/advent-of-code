# Advent of Code 2022 - Day 3
# split line in 2
# for each ch in line1 check is in line2
# if yes get this letter
# convert to number
# add in to the grand total

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input_file.txt', 'r') as file:
        lines = file.read().splitlines()
        prio = 0
        for line in lines:
            firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
            letter = [ch for ch in firstpart if ch in secondpart]
            print(f'this is the found letter: {letter[0]}')
            if not letter[0].isupper():
                prio += ord(letter[0]) - 96
            else:
                prio += ord(letter[0]) - 38 
    print(prio)

if __name__ == '__main__':
    main()
