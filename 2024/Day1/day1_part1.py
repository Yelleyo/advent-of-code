# Advent of Code 2024 - Day 1
# Author: Yelleyo

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input_file.txt', 'r') as file:
        lines = file.read().splitlines()
        list1 = []
        list2 = []
        for line in lines:
            list1.append(int(line.split("   ")[0]))
            list2.append(int(line.split("   ")[1]))
        list1.sort()
        list2.sort()
        print(f'those are the list sorted:\n{list1}\n{list2}')
        total = 0
        for i, nb in enumerate(list1):
            total += abs(list2[i] - nb)
        
        print(f'the total is: {total}')


if __name__ == '__main__':
    main()
