# Advent of Code 2022 - Day 5
# Author: Yelleyo

# the stak is a dict of arrays: stack = {1: [Z] ; 2 :... 
# instruction tell when to pop and append box from which array

# Making the initial staks dict 
# for line in the staks replace start at index 2, and every 4 index if not ' ' append to index nb

 

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input_file.txt', 'r') as file:
        content = file.read()
        blocks = content.split("\n\n")
        stack_raw = blocks[0]
        instructions_raw = blocks[1]

        # making the stack dict
        stack_lines = stack_raw.splitlines()
        stack = {}
        for line in stack_lines:
            print(f'this is a line in stack_raw: {line}')
            for i in range(1, len(line), 4):
                if i not in stack:
                    stack[i] = []
                if line[i].isalpha():
                    stack[i].insert(0, line[i])
                if line[i].isnumeric():
                    stack[line[i]] = stack.pop(i)
        
        # making the instruction array
        instructions_lines = instructions_raw.split("\n")
        instructions = []
        for line in instructions_lines:
            amount = int(line.split(" ")[1])
            origin = line.split(" ")[3]
            destination = line.split(" ")[5]
            set = [amount, origin, destination]
            instructions.append(set)
        
        # Applying the instructions
        for instruction in instructions:
            amount = instruction[0]
            origin = instruction[1]
            destination = instruction[2]
            # print(stack)

            for i in range(-amount, 0):
                # print(f'this is i: {i}')
                # print(f'this is stack[origin][i] {stack[origin][i]}')
                if stack[origin]:  # Check if the origin list is not empty
                    # print(f'moving {stack[origin][i]}')
                    to_move = stack[origin][i]
                    stack[destination].append(to_move) 
                    del stack[origin][i]
                else:
                    print(f"The origin {origin} is empty, cannot move any more elements.")
    
    # get the last value for each array in the dict:
    answer = ''
    for key in stack:
        answer += stack[key][-1]

    # print(stack)
    print(answer)

if __name__ == '__main__':
    main()
