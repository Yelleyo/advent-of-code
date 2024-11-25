import re


def get_seeds():
    with open('test_input.txt', 'r') as file:
        seeds = [int(i.group()) for i in re.finditer(r'\d+', file.readline())]
        seeds_array = [[seeds[i], seeds[i+1] + seeds[i]] for i in range(0, len(seeds)-1, 2)]
        print(f'This is original seeds_array: {seeds_array}')
        # This is original seeds_array: [[79, 93], [55, 68]]
        return seeds_array

get_seeds()

def get_maps():
    maps = []
    sub_map = [] # Temporary list to hold the current block's values
    with open('test_input.txt', 'r') as file:
        file_content = file.readlines()
        for line_number, line in enumerate(file_content, start=1):
            line = line.strip()
            if line == '' or line[0].isalpha():
                if sub_map:  # Only add to maps if sub_map is not empty
                    maps.append(sub_map)
                sub_map = []  # Start a new block
            elif line[0].isdigit():
                line_info = [int(i) for i in line.split()]
                dest_range_start, source_range_start, range_line = map(int, line_info[:3])
                sub_map.append([source_range_start, (source_range_start + range_line), (dest_range_start - source_range_start)])

    if sub_map:  # Add the last block if it is not empty
        maps.append(sub_map)

    print(f"This is the array of maps: {maps}")
    return maps
                
get_maps()


def main():
    get_seeds()
    get_maps()    






# for pair in seeds_array:
    # start_seed = pair[0]
    # end_seed = pair[1]