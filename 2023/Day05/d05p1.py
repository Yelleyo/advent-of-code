# make seeds array
# nope # make dict for each of the maps, those will be huge!!
# for each line check if source is in (source + range)
# then output = dest_start + (source_start - dest_start)

import re

input = 'input.txt'
seeds = []

def main():
    get_seeds()


def get_seeds():
    global seeds 
    with open(input, 'r') as file:
            seeds = [int(i.group()) for i in re.finditer(r'\d+', file.readline())]

def io_machine():
    global seeds

with open('test_input.txt', 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if line_number >= 2:  # Skip the first line
            line = line.strip()  # Strip the current line
            while line:  # While the line is not empty
                print(f"line: {line}")
                line_info = [int(i.group()) for i in re.finditer(r'\d+', line)]
                print(f"{line_info}")
                try:
                    line = next(file).strip()  # Read the next line
                except StopIteration:
                    break  # End of file reached



