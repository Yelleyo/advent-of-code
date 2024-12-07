# Advent of Code 2024 - Day 6
# Author: Yelleyo
import os
import copy

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    with open('test.txt', 'r') as file:
        lines = file.read().splitlines()

    infinite_loop_count = 0

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#' or lines[y][x] == '^':
                continue  # Skip positions that are already '#' or '^'
            
            test_lines = copy.deepcopy(lines)
            test_lines[y] = test_lines[y][:x] + '#' + test_lines[y][x+1:]
            
            print(f'Testing with ({x}, {y}) replaced with #')
            if run_test(test_lines):
                infinite_loop_count += 1

    print(f"Total infinite loops detected: {infinite_loop_count}")

def run_test(lines):
    direction = 'up'
    end = False
    pos = find_start(lines)
    if pos is None:
        print("No starting position found.")
        return False
    
    visited_positions = set()
    visited_states = set()  # To track position and direction
    visited_positions.add(pos)  
    visited_states.add((pos, direction))
    
    print(f'Initial pos: {pos}')
    while not end:
        pos, end, direction = move(lines, pos, direction, visited_positions)
        print(f'I am here now: {pos}, and I will go {direction}')
        if (pos, direction) in visited_states:
            print("Infinite loop detected!")
            return True
        visited_positions.add(pos)
        visited_states.add((pos, direction))
    
    print(f"Total unique positions visited: {len(visited_positions)}")
    return False

def move(lines, pos, direction, visited_positions):
    match direction:
        case 'up':
            return up(lines, pos, visited_positions)
        case 'right':
            return right(lines, pos, visited_positions)
        case 'down':
            return down(lines, pos, visited_positions)
        case 'left':
            return left(lines, pos, visited_positions)

def up(lines, pos, visited_positions):
    x, y = pos
    direction = 'up'
    while y > 0:
        y -= 1
        if lines[y][x] == '#':
            direction = 'right'
            return (x, y + 1), False, direction 
        visited_positions.add((x, y))
    return (x, y), True, direction
    
def right(lines, pos, visited_positions):
    x, y = pos
    direction = 'right'
    while x < len(lines[y]) - 1:
        x += 1
        if lines[y][x] == '#':
            direction = 'down'
            return (x - 1, y), False, direction
        visited_positions.add((x, y))
    return (x, y), True, direction

def down(lines, pos, visited_positions):
    x, y = pos
    direction = 'down'
    while y < len(lines) - 1:
        y += 1
        if lines[y][x] == '#':
            direction = 'left'
            return (x, y - 1), False, direction 
        visited_positions.add((x, y))
    return (x, y), True, direction

def left(lines, pos, visited_positions):
    x, y = pos
    direction = 'left'
    while x > 0:
        x -= 1
        if lines[y][x] == '#':
            direction = 'up'
            return (x + 1, y), False, direction
        visited_positions.add((x, y))
    return (x, y), True, direction

def find_start(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '^':
                return (x, y)
    return None  # Return None if the start position is not found

if __name__ == '__main__':
    main()