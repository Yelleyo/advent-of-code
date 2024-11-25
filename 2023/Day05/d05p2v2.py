# same as before but with improvements on perf from OpenAI
# with  progress bar
import re
from tqdm import tqdm

def process_block(block, source, conversion_done):
    if not conversion_done:
        for line in block:
            line_info = [int(i) for i in line.split()]
            source_range_start = int(line_info[1])
            dest_range_start = int(line_info[0])
            range_line = int(line_info[2])
            if source_range_start <= source <= (source_range_start + range_line):
                source = source + (dest_range_start - source_range_start)
                conversion_done = 1
                break  # break early if a match is found
    return source, conversion_done

def get_seeds():
    with open('input.txt', 'r') as file:
        seeds = [int(i.group()) for i in re.finditer(r'\d+', file.readline())]
        seeds_array = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
        return seeds_array

def main():
    seeds_array = get_seeds()
    lowest_location = float('inf')

    # Read file content only once
    with open('input.txt', 'r') as file:
        file_content = file.readlines()

    for pair in tqdm(seeds_array, desc="Processing seeds", unit="pair"):  # Wrap seeds_array with tqdm
        original_seed = pair[0]
        end = original_seed + pair[1]
        while original_seed <= end:
            seed = original_seed
            block = []
            conversion_done = 0
            for line_number, line in enumerate(file_content, start=1):
                if line_number >= 2:
                    line = line.strip()
                    if line == '' or line[0].isalpha():
                        if block:
                            seed, conversion_done = process_block(block, seed, conversion_done)
                            block = []
                    elif line[0].isdigit():
                        block.append(line)

            if block:
                seed, conversion_done = process_block(block, seed, conversion_done)

            if lowest_location > seed:
                lowest_location = seed

            original_seed += 1

        print(f"current lowest location: {lowest_location}")

main()