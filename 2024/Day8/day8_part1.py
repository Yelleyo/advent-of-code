# Advent of Code 2024 - Day 8
# Author: Yelleyo


# frequencies defined by letter (upper or lower) and digit
#find all nodes that are at a mirror point from each pair of node:
# #--a--a--#  

# for each letter: check all points on the map -> put in a array of coordinates
# iterate over those array of coordinates -> if antonote fir in map -> couter +1 



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
            for j in range(len(antenna_list)):
                if i != j:
                    a1x, a1y = antenna_list[i]
                    a2x, a2y = antenna_list[j]
                    print(f'Comparing point: {a1x},{a1y} with {a2x},{a2y}')
                    node_x = (a2x - a1x)*2 + a1x
                    node_y = (a2y - a1y)*2 + a1y
                    if 0 <= node_x <= len(lines[0]) - 1 and 0 <= node_y <= len(lines) -1:
                        node_list.append((node_x,node_y))
                        print(f'new node at: {node_x},{node_y}')
    return node_list
        
def map_antennas(lines):
    map = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            antenna = lines[y][x]
            if antenna not in map:
                map[antenna] = []
            map[antenna].append((x,y))
    del map['.']
    print(map)
    return map


if __name__ == '__main__':
    main()
