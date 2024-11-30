# Advent of Code 2022 - Day 4
# Author: Yelleyo
# split the pairs in 2 
# compare begining and end of each pair --> 2 times
# + 1 if met those requirements: 

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input_file.txt', 'r') as file:
        lines = file.read().splitlines()
        total_pairs = 0
        for line in lines:
            p1, p2 = line.split(",")
            b1, e1 = map(int,p1.split("-"))
            b2, e2 = map(int,p2.split("-"))
            if ((b1 <= b2) and (e1 >= e2)) or ((b1 >= b2) and (e1 <= e2)):
                print(f'found true: pair1: {b1}-{e1} pair2: {b2}-{e2}')
                total_pairs += 1
    print(total_pairs)
        

if __name__ == '__main__':
    main()
