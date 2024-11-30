# Advent of Code 2022 - Day 3
# every 3 lines check the ch in common
# convert ot prio and add to the grand total

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input_file.txt', 'r') as file:
        lines = file.read().splitlines()
        prio = 0
        for i in range(0, len(lines) - 2, 3):
            line1 = lines[i]
            line2 = lines[i+1]
            line3 = lines[i+2]
            
            letter = [ch for ch in line1 if (ch in line2 and ch in line3)]
            print(f'this is the found letter: {letter[0]}')

            if not letter[0].isupper():
                prio += ord(letter[0]) - 96
            else:
                prio += ord(letter[0]) - 38 
    print(prio)

if __name__ == '__main__':
    main()
