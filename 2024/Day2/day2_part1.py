# Advent of Code 2024 - Day 2
# Author: Yelleyo

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
        safe = 0
        
        for line in lines:
            numbers = line.split(" ")
            safe1 = True
            safe2 = True
            
            for i in range(len(numbers) - 1):
                nb1 = int(numbers[i])
                nb2 = int(numbers[i + 1])
                
                if not (1 <= nb1 - nb2 <= 3):
                    safe1 = False
                if not (-3 <= nb1 - nb2 <= -1):
                    safe2 = False
            
            if safe1 or safe2:
                safe += 1

        
        print(f'Total safe lines: {safe}')

if __name__ == '__main__':
    main()