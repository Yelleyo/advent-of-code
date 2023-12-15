# This is working but very slow. 

import re

input = 'input.txt'
conversion_done = 0

def process_block(block, source):
    global conversion_done
    # print(block)
    conversion_done = 0
    for line in block:
        line_info = [int(i) for i in line.split()]
        # print(line_info)
        source_range_start = int(line_info[1])
        dest_range_start = int(line_info[0])
        range_line = int(line_info[2])
        if source_range_start <= source <= (source_range_start + range_line) and not conversion_done:
            source = source + (dest_range_start - source_range_start)
            conversion_done = 1
            # print(f"Line output: {source}")
        # else:
            # print(f"Source not modified: still is {source}")
    # print(f"---> This block converted the value to {source}")

    return source
        
def get_seeds():
    with open(input, 'r') as file:
        seeds = [int(i.group()) for i in re.finditer(r'\d+', file.readline())]
        seeds_array = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
        print(seeds_array)
        return seeds_array




def main():
    seeds_array = get_seeds()
    lowest_location = float('inf')  # initialize it to infinity

    for pair in seeds_array:
        original_seed = pair[0]
        end = original_seed + pair[1]
        while original_seed <= end:
            seed = original_seed
            # print(f"------------ Working on seed: {seed} ------------")
            with open(input, 'r') as file:
                block = []
                for line_number, line in enumerate(file, start=1):
                    if line_number >= 2:  # Skip the first line
                        line = line.strip()
                        if line == '' or line[0].isalpha():  # check if the line is empty or starts with a letter
                            if block:  # if there are lines in the block
                                seed = process_block(block, seed)  # I assume process_block() returns an updated seed
                                block = []  # clear the block
                        elif line[0].isdigit():  # check if the line starts with a number
                            block.append(line)

                if block:  # process the last block if it's not empty
                    seed = process_block(block, seed)

            if lowest_location > seed:
                lowest_location = seed

            original_seed += 1  # increment the original seed value

        print(f"current lowest location: {lowest_location}")

main()