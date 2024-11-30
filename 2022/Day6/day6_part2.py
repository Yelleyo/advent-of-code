# Advent of Code 2022 - Day 6
# Author: Yelleyo

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input_file.txt', 'r') as file:
        content = file.read()
        for i, ch in enumerate(content):
            slice = []
            if i >= 13:
                slice = [content[j] for j in range(i-13, i+1)]
                if len(slice) == len(set(slice)):
                    print(f'marker {ch} found at index: {i + 1} in slice {slice}')
                    break

if __name__ == '__main__':
    main()
