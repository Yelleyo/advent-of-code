import re

input = 'input.txt'
conversion_done = 0
lowest_location = 10000000000000000000000000000000000000000

def process_block(block, source):
    global conversion_done
    print(block)
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
            print(f"Line output: {source}")
        else:
            print(f"Source not modified: still is {source}")
    print(f"---> This block converted the value to {source}")

    return source
        
def get_seeds():
    global seeds 
    with open(input, 'r') as file:
        seeds = [int(i.group()) for i in re.finditer(r'\d+', file.readline())]
        print(f"Those are the seeds: {seeds}")

get_seeds()
for seed in seeds:
    source = seed
    with open(input, 'r') as file:
        print(f"------------ Working on seed: {seed} ------------")
        block = []
        for line_number, line in enumerate(file, start=1):
            if line_number >= 2:  # Skip the first line
                line = line.strip()
                if line == '' or line[0].isalpha():  # check if the line is empty or starts with a letter
                    if block:  # if there are lines in the block
                        source = process_block(block, source)
                        block = []  # clear the block
                elif line[0].isdigit():  # check if the line starts with a number
                    block.append(line)

        if block:  # process the last block if it's not empty
            source = process_block(block, source)
    print(f"Final location for seed {seed}: {source}")
    # check if source is smaller than prvious one, if yes replace the value
    if lowest_location > source:
        lowest_location = source
    print(f"current lowest location: {lowest_location}")