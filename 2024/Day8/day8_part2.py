# Advent of Code 2024 - Day 8
# Author: Yelleyo

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
    antennas = map_antennas(lines)
    nodes = map_node(antennas, lines)
    unique_nodes = set(nodes)
    print(f'Total amount of nodes: {len(unique_nodes)}')



def map_node(antennas, lines):
    node_list = []
    for key in antennas:
        print(f'\nchecking antennas: {key}')
        antenna_list = antennas[key]
        for i in range(len(antenna_list)):
            node_list.append((antenna_list[i]))
            for j in range(len(antenna_list)):
                if i != j:
                    a = antenna_list[i]
                    b = antenna_list[j]
                    next_node(a, b, lines, node_list)
    return node_list

def next_node(a,b, lines, node_list):
    ax, ay = a
    bx, by = b
    cx = (bx - ax) + bx
    cy = (by - ay) + by
    c = (cx,cy) 
    if 0 <= cx <= len(lines[0]) - 1 and 0 <= cy <= len(lines) -1:
        print(f'point {a}|{b} made: {c}')
        node_list.append((cx,cy))
        next_node(b, c, lines, node_list)
        
def map_antennas(lines):
    map = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            antenna = lines[y][x]
            if antenna not in map:
                map[antenna] = []
            map[antenna].append((x,y))
    del map['.']
    # del map['#']
    print(map)
    return map


if __name__ == '__main__':
    main()
