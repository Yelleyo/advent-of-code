# Advent of Code 2022 - Day 7
# Author: Yelleyo

import os

# Change directory to the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
    
    cd_blocks = content.strip().split("$ cd ")
    del cd_blocks[0]
    blocks = []
    for block in cd_blocks:
        blocks.append(block.strip().split("\n"))

    block_dict = {}
    current_path = []

    for block in blocks:
        key = block[0].strip()
        values = block[1:]
        if '$ ls' in values:
            values.remove('$ ls')
        
        if key == '..':
            current_path.pop()
        else:
            current_path.append(key)
            path_key = '/'.join(current_path)
            block_dict[path_key] = values

    # Process the block_dict to calculate sizes and directories
    for key in block_dict:
        lines = block_dict[key]
        dirs = []
        size = 0
        for line in lines:
            if 'dir' in line:
                dirs.append(line.split(" ")[-1])
            elif line[0].isdigit():
                size += int(line.split(" ")[0])
        block_dict[key] = [size, dirs]

    print(f'This is the cleaned up dict: {block_dict}')

    folder_sizes = 0
    for key in block_dict:
        if int(check_size(block_dict, key)) <= 100000:
            folder_sizes += check_size(block_dict, key)
    
    print(f'This is the final result:\n{folder_sizes}')


def check_size(block_dict, key):
    size = int(block_dict[key][0])
    sub_dirs = block_dict[key][1]
    if not sub_dirs:
        return size
    else:
        for sub_dir in sub_dirs:
            sub_key = f"{key}/{sub_dir}"
            size += check_size(block_dict, sub_key)
    return size

if __name__ == "__main__":
    main()